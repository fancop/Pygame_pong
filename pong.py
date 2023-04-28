"""
TODO:
    крутить мяч при отскоку от ракетки:
        ракетка едет вниз - мяч закручивается вверх
        ракетка едет вверх - мяч закручивается вниз
    звуки: гол мне и противнику, отскок
    противник слишком сильный!
    выбрать режим игры: с БОТом или человеком
    уровень сложности
"""

import pygame
import sys
from degrees_to_velocity import degrees_to_velocity
from random import randint

pygame.init()

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 1000

player_1_width = 5  # ширина игрока в пикселях
player_1_height = 75  # высота игрока в пикселях
player_1 = pygame.Rect((0, 0, player_1_width, player_1_height))  # координаты x и y, ширина, высота

player_2_width = 5  # ширина игрока в пикселях
player_2_height = 75  # высота игрока в пикселях
player_2 = pygame.Rect((0, 0, player_2_width, player_2_height))  # координаты x и y, ширина, высота

def players_to_center():
    player_1.x = screen_width * 0.1
    player_1.y = screen_height // 2 - player_1_height // 2
    player_2.x = screen_width * 0.9 - player_2_width
    player_2.y = screen_height // 2 - player_1_height // 2

# экран
screen_info = pygame.display.Info()  # собираем информацию о экране
screen_width = screen_info.current_w  # ширина экрана в пикселях
screen_height = screen_info.current_h  # высота экрана в пикселях
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)  # экран
pygame.display.set_caption("Пин - Понг")

# игрок 1
player_1_x = 50
player_1_score = 0  # забитые голы 1 игрока
player_1_speed = 2
players_to_center()

# игрок 2
player_2_x = screen_width - player_2_width - 50
player_2_score = 0  # забитые голы 2 игрока
player_2_speed = 2
players_to_center()


# мяч
# сброс мяча
def ball_to_center() -> tuple:
    ball.x = screen_width // 2 - ball_width // 2
    ball.y = screen_height // 2 - ball_height // 2

def rotate_ball():
    if randint(0, 1) == 0:
        direction = randint(255, 315)
    else:
        direction = randint(90, 135)
    velocity = degrees_to_velocity(direction, 2)
    return velocity

ball_width = 5  # ширина мяча в пикселях
ball_height = 5  # высота мяча в пикселях
ball_speed = 2
ball = pygame.Rect((0, 0, ball_width, ball_height))  # координаты x и y, ширина, высота
ball_to_center()
velocity = rotate_ball()
ball_speed_x = velocity[0]
ball_speed_y = velocity[1]

clock = pygame.time.Clock()

# табло
score_left = pygame.font.Font(None, 60)
score_right = pygame.font.Font(None, 60)

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


    # движение игрока 1
    keys = pygame.key.get_pressed()  # собираем нажатые клавиши
    if keys[pygame.K_w]:  # обрабатываем нажатые клавиши
        player_1.y -= player_1_speed  # игрок 1 поднялся вверх
        if player_1.y < 0:
            player_1.y = 0
    if keys[pygame.K_s]:
        player_1.y += player_1_speed
        if player_1.y > screen_height - player_1_height:
            player_1.y = screen_height - player_1_height  # игрок 1 опустился вниз
    """     
    # движение игрока 2
    if keys[pygame.K_UP]:
        player_2.y -= player_2_speed  # игрок 2 поднялся вверх
        if player_2.y < 0:
            player_2.y = 0
    if keys[pygame.K_DOWN]:
        player_2.y += player_2_speed
        if player_2.y > screen_height - player_2_height:
            player_2.y = screen_height - player_2_height  # игрок 2 опустился вниз
    """
    # логика
    # движение мячика
    ball.x -= ball_speed_x  # мяч всегда движется со своей скоростью по x
    ball.y -= ball_speed_y  # мяч всегда движется со своей скоростью по y

    # противник БОТ
    if ball.centery < player_2.centery:  # мяч выще ракетки
        player_2.y -= player_2_speed 
    if ball.centery > player_2.centery:  # мяч ниже ракетки
        player_2.y += player_2_speed 
        
    
    # голы
    # гол правого игрока
    if ball.x < 0:  # мяч вылетел за левую границу экрана
        player_2_score += 1
        ball_to_center()
        players_to_center()
        velocity = rotate_ball()
        ball_speed_x = velocity[0]
        ball_speed_y = velocity[1]
        pygame.time.delay(1000)

    # гол левого игрока
    if ball.x > screen_width - ball_width:  # мяч вылетел за правую границу экрана
        player_1_score += 1
        ball_to_center()
        players_to_center()
        velocity = rotate_ball()
        ball_speed_x = velocity[0]
        ball_speed_y = velocity[1]
        pygame.time.delay(1000)
        

    # вылеты в верх и низ
    if ball.y < 0:  # мяч вылетел за верхнюю границу экрана
        ball_speed_y *= -1
    if ball.y > screen_height - ball_height:  # мяч вылетел за нижнюю границу экрана
        ball_speed_y *= -1

    # отскок от ракеток
    if ball.colliderect(player_1) or ball.colliderect(player_2):
        ball_speed_x *= -1

    # отрисовка
    screen.fill((BLACK))
    pygame.draw.rect(screen, WHITE, player_1)  # рисуем игрока 1
    pygame.draw.rect(screen, WHITE, player_2)  # рисуем игрока 2
    pygame.draw.rect(screen, WHITE, ball)  # рисуем мячик
    score_left_img = score_left.render(str(player_1_score), True, WHITE)
    score_right_img = score_left.render(str(player_2_score), True, WHITE)
    screen.blit(score_left_img, (screen_width * 0.25, 20))
    screen.blit(score_right_img, (screen_width * 0.72, 20))
    pygame.display.flip()  #обновляем экран 

    clock.tick(FPS)  # количество кадров в секунду

