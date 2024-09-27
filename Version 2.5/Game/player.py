#player.py
import pygame
import math
from const import Settings

conf = Settings()

class Player:
    def __init__(self):
        self.x, self.y = conf.player_pos
        self.angle = conf.player_angle
        self.speed_forward = conf.player_speed
        self.speed_side = 1
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.x += self.speed_forward * cos_a
            self.y += self.speed_forward * sin_a
        if keys[pygame.K_s]:
            self.x -= self.speed_forward * cos_a
            self.y -= self.speed_forward * sin_a
        if keys[pygame.K_d]:
            self.x -= self.speed_side * sin_a
            self.y += self.speed_side * cos_a
        if keys[pygame.K_a]:
            self.x += self.speed_side * sin_a
            self.y -= self.speed_side * cos_a

        # Повороты
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02

        # Управление мышью
        mouse_dx, _ = pygame.mouse.get_rel()
        self.angle += mouse_dx * 0.002
