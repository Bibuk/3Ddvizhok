#const.py
import math
import pygame

# Разрешение экрана
class Settings:
    WIDTH = 1200
    HEIGHT = 800
    HALF_WIDTH = WIDTH // 2
    HALF_HEIGHT = HEIGHT // 2
    FPS = 120
    TILE = 64

    # настройка лучей
    FOV = math.pi / 3
    HALF_FOV = FOV / 2
    NUM_RAYS = 300
    MAX_DEPTH = 1200
    DELTA_ANGLE = FOV / NUM_RAYS
    DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
    PROJ_COEFF = 3 * DIST * TILE
    SCALE = WIDTH // NUM_RAYS

    # Настройки игрока 
    player_pos = (HALF_WIDTH, HALF_HEIGHT)
    player_angle = 0
    player_speed = 2

    # Настройка текстур
    TEXTURE_WIDTH = 64
    TEXTURE_HEIGHT = 64
    TEXTURE_SCALE = TEXTURE_WIDTH // TILE