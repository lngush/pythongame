# config.py

# Размер окна
WIDTH = 800
HEIGHT = 600

# Размер блока
SNAKE_BLOCK = 10

# Цвета
BACKGROUND_COLOR = (144, 238, 144)  # салатовый
SNAKE_COLOR = (0, 0, 0)            # черный
SNAKE_HEAD_COLOR = (30, 30, 30)    # чуть светлее
OBSTACLE_COLOR = (70, 70, 70)      # серые препятствия
FOOD_COLOR = (255, 0, 0)           # красная еда
TEXT_COLOR = (0, 0, 0)

# Шрифты
try:
    import pygame
    FONT_MENU = pygame.font.SysFont("comicsansms", 40)
    FONT_GAME = pygame.font.SysFont("bahnschrift", 25)
except:
    pass  