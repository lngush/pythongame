# draw.py

import pygame
from config import SNAKE_BLOCK, SNAKE_COLOR, SNAKE_HEAD_COLOR, OBSTACLE_COLOR, FOOD_COLOR, TEXT_COLOR, FONT_GAME


def draw_snake(snake_block, snake_list, screen):
    for i, block in enumerate(snake_list):
        color = SNAKE_HEAD_COLOR if i == len(snake_list) - 1 else SNAKE_COLOR
        pygame.draw.rect(screen, color, [block[0], block[1], snake_block, snake_block])


def draw_obstacles(obstacles, screen):
    for obs in obstacles:
        pygame.draw.rect(screen, OBSTACLE_COLOR, [obs[0], obs[1], SNAKE_BLOCK, SNAKE_BLOCK])


def score_display(score, screen):
    value = FONT_GAME.render(f"Счёт: {score}", True, TEXT_COLOR)
    screen.blit(value, [10, 10])