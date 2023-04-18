import pygame
import sys
import degrees_to_velocity

pygame.init()

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# экран
screen_width = 1366  # ширина экрана в пикселях
screen_height = 768  # высота экрана в пикселях
screen = pygame.display.set_mode((screen_width, screen_height))  # экран
pygame.display.set_caption("Пин - Понг")

# игрок 1
player_1_width = 5  # ширина игрока в пикселях
player_1_height = 75  # высота игрока в пикселях
player_1_x = 50
player_1_y = screen_height // 2 - player_1_height // 2
player_1_score = 0
player_1 = pygame.Rect((player_1_x, player_1_y, player_1_width, player_1_height))  # координаты x и y, ширина, высота

# игрок 2
player_2_width = 5  # ширина игрока в пикселях
player_2_height = 75  # высота игрока в пикселях
player_2_x = screen_width - player_2_width - 50
player_2_y = screen_height // 2 - player_1_height // 2
player_2_score = 0
player_2 = pygame.Rect((player_2_x, player_2_y, player_2_width, player_2_height))  # координаты x и y, ширина, высота

# мяч
ball_width = 5  # ширина мяча в пикселях
ball_height = 5  # высота мяча в пикселях
ball_x = screen_width // 2 - ball_width // 2
ball_y = screen_height // 2 - ball_height // 2
velocity = degrees_to_velocity.degrees_to_velocity(45, 2)
ball_speed_x = velocity[0]
ball_speed_y = velocity[1]
ball = pygame.Rect((ball_x, ball_y, ball_width, ball_height))  # координаты x и y, ширина, высота

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
        player_1.y -= 2  # игрок 1 поднялся вверх
        if player_1.y < 0:
            player_1.y = 0
    if keys[pygame.K_s]:
        player_1.y += 2
        if player_1.y > screen_height - player_1_height:
            player_1.y = screen_height - player_1_height  # игрок 1 опустился вниз

    # движение игрока 2
    if keys[pygame.K_UP]:
        player_2.y -= 2  # игрок 2 поднялся вверх
        if player_2.y < 0:
            player_2.y = 0
    if keys[pygame.K_DOWN]:
        player_2.y += 2
        if player_2.y > screen_height - player_2_height:
            player_2.y = screen_height - player_2_height  # игрок 2 опустился вниз

    # движение мячика
    ball.x -= ball_speed_x  # мяч всегда движется со своей скоростью по x
    ball.y -= ball_speed_y  # мяч всегда движется со своей скоростью по y
    if ball.x < 0:  # мяч вылетел за левую границу экрана
        ball_speed_x *= -1  # переворачиваем скорость (меняем знак)
    if ball.x > screen_width - ball_width:  # мяч вылетел за правую границу экрана
        ball_speed_x *= -1
    if ball.y < 0:  # мяч вылетел за верхнюю границу экрана
        ball_speed_y *= -1
    if ball.y > screen_height - ball_height:  # мяч вылетел за нижнюю границу экрана
        ball_speed_y *= -1

    # отрисовка
    screen.fill((BLACK))
    pygame.draw.rect(screen, WHITE, player_1)  # рисуем игрока 1
    pygame.draw.rect(screen, WHITE, player_2)  # рисуем игрока 2
    pygame.draw.rect(screen, WHITE, ball)  # рисуем мячик
    pygame.display.flip()  #обновляем экран 

    clock.tick(1500)  # количество кадров в секунду

