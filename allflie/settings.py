# settings.py
WIDTH = 800
HEIGHT = 600
FPS = 60
BACKGROUND_COLOR = (30, 30, 30)
PLAYER_SPEED = 5
PLAYER_FIRE_RATE = 300  # ms between shots
PLAYER_ZONE_WIDTH = 280
BOUNDARY_LINE_X = PLAYER_ZONE_WIDTH

# asset paths
ASSET_DIR = "assets"
PLAYER_STAND_IMAGE = "naruto1.png"
PLAYER_RUN_IMAGE = "naruto2.png"
PLAYER_SHOOT_IMAGE = "naruto3.png"
POWER_IMAGE = "power.png"
ENEMY_IMAGES = {
    'easy': "enemy1.png",   # 10 คะแนน
    'mid': "enemy2.png",    # 20 คะแนน
    'bad': "enemy3.png"     # ยิงโดนเสีย 5 คะแนน
}
BACKGROUND_IMAGE = "background.png"

