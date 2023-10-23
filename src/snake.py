import src.config as cfg
from pygame.math import Vector2

class Snake:
    def __init__(self):
        # create snake
        self.body = [Vector2(6, 10), Vector2(5, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

        self.head_up = cfg.pygame.image.load(cfg.SNAKE_PATH_head_up + str(cfg.regular_word) + '.png').convert_alpha()
        self.head_down = cfg.pygame.image.load(cfg.SNAKE_PATH_head_down + str(cfg.regular_word) + '.png').convert_alpha()
        self.head_right = cfg.pygame.image.load(cfg.SNAKE_PATH_head_right + str(cfg.regular_word) + '.png').convert_alpha()
        self.head_left = cfg.pygame.image.load(cfg.SNAKE_PATH_head_left + str(cfg.regular_word) + '.png').convert_alpha()

        self.tail_up = cfg.pygame.image.load(cfg.SNAKE_PATH_tail_up + str(cfg.regular_word) + '.png').convert_alpha()
        self.tail_down = cfg.pygame.image.load(cfg.SNAKE_PATH_tail_down + str(cfg.regular_word) + '.png').convert_alpha()
        self.tail_right = cfg.pygame.image.load(cfg.SNAKE_PATH_tail_right + str(cfg.regular_word) + '.png').convert_alpha()
        self.tail_left = cfg.pygame.image.load(cfg.SNAKE_PATH_tail_left + str(cfg.regular_word) + '.png').convert_alpha()

        self.body_vertical = cfg.pygame.image.load(cfg.SNAKE_PATH_body_vertical + str(cfg.regular_word) + '.png').convert_alpha()
        self.body_horizontal = cfg.pygame.image.load(cfg.SNAKE_PATH_body_horizontal + str(cfg.regular_word) + '.png').convert_alpha()

        self.body_tr = cfg.pygame.image.load(cfg.SNAKE_PATH_body_tr + str(cfg.regular_word) + '.png').convert_alpha()
        self.body_tl = cfg.pygame.image.load(cfg.SNAKE_PATH_body_tl + str(cfg.regular_word) + '.png').convert_alpha()
        self.body_br = cfg.pygame.image.load(cfg.SNAKE_PATH_body_br + str(cfg.regular_word) + '.png').convert_alpha()
        self.body_bl = cfg.pygame.image.load(cfg.SNAKE_PATH_body_bl + str(cfg.regular_word) + '.png').convert_alpha()

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
