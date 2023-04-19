from config import *
import config
from pygame.math import Vector2


class Draw:
    
    def draw_snake(self, snake):
        for index, block in enumerate(snake.body):
            x_pos, y_pos = int(block.x * cell_size), int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                if snake.direction == Vector2(1, 0): display.blit(snake.head_right, block_rect)
                if snake.direction == Vector2(-1, 0): display.blit(snake.head_left, block_rect)
                if snake.direction == Vector2(0, -1): display.blit(snake.head_up, block_rect)
                if snake.direction == Vector2(0, 1): display.blit(snake.head_down, block_rect)
            elif index == len(snake.body) - 1:
                connection = snake.body[len(snake.body) - 2] - snake.body[len(snake.body) - 1]
                if connection == Vector2(0, 1): display.blit(snake.tail_up, block_rect)
                if connection == Vector2(0, -1): display.blit(snake.tail_down, block_rect)
                if connection == Vector2(1, 0): display.blit(snake.tail_left, block_rect)
                if connection == Vector2(-1, 0): display.blit(snake.tail_right, block_rect)
            else:
                previous_block, next_block = snake.body[index + 1] - block, snake.body[index - 1] - block
                if previous_block.x == next_block.x: display.blit(snake.body_vertical, block_rect)
                elif previous_block.y == next_block.y: display.blit(snake.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1: display.blit(snake.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1: display.blit(snake.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1: display.blit(snake.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1: display.blit(snake.body_br, block_rect)

    def draw_fruit(self, fruit):
        fruit_rect = pygame.Rect(int(fruit.pos.x * cell_size), int(fruit.pos.y * cell_size), cell_size, cell_size)
        display.blit(fruit.apple, fruit_rect)

        if config.black_apple:
            fruit_rect_black = pygame.Rect(int(fruit.pos_black.x * cell_size), int(fruit.pos_black.y * cell_size),
                                           cell_size, cell_size)
            display.blit(fruit.black_apple, fruit_rect_black)

        if config.clock_:
            fruit_rect_clock = pygame.Rect(int(fruit.pos_clock.x * cell_size), int(fruit.pos_clock.y * cell_size),
                                           cell_size, cell_size)
            display.blit(fruit.clock, fruit_rect_clock)

    def draw_score(self, game_font, count, fruit):
        score_surface = game_font.render(str(count), True, (56, 74, 12))
        score_rect = score_surface.get_rect(center=(cell_size, cell_size - 20))
        display.blit(score_surface, score_rect)
        apple_rect = fruit.apple.get_rect(center=(cell_size - 20, cell_size - 20))
        display.blit(fruit.apple, apple_rect)

    def draw(self, snake, fruit, game_font, count, flag_pause, pause):
        self.draw_fruit(fruit)
        self.draw_snake(snake)
        self.draw_score(game_font, count, fruit)
        if flag_pause:
            pause_rect = pygame.Rect(int(cell_number * cell_size) // 2 - 250 // 2, int(cell_number * cell_number) // 2 + 150 // 2, cell_size // 2, cell_size // 2)
            display.blit(pause, pause_rect)