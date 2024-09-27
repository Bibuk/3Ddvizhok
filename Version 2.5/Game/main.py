#main.py
from const import Settings
from player import Player
from rendering import Rendering
from Map import world_map
from RayCasting import raycasting
import pygame
import math

# Инициализация Pygame и основных переменных
conf = Settings()
pygame.init()
sc = pygame.display.set_mode((conf.WIDTH, conf.HEIGHT))
clock = pygame.time.Clock()

pl = Player()
rendering = Rendering(sc)  # Создаем объект rendering с экраном

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    # Движение игрока
    pl.movement()
    
    # Отрисовка
    rendering.background()  
    rendering.world(pl.pos, pl.angle)  # Отрисовка мира с позиции игрока
    fps = clock.get_fps()
    rendering.fps(fps)  # Отображение FPS

    # Обновление экрана
    pygame.display.flip()
    clock.tick(conf.FPS)