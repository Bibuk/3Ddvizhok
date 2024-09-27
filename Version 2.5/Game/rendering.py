#rendering.py
import pygame
from RayCasting import raycasting
from const import Settings

conf = Settings()


class Rendering:
    def __init__(self, sc):
        self.sc = sc
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.texture = pygame.image.load('c:/Users/Roman/Desktop/Version/Version 2.5/Game/img/photo1.png').convert()

    def background(self):
        # Верхняя и нижняя часть экрана (небо и земля)
        pygame.draw.rect(self.sc, (77, 143, 172), (0, 0, conf.WIDTH, conf.HALF_HEIGHT))
        pygame.draw.rect(self.sc, (26, 26, 26), (0, conf.HALF_HEIGHT, conf.WIDTH, conf.HALF_HEIGHT))

    def world(self, player_pos, player_angle):
        raycasting(self.sc, player_pos, player_angle, self.texture)  # Вызов функции ray_casting для отрисовки

    def fps(self, fps):
        display_fps = str(int(fps))
        render = self.font.render(display_fps, 0, (0, 205, 0))
        self.sc.blit(render, (conf.WIDTH - 65, 5))  # Позиция FPS на экране