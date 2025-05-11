# main.py

import pygame
from menu import choose_difficulty, choose_game_mode
from game import run_game

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()

difficulty = choose_difficulty(screen, clock)
game_mode = choose_game_mode(screen, clock)

run_game(screen, clock, difficulty, game_mode)

pygame.quit()