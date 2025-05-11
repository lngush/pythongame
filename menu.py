# menu.py
import pygame
from config import WIDTH, HEIGHT, TEXT_COLOR, FONT_MENU, FONT_GAME, BACKGROUND_COLOR


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    rect = textobj.get_rect()
    rect.topleft = (x, y)
    surface.blit(textobj, rect)


def choose_difficulty(screen, clock):
    choosing = True
    difficulty = 15
    while choosing:
        screen.fill(BACKGROUND_COLOR)
        draw_text("Выберите сложность:", FONT_MENU, TEXT_COLOR, screen, 200, 100)

        draw_text("1 - Легко (медленно)", FONT_GAME, TEXT_COLOR, screen, 250, 200)
        draw_text("2 - Средне (нормально)", FONT_GAME, TEXT_COLOR, screen, 250, 250)
        draw_text("3 - Сложно (быстро)", FONT_GAME, TEXT_COLOR, screen, 250, 300)

        pygame.display.update()
        clock.tick(15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    difficulty = 10
                    choosing = False
                elif event.key == pygame.K_2:
                    difficulty = 15
                    choosing = False
                elif event.key == pygame.K_3:
                    difficulty = 25
                    choosing = False
    return difficulty


def choose_game_mode(screen, clock):
    choosing = True
    mode = "normal"
    while choosing:
        screen.fill(BACKGROUND_COLOR)
        draw_text("Выберите режим игры:", FONT_MENU, TEXT_COLOR, screen, 180, 80)

        draw_text("1 - Обычный", FONT_GAME, TEXT_COLOR, screen, 200, 180)
        draw_text("2 - С препятствиями", FONT_GAME, TEXT_COLOR, screen, 200, 230)
        draw_text("3 - Без границ", FONT_GAME, TEXT_COLOR, screen, 200, 280)

        pygame.display.update()
        clock.tick(15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    mode = "normal"
                    choosing = False
                elif event.key == pygame.K_2:
                    mode = "obstacles"
                    choosing = False
                elif event.key == pygame.K_3:
                    mode = "infinite"
                    choosing = False
    return mode