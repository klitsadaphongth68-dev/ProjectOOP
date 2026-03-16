import os
import random
import pygame
from allflie.settings import ASSET_DIR, ENEMY_IMAGES

class Enemy(pygame.sprite.Sprite):
    TYPE_DATA = {
        'easy': {'score': 10, 'color': (150, 220, 120), 'size': (96, 96)},
        'mid': {'score': 20, 'color': (220, 140, 40), 'size': (108, 108)},
        'bad': {'score': -5, 'color': (220, 50, 50), 'size': (84, 84)},
    }

    def __init__(self, x, y, enemy_type='easy', speed=2.5):
        super().__init__()
        self.type = enemy_type
        self.value = self.TYPE_DATA[enemy_type]['score']
        self.speed = speed
        self.image = self.load_image(ENEMY_IMAGES.get(enemy_type, ''), self.TYPE_DATA[enemy_type]['size'], self.TYPE_DATA[enemy_type]['color'])
        self.rect = self.image.get_rect(center=(x, y))

    def load_image(self, filename, fallback_size, fallback_color):
        path = os.path.join(ASSET_DIR, filename)
        try:
            image = pygame.image.load(path).convert_alpha()
            return pygame.transform.scale(image, fallback_size)
        except Exception:
            surf = pygame.Surface(fallback_size, pygame.SRCALPHA)
            surf.fill(fallback_color)
            return surf

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()

