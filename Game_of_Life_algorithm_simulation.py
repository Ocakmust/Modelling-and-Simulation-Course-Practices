import pygame
import sys
import random

screen_width = 800
screen_height = 600
rows = 30
cols = 50
cell_width = screen_width // cols
cell_height = screen_height // rows
pygame.init()

grid = [[0 for i in range(cols)] for j in range(rows)]
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game of Life")

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)


game_running = False

def draw():
    for row in range(rows):
        for col in range(cols):
            color = blue if grid[row][col] == 1 else white
            rect = pygame.Rect(col * cell_width, row * cell_height, cell_width, cell_height)
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, black, rect, 1)

def count_cells(row, col):
    cell = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            new_row = (row + i) % rows
            new_col = (col + j) % cols
            cell += grid[new_row][new_col]
    return cell

def upt():
    new_grid = [[0 for i in range(cols)] for j in range(rows)]
    for row in range(rows):
        for col in range(cols):
            neighbors = count_cells(row, col)
            if grid[row][col] == 1: 
                if neighbors == 2 or neighbors == 3:
                    new_grid[row][col] = 1
            else:  
                if neighbors == 3:
                    new_grid[row][col] = 1
    return new_grid

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_running = not game_running
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game_running:
                x, y = pygame.mouse.get_pos()
                col = x // cell_width
                row = y // cell_height
                grid[row][col] = 1 - grid[row][col]  

    screen.fill(white)

    draw()

    if game_running:
        grid = upt()

    pygame.display.flip()
