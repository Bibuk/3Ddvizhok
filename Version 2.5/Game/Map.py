#Map.py
from const import Settings

conf = Settings()

text_map = [
    '111111111111',
    '1.......1..1',
    '1..111.....1',
    '1.......1..1',
    '1.1.....1..1',
    '1.111...11.1',
    '1.....1....1',
    '111111111111'
]

world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == '1':
            world_map.add((i * conf.TILE, j * conf.TILE))
