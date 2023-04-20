import src.config as cfg
import random

class Fruit:
    def __init__(self):
        self.apple = cfg.pygame.image.load(cfg.APPLE_PATH).convert_alpha()
        self.black_apple = cfg.pygame.image.load(cfg.B_APPLE_PATH).convert_alpha()
        self.clock = cfg.pygame.image.load(cfg.CLOCK_PATH).convert_alpha()

        self.x = random.randint(0, cfg.cell_number - 1)
        self.y = random.randint(0, cfg.cell_number - 1)

        self.x_black = random.randint(0, cfg.cell_number - 1)
        self.y_black = random.randint(0, cfg.cell_number - 1)

        self.x_clock = random.randint(0, cfg.cell_number - 1)
        self.y_clock = random.randint(0, cfg.cell_number - 1)

        self.pos = cfg.pygame.math.Vector2(self.x, self.y)
        self.pos_black = cfg.pygame.math.Vector2(self.x_black, self.y_black)
        self.pos_clock = cfg.pygame.math.Vector2(self.x_clock, self.y_clock)
