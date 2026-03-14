import os
import pygame
from allflie.settings import (
    PLAYER_SPEED,
    ASSET_DIR,
    PLAYER_STAND_IMAGE,
    PLAYER_RUN_IMAGE,
    PLAYER_SHOOT_IMAGE,
    BOUNDARY_LINE_X,
)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = {
            'stand': self.load_image(PLAYER_STAND_IMAGE, (40, 40), (50, 150, 240)),
            'run': self.load_image(PLAYER_RUN_IMAGE, (40, 40), (70, 180, 255)),
            'shoot': self.load_image(PLAYER_SHOOT_IMAGE, (40, 40), (255, 255, 0)),
        }
        self.state = 'stand'
        self.image = self.images[self.state]
        self.rect = self.image.get_rect(center=(x, y))

    def load_image(self, filename, fallback_size, fallback_color):
        path = os.path.join(ASSET_DIR, filename)
        try:
            image = pygame.image.load(path).convert_alpha()
            return pygame.transform.scale(image, fallback_size)
        except Exception:
            surface = pygame.Surface(fallback_size, pygame.SRCALPHA)
            surface.fill(fallback_color)
            return surface

    def update(self):
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        self.state = 'stand'

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy = -PLAYER_SPEED
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy = PLAYER_SPEED
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx = -PLAYER_SPEED
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx = PLAYER_SPEED

        if dx != 0 or dy != 0:
            self.state = 'run'

        if keys[pygame.K_SPACE]:
            self.state = 'shoot'

        self.rect.x += dx
        self.rect.y += dy

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > BOUNDARY_LINE_X:
            self.rect.right = BOUNDARY_LINE_X
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > pygame.display.get_surface().get_height():
            self.rect.bottom = pygame.display.get_surface().get_height()

        self.image = self.images[self.state]

