"""
SNAKE GAME🐍
"""

#pip install pygame
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Snake Game')

#Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 100, 0)
RED = (220, 20, 60)
BG = (30, 30, 30)
GRID_COLOR = (50, 50, 50)

#Snake
snake = [(100, 50)]
direction = (10, 0)
food = (300, 200)

# Font
font = pygame.font.SysFont("Arial", 24, bold=True)

def draw_grid():
    for x in range(0, 600, 10):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, 400))
    for y in range(0, 400, 10):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (600, y))

def draw_snake():
    for i, part in enumerate(snake):
        # lighter head color
        color = GREEN if i == 0 else DARK_GREEN
        pygame.draw.rect(screen, color, (*part, 10, 10))
        pygame.draw.rect(screen, BG, (*part, 10, 10), 1)  # borda

def draw_food():
    pygame.draw.circle(screen, RED, (food[0] + 5, food[1] + 5), 5)

def draw_score():
    score = font.render(f"Score: {len(snake)-1}", True, WHITE)
    screen.blit(score, (10, 10))

def draw():
    screen.fill(BG)
    draw_grid()
    draw_snake()
    draw_food()
    draw_score()
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

    if new_head in snake[1:] or new_head[0] < 0 or new_head[0] >= 600 or new_head[1] < 0 or new_head[1] >= 400:
        screen.fill(BG)
        game_over_text = font.render("GAME OVER", True, RED)
        screen.blit(game_over_text, (220, 180))
        pygame.display.update()
        pygame.time.delay(2000)
        running = False

    draw()
    clock.tick(10)

pygame.quit()
