# game.py

import pygame
import random
from config import WIDTH, HEIGHT, SNAKE_BLOCK, BACKGROUND_COLOR, FOOD_COLOR
from draw import draw_snake, draw_obstacles, score_display


def generate_obstacles(num_obstacles, snake_block):
    obstacles = []
    for _ in range(num_obstacles):
        obs_x = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
        obs_y = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
        obstacles.append([obs_x, obs_y])
    return obstacles


def run_game(screen, clock, difficulty, game_mode):
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0

    obstacles = []
    if game_mode == "obstacles":
        obstacles = generate_obstacles(10, SNAKE_BLOCK)

    while not game_over:

        while game_close:
            screen.fill(BACKGROUND_COLOR)
            font = pygame.font.SysFont("comicsansms", 40)
            msg = font.render("Вы проиграли!", True, (255, 0, 0))
            screen.blit(msg, [280, 150])

            msg = pygame.font.SysFont("bahnschrift", 25).render(
                "Нажмите C - Играть снова или Q - Выход", True, TEXT_COLOR)
            screen.blit(msg, [180, 250])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        run_game(screen, clock, difficulty, game_mode)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        x1 += x1_change
        y1 += y1_change

        # Режим "без границ"
        if game_mode == "infinite":
            if x1 >= WIDTH:
                x1 = 0
            elif x1 < 0:
                x1 = WIDTH - SNAKE_BLOCK
            if y1 >= HEIGHT:
                y1 = 0
            elif y1 < 0:
                y1 = HEIGHT - SNAKE_BLOCK

        # Проверка столкновения со стеной
        elif game_mode == "normal" or game_mode == "obstacles":
            if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
                game_close = True

        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, FOOD_COLOR, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])

        if game_mode == "obstacles":
            draw_obstacles(obstacles, screen)

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Проверка столкновения с собой
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        # Проверка столкновения с препятствием
        if game_mode == "obstacles":
            for obs in obstacles:
                if x1 == obs[0] and y1 == obs[1]:
                    game_close = True

        draw_snake(SNAKE_BLOCK, snake_list, screen)
        score_display(length_of_snake - 1, screen)

        pygame.display.update()

        # Поедание еды
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(difficulty)