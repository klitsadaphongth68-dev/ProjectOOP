import os
import random
import pygame
import sys
from allflie.settings import (
    WIDTH,
    HEIGHT,
    FPS,
    BACKGROUND_COLOR,
    ASSET_DIR,
    BACKGROUND_IMAGE,
    BOUNDARY_LINE_X,
)
from allflie.player import Player
from allflie.enemy import Enemy
from allflie.bullet import Bullet

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("ProjectOOP Pygame Shooter")
        self.clock = pygame.time.Clock()
        self.running = True

        self.background = self.load_background(BACKGROUND_IMAGE)

        self.all_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()

        self.player = Player(BOUNDARY_LINE_X // 2, HEIGHT // 2)
        self.all_sprites.add(self.player)

        self.state = 'MENU'
        self.difficulty = 'normal'
        self.difficulties = ['easy', 'normal', 'hard']
        self.diff_idx = 1
        
        # Menu UI rects
        self.font_title = pygame.font.SysFont(None, 72)
        self.font_menu = pygame.font.SysFont(None, 48)
        self.btn_play = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 - 50, 200, 50)
        self.btn_diff = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 20, 200, 50)
        self.btn_exit = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 90, 200, 50)

        self.score = 0
        self.is_game_over = False
        self.spawn_timer = 0
        self.spawn_delay = 1000
        self.start_time = pygame.time.get_ticks()

    def reset_game(self):
        self.score = 0
        self.is_game_over = False
        self.spawn_timer = 0
        self.spawn_delay = 1000
        self.start_time = pygame.time.get_ticks()
        self.enemy_sprites.empty()
        self.bullet_sprites.empty()
        self.all_sprites.empty()
        self.player = Player(BOUNDARY_LINE_X // 2, HEIGHT // 2)
        self.all_sprites.add(self.player)
        self.state = 'PLAYING'


    def load_background(self, filename):
        path = os.path.join(ASSET_DIR, filename)
        try:
            image = pygame.image.load(path).convert()
            return pygame.transform.scale(image, (WIDTH, HEIGHT))
        except Exception:
            return None

    def spawn_enemy(self):
        # spawn at rightmost edge (just outside screen) for incoming enemies
        enemy_x = WIDTH + 20
        enemy_y = random.randint(40, HEIGHT - 40)
        spawn_roll = random.random()

        if spawn_roll < 0.55:
            etype = 'easy'
        elif spawn_roll < 0.85:
            etype = 'mid'
        else:
            etype = 'bad'

        elapsed_seconds = (pygame.time.get_ticks() - self.start_time) / 1000
        
        diff_multiplier = 1.0
        if self.difficulty == 'easy':
            diff_multiplier = 0.6
        elif self.difficulty == 'hard':
            diff_multiplier = 1.5

        # เพิ่มความเร็วแบบช้า ๆ เพื่อความเล่นได้ (ไม่ฉับพลัน)
        speed = (1.5 + min(3.0, elapsed_seconds / 10)) * diff_multiplier

        enemy = Enemy(enemy_x, enemy_y, enemy_type=etype, speed=speed)
        self.enemy_sprites.add(enemy)
        self.all_sprites.add(enemy)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if self.state == 'MENU':
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if self.btn_play.collidepoint(pos):
                        self.reset_game()
                    elif self.btn_diff.collidepoint(pos):
                        self.diff_idx = (self.diff_idx + 1) % len(self.difficulties)
                        self.difficulty = self.difficulties[self.diff_idx]
                    elif self.btn_exit.collidepoint(pos):
                        self.running = False
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.state = 'MENU'
                    if not self.is_game_over and event.key == pygame.K_SPACE:
                        bullet = Bullet(self.player.rect.right + 10, self.player.rect.centery)
                        self.bullet_sprites.add(bullet)
                        self.all_sprites.add(bullet)

    def update(self):
        if self.state == 'MENU':
            return
            
        if self.is_game_over:
            return

        t = pygame.time.get_ticks()
        if t - self.spawn_timer >= self.spawn_delay:
            self.spawn_enemy()
            self.spawn_timer = t
            self.spawn_delay = max(300, 1000 - int((t - self.start_time) / 120))

        self.all_sprites.update()

        hits = pygame.sprite.groupcollide(self.bullet_sprites, self.enemy_sprites, True, True)
        for bullet, enemies in hits.items():
            for enemy in enemies:
                self.score += enemy.value

        for enemy in self.enemy_sprites:
            # enemy3 (bad) จะปล่อยผ่านได้ โดยไม่แพ้ แต่ชนโดนจะยังเสียคะแนน -5
            if enemy.rect.left <= BOUNDARY_LINE_X:
                if enemy.type != 'bad':
                    self.is_game_over = True

    def draw_menu(self):
        if self.background:
            self.screen.blit(self.background, (0, 0))
        else:
            self.screen.fill(BACKGROUND_COLOR)

        title = self.font_title.render("COWBOY VS SLIME", True, (255, 200, 0))
        self.screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//2 - 150))

        pygame.draw.rect(self.screen, (50, 200, 50), self.btn_play, border_radius=10)
        play_txt = self.font_menu.render("PLAY", True, (255, 255, 255))
        self.screen.blit(play_txt, (self.btn_play.centerx - play_txt.get_width()//2, self.btn_play.centery - play_txt.get_height()//2))

        pygame.draw.rect(self.screen, (200, 150, 50), self.btn_diff, border_radius=10)
        diff_txt = self.font_menu.render(f"LVL: {self.difficulty.upper()}", True, (255, 255, 255))
        self.screen.blit(diff_txt, (self.btn_diff.centerx - diff_txt.get_width()//2, self.btn_diff.centery - diff_txt.get_height()//2))

        pygame.draw.rect(self.screen, (200, 50, 50), self.btn_exit, border_radius=10)
        exit_txt = self.font_menu.render("EXIT", True, (255, 255, 255))
        self.screen.blit(exit_txt, (self.btn_exit.centerx - exit_txt.get_width()//2, self.btn_exit.centery - exit_txt.get_height()//2))

        pygame.display.flip()

    def draw(self):
        if self.state == 'MENU':
            self.draw_menu()
            return
            
        if self.background:
            self.screen.blit(self.background, (0, 0))
        else:
            self.screen.fill(BACKGROUND_COLOR)

        pygame.draw.line(self.screen, (255, 255, 255), (BOUNDARY_LINE_X, 0), (BOUNDARY_LINE_X, HEIGHT), 3)

        self.all_sprites.draw(self.screen)

        font = pygame.font.SysFont(None, 28)
        score_text = font.render(f"Score: {self.score} | Diff: {self.difficulty.upper()}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

        if self.is_game_over:
            over = pygame.font.SysFont(None, 64).render("GAME OVER", True, (255, 50, 50))
            self.screen.blit(over, (WIDTH // 2 - over.get_width() // 2, HEIGHT // 2 - over.get_height() // 2 - 40))
            result = pygame.font.SysFont(None, 48).render(f"Final Score: {self.score}", True, (255, 255, 255))
            self.screen.blit(result, (WIDTH // 2 - result.get_width() // 2, HEIGHT // 2 - result.get_height() // 2 + 30))

        ui = pygame.font.SysFont(None, 24)
        self.screen.blit(ui.render("SPACE: shoot, R: menu", True, (255, 255, 255)), (10, HEIGHT - 30))

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
    sys.exit()