from config import *
import config
from pygame.math import Vector2

class Snake:
    def __init__(self):
        # create snake
        self.body = [Vector2(6, 10), Vector2(5, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

        self.head_up = pygame.image.load(config.SNAKE_PATH_head_up + str(config.regular_word) + '.png').convert_alpha()
        self.head_down = pygame.image.load(config.SNAKE_PATH_head_down + str(config.regular_word) + '.png').convert_alpha()
        self.head_right = pygame.image.load(config.SNAKE_PATH_head_right + str(config.regular_word) + '.png').convert_alpha()
        self.head_left = pygame.image.load(config.SNAKE_PATH_head_left + str(config.regular_word) + '.png').convert_alpha()

        self.tail_up = pygame.image.load(config.SNAKE_PATH_tail_up + str(config.regular_word) + '.png').convert_alpha()
        self.tail_down = pygame.image.load(config.SNAKE_PATH_tail_down + str(config.regular_word) + '.png').convert_alpha()
        self.tail_right = pygame.image.load(config.SNAKE_PATH_tail_right + str(config.regular_word) + '.png').convert_alpha()
        self.tail_left = pygame.image.load(config.SNAKE_PATH_tail_left + str(config.regular_word) + '.png').convert_alpha()

        self.body_vertical = pygame.image.load(config.SNAKE_PATH_body_vertical + str(config.regular_word) + '.png').convert_alpha()
        self.body_horizontal = pygame.image.load(config.SNAKE_PATH_body_horizontal + str(config.regular_word) + '.png').convert_alpha()

        self.body_tr = pygame.image.load(config.SNAKE_PATH_body_tr + str(config.regular_word) + '.png').convert_alpha()
        self.body_tl = pygame.image.load(config.SNAKE_PATH_body_tl + str(config.regular_word) + '.png').convert_alpha()
        self.body_br = pygame.image.load(config.SNAKE_PATH_body_br + str(config.regular_word) + '.png').convert_alpha()
        self.body_bl = pygame.image.load(config.SNAKE_PATH_body_bl + str(config.regular_word) + '.png').convert_alpha()

    def move(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
