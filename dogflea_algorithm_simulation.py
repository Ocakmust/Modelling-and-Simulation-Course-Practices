import random


n = 20
initial_state = (20, 0)
num_simulations = 20


def simulation():
    init_state=list(initial_state)
    state = list(initial_state)
    itr = 0

    while True:
        itr += 1
        rand_num=random.random()
        curr_state=state[0]/n

        if rand_num < state[0]/n:
            state[0] -= 1
            state[1] += 1
        else:
            state[0] += 1
            state[1] -= 1  

        if itr<21:
            print(f" Iteration {itr}: Random Number= {rand_num:.2f}, State = {state} ")
            

        if state==init_state:
            print(f"Came back to initial state at {itr}th iteration")
            break 

    return itr
    
total_itr=0    

for sim in range(1, num_simulations + 1):
    print(f"Simulation number {sim}:")
    itr = simulation()
    total_itr += itr
    print()

print(f"Avarage number of iterations is -> {total_itr/num_simulations}, Expected resault -> 2^20={2**200}")

