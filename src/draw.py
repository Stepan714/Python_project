import src.config as cfg
from pygame.math import Vector2


class Draw:
    
    def draw_snake(self, snake):
        for index, block in enumerate(snake.body):
            x_pos, y_pos = int(block.x * cfg.cell_size), int(block.y * cfg.cell_size)
            block_rect = cfg.pygame.Rect(x_pos, y_pos, cfg.cell_size, cfg.cell_size)

            if index == 0:
                if snake.direction == Vector2(1, 0): cfg.display.blit(snake.head_right, block_rect)
                if snake.direction == Vector2(-1, 0): cfg.display.blit(snake.head_left, block_rect)
                if snake.direction == Vector2(0, -1): cfg.display.blit(snake.head_up, block_rect)
                if snake.direction == Vector2(0, 1): cfg.display.blit(snake.head_down, block_rect)
            elif index == len(snake.body) - 1:
                connection = snake.body[len(snake.body) - 2] - snake.body[len(snake.body) - 1]
                if connection == Vector2(0, 1): cfg.display.blit(snake.tail_up, block_rect)
                if connection == Vector2(0, -1): cfg.display.blit(snake.tail_down, block_rect)
                if connection == Vector2(1, 0): cfg.display.blit(snake.tail_left, block_rect)
                if connection == Vector2(-1, 0): cfg.display.blit(snake.tail_right, block_rect)
            else:
                previous_block, next_block = snake.body[index + 1] - block, snake.body[index - 1] - block
                if previous_block.x == next_block.x: cfg.display.blit(snake.body_vertical, block_rect)
                elif previous_block.y == next_block.y: cfg.display.blit(snake.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1: cfg.display.blit(snake.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1: cfg.display.blit(snake.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1: cfg.display.blit(snake.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1: cfg.display.blit(snake.body_br, block_rect)

    def draw_fruit(self, fruit):
        fruit_rect = cfg.pygame.Rect(int(fruit.pos.x * cfg.cell_size), int(fruit.pos.y * cfg.cell_size), cfg.cell_size, cfg.cell_size)
        cfg.display.blit(fruit.apple, fruit_rect)

        if cfg.black_apple:
            fruit_rect_black = cfg.pygame.Rect(int(fruit.pos_black.x * cfg.cell_size), int(fruit.pos_black.y * cfg.cell_size),
                                           cfg.cell_size, cfg.cell_size)
            cfg.display.blit(fruit.black_apple, fruit_rect_black)

        if cfg.clock_:
            fruit_rect_clock = cfg.pygame.Rect(int(fruit.pos_clock.x * cfg.cell_size), int(fruit.pos_clock.y * cfg.cell_size),
                                           cfg.cell_size, cfg.cell_size)
            cfg.display.blit(fruit.clock, fruit_rect_clock)

    def draw_score(self, game_font, count, fruit):
        score_surface = game_font.render(str(count), True, (56, 74, 12))
        score_rect = score_surface.get_rect(center=(cfg.cell_size, cfg.cell_size - 20))
        cfg.display.blit(score_surface, score_rect)
        apple_rect = fruit.apple.get_rect(center=(cfg.cell_size - 20, cfg.cell_size - 20))
        cfg.display.blit(fruit.apple, apple_rect)

    def draw(self, snake, fruit, game_font, count, flag_pause, pause):
        self.draw_fruit(fruit)
        self.draw_snake(snake)
        self.draw_score(game_font, count, fruit)
        if flag_pause:
            pause_rect = cfg.pygame.Rect(int(cfg.cell_number * cfg.cell_size) // 2 - 250 // 2, int(cfg.cell_number * cfg.cell_number) // 2 + 150 // 2, cfg.cell_size // 2, cfg.cell_size // 2)
            cfg.display.blit(pause, pause_rect)