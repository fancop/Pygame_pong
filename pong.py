import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# экран
screen_width = 800  # ширина экрана в пикселях
screen_height = 600  # высота экрана в пикселях
screen = pygame.display.set_mode((screen_width, screen_height))  # экран
pygame.display.set_caption("ПинПонг")

# игрок 1
player_1_width = 5  # ширина игрока в пикселях
player_1_height = 75  # высота игрока в пикселях
player_1_x = 50
player_1_y = screen_height // 2 - player_1_height // 2
player_1 = pygame.Rect(
    player_1_x, player_1_y, player_1_width, player_1_height
)  # координаты x и y, ширина, высота

# игрок 2
player_2_width = 5  # ширина игрока в пикселях
player_2_height = 75  # высота игрока в пикселях
player_2_x = screen_width - player_2_width - 50
player_2_y = screen_height // 2 - player_1_height // 2
player_2 = pygame.Rect(
    player_2_x, player_2_y, player_2_width, player_2_height
)  # координаты x и y, ширина, высота

# мяч
ball_width = 5  # ширина мяча в пикселях
ball_height = 5  # высота мяча в пикселях
ball_x = screen_width // 2 - ball_width // 2
ball_y = screen_height // 2 - ball_height // 2
ball = pygame.Rect(
    ball_x, ball_y, ball_width, ball_height
)  # координаты x и y, ширина, высота

# главный цикл
while True: 
    events = pygame.event.get()  # собираем все события
    for event in events:  # читаю все события
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # нажатая клавиша
                pygame.quit()
                sys.exit()

    keys = pygame.key.get_pressed()  # собираем нажатые клавиши
    if keys[pygame.K_w]:  # обрабатываем нажатые клавиши
        player_1.y -= 1  # игрок 1 поднялся вверх
        if player_1.y < 0:
            player_1.y = 0
    if keys[pygame.K_s]:
        player_1.y += 1
        if player_1.y > screen_height - player_1_height:
            player_1.y = screen_height - player_1_height  # игрок 1 опустился вниз

    if keys[pygame.K_UP]:
        player_2.y -= 1  # игрок 2 поднялся вверх
        if player_2.y < 0:
            player_2.y = 0
    if keys[pygame.K_DOWN]:
        player_2.y += 1
        if player_2.y > screen_height - player_2_height:
            player_2.y = screen_height - player_2_height  # игрок 2 опустился вниз

    ball_x += 1
    ball_y += 1

    # отрисовка
    screen.fill((BLACK))
    pygame.draw.rect(screen, WHITE, player_1)  # рисуем игрока 1
    pygame.draw.rect(screen, WHITE, player_2)  # рисуем игрока 2
    pygame.draw.rect(screen, WHITE, ball)  # рисуем мячик
    pygame.display.flip()  #обновляем экран 

