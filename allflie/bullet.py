import os
import pygame
from allflie.settings import ASSET_DIR, POWER_IMAGE

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = self.load_image(POWER_IMAGE, 36, (255, 230, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 12

    def load_image(self, filename, size, color):
        try:
            path = os.path.join(ASSET_DIR, filename)
            image = pygame.image.load(path).convert_alpha()
            return pygame.transform.scale(image, (size, size))
        except Exception:
            surf = pygame.Surface((size, size), pygame.SRCALPHA)
            pygame.draw.circle(surf, color, (size // 2, size // 2), size // 2)
            return surf

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > pygame.display.get_surface().get_width():
            self.kill()
