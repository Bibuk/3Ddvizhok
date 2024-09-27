# RayCasting.py
import pygame
import math
from const import Settings
from Map import world_map

conf = Settings()

def mapping(a, b):
    return (a // conf.TILE) * conf.TILE, (b // conf.TILE) * conf.TILE

def raycasting(sc, player_pos, player_angle, texture):
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - conf.HALF_FOV
    for ray in range(conf.NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001

        # verticals
        x, dx = (xm + conf.TILE, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, conf.WIDTH, conf.TILE):
            depth_v = (x - ox) / cos_a
            yv = oy + depth_v * sin_a
            if mapping(x + dx, yv) in world_map:
                break
            x += dx * conf.TILE

        # horizontals
        y, dy = (ym + conf.TILE, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, conf.HEIGHT, conf.TILE):
            depth_h = (y - oy) / sin_a
            xh = ox + depth_h * cos_a
            if mapping(xh, y + dy) in world_map:
                break
            y += dy * conf.TILE

        # projection
        depth, offset = (depth_v, yv) if depth_v < depth_h else (depth_h, xh)
        offset = int(offset) % conf.TILE
        depth *= math.cos(player_angle - cur_angle)
        depth = max(depth, 0.00001)
        proj_height = min(int(conf.PROJ_COEFF / depth), 2 * conf.HEIGHT)

        wall_column = texture.subsurface(offset * conf.TEXTURE_SCALE, 0, conf.TEXTURE_SCALE, conf.TEXTURE_HEIGHT)
        wall_column = pygame.transform.scale(wall_column, (conf.SCALE, proj_height))
        sc.blit(wall_column, (ray * conf.SCALE, conf.HALF_HEIGHT - proj_height // 2))

        cur_angle += conf.DELTA_ANGLE