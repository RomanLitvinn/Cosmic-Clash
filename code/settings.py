from pygame import image

# screen
screen_width = 900
screen_height = screen_width
raw_bg = image.load("../graphics/backgrounds/blue.png")

# player
raw_player = image.load("../graphics/character/ship.png")
raw_laser = image.load("../graphics/character/lasers/laser.png")

# enemy
raw_small_enemy = image.load("../graphics/enemies/enemy_small.png")
raw_normal_enemy = image.load("../graphics/enemies/enemy_normal.png")
raw_big_enemy = image.load("../graphics/enemies/enemy_big.png")

raw_enemy_laser = image.load("../graphics/enemies/lasers/laser.png")
