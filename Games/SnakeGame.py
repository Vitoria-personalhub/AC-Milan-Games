"""
SNAKE GAME🐍
"""

#pip install pygame
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Snake Game')

snake = [(100, 50)]
direction = (10, 0)
food = (300, 200)

def draw():
    screen.fill((0, 0, 0))
    for part in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*part, 10, 10))

    pygame.draw.rect(screen, (255, 0, 0), (*food, 10, 10))
    pygame.display.update()

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 10):
                direction = (0, -10)
            elif event.key == pygame.K_DOWN and direction != (0, -10):
                direction = (0, 10)
            elif event.key == pygame.K_LEFT and direction != (10, 0):
                direction = (-10, 0)
            elif event.key == pygame.K_RIGHT and direction != (-10, 0):
                direction = (10, 0)

    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)

    if new_head == food:
        food = (random.randrange(0, 600, 10), random.randrange(0, 400, 10))
    else:
        snake.pop()

    if new_head in snake[1:]:
        print('''
        \033[31mGAME OVER\033[m
        \033[1mSnake bumped into itself!\033[m''')
        running = False

    if new_head[0] < 0 or new_head[0] >= 600:
        print('''
        \033[31mGAME OVER\033[m
        \033[1mSnake hits the wall!\033[m''')
        running = False

    if new_head[1] < 0 or new_head[1] >= 400:
        print('''
        \033[31mGAME OVER\033[m
        \033[1mSnake hits the wall!\033[m''')
        running = False

    draw()
    clock.tick(15)

pygame.quit()
