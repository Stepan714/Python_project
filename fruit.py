from config import *
import config
import random

class Fruit:
    def __init__(self):
        self.apple = pygame.image.load(config.APPLE_PATH).convert_alpha()
        self.black_apple = pygame.image.load(config.B_APPLE_PATH).convert_alpha()
        self.clock = pygame.image.load(config.CLOCK_PATH).convert_alpha()

        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)

        self.x_black = random.randint(0, cell_number - 1)
        self.y_black = random.randint(0, cell_number - 1)

        self.x_clock = random.randint(0, cell_number - 1)
        self.y_clock = random.randint(0, cell_number - 1)

        self.pos = pygame.math.Vector2(self.x, self.y)
        self.pos_black = pygame.math.Vector2(self.x_black, self.y_black)
        self.pos_clock = pygame.math.Vector2(self.x_clock, self.y_clock)
