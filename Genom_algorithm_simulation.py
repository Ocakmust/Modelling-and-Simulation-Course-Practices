import random
import math

def calculate_road(road_list):
    total_road = 0
    text = ""
    x1, y1 = None, None

    for key, (x2, y2) in road_list.items():
        if x1 is not None:
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            total_road += distance
        text += str(key)
        x1, y1 = x2, y2

    first_key, (x_first, y_first) = next(iter(road_list.items()))
    distance_to_first = math.sqrt((x_first - x1) ** 2 + (y_first - y1) ** 2)
    total_road += distance_to_first

    return {text: total_road}

def choose_mating(genom_dict):
    fitness_values = [1 / distance for distance in genom_dict.values()]
    total_fitness = sum(fitness_values)

    cumulative_probabilities = []
    cumulative_sum = 0
    for fitness in fitness_values:
        cumulative_sum += fitness / total_fitness
        cumulative_probabilities.append(cumulative_sum)

    random_value = random.random()
    for i, c_probability in enumerate(cumulative_probabilities):
        if random_value <= c_probability:
            return i
    return len(cumulative_probabilities) - 1

def initialize_population(num_cities, population_size):
    population = []
    for _ in range(population_size):
        route = list(range(num_cities))
        random.shuffle(route)
        population.append(route)
    return population

def order_crossover(parent1, parent2):
    size = len(parent1)
    cut1, cut2 = sorted(random.sample(range(size), 2))

    child = [None] * size
    child[cut1:cut2] = parent1[cut1:cut2]

    current_pos = cut2
    for city in parent2:
        if city not in child:
            if current_pos >= size:
                current_pos = 0
            child[current_pos] = city
            current_pos += 1

    return child

def mutate(route, mutation_rate):
    for i in range(len(route)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(route) - 1)
            route[i], route[j] = route[j], route[i]
    return route

def create_road_dict(route, city_positions):
    return {i: city_positions[int(i)] for i in route}

def genetic_algorithm(city_positions, num_generations=1000, population_size=100, mutation_rate=0.005):
    num_cities = len(city_positions)
    population = initialize_population(num_cities, population_size)

    best_route = None
    best_distance = float('inf')

    for generation in range(num_generations):
        fitness_dict = {}
        for route in population:
            road_dict = create_road_dict(route, city_positions)
            result = calculate_road(road_dict)
            fitness_dict.update(result)

        mating_pool = [population[choose_mating(fitness_dict)] for _ in range(population_size)]

        next_generation = []
        for i in range(0, population_size, 2):
            parent1 = mating_pool[i]
            parent2 = mating_pool[i + 1]

            child1= order_crossover(parent1, parent2)
            child2= order_crossover(parent2, parent1)

            next_generation.extend([mutate(child1, mutation_rate), mutate(child2, mutation_rate)])

        population = next_generation

        for route in population:
            road_dict = create_road_dict(route, city_positions)
            distance = list(calculate_road(road_dict).values())[0]
            if distance < best_distance:
                best_distance = distance
                best_route = route

        print(f"Generation {generation + 1}: Best Distance = {best_distance:.2f}")

    return best_route, best_distance

if __name__ == "__main__":
    N = int(input("Enter the number of cities: "))
    city_locs = {}

    for i in range(N):
        cord = input(f"Enter coordinates of city {i}: ")
        x, y = map(float, cord.split())
        city_locs[i] = (x, y)

    best_route, best_distance = genetic_algorithm(city_locs)
    print(f"\nBest route: {best_route}")
    print(f"Total distance: {best_distance:.2f}")
