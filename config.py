import pygame

pygame.init()

cell_size = 40
cell_number = 20
carta = {1: 'one', 2: 'two', 3: 'three'}
input_text = ''

display = pygame.display.set_mode((cell_number * cell_size, cell_size * cell_number))
clock = pygame.time.Clock()

item = 1
regular_word = 1
level = 1

show = True
end = True
new_record = False
black_apple = False
clock_ = False

clock_c = 0


# SNAKE PATH
SNAKE_PATH_head_up = f'Graphics/head_up'
SNAKE_PATH_head_down = f'Graphics/head_down'
SNAKE_PATH_head_right = f'Graphics/head_right'
SNAKE_PATH_head_left = f'Graphics/head_left'

SNAKE_PATH_tail_up = f'Graphics/tail_up'
SNAKE_PATH_tail_down = f'Graphics/tail_down'
SNAKE_PATH_tail_right = f'Graphics/tail_right'
SNAKE_PATH_tail_left = f'Graphics/tail_left'

SNAKE_PATH_body_vertical = f'Graphics/body_vertical'
SNAKE_PATH_body_horizontal = f'Graphics/body_horizontal'

SNAKE_PATH_body_tr = f'Graphics/body_tr'
SNAKE_PATH_body_tl = f'Graphics/body_tl'
SNAKE_PATH_body_br = f'Graphics/body_br'
SNAKE_PATH_body_bl = f'Graphics/body_bl'


# FRUIT PATH
APPLE_PATH = 'Graphics/apple.png'
B_APPLE_PATH = 'Graphics/black_apple.png'
CLOCK_PATH = 'Graphics/clock.png'

# OTHER PATH
GAME_OVER_PATH = f'Graphics/game_over.png'
PAUSE_PATH = 'Graphics/pause_new.png'
FONT_PATH = 'DaFront/Rastano.ttf'
GROUND_PATH = f'Graphics/color_'