import config
from show_button import *
from snake import *
from fruit import *
from draw import *
import sys


class Game:
    def __init__(self):

        self.snake = Snake()

        self.gover = pygame.image.load(config.GAME_OVER_PATH).convert_alpha()

        self.fruit = Fruit()

        self.draw = Draw()

        self.pause = pygame.image.load(config.PAUSE_PATH).convert_alpha()
        self.flag_pause = False

        self.game_font = pygame.font.Font(config.FONT_PATH, 25)

        self.TT = 150
        self.SCREEN_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(self.SCREEN_UPDATE, self.TT)

        self.count = 0

        mas_ost = [10, 8, 6, 4, 2]
        self.ost = mas_ost[config.level - 1]

        self.bg = pygame.image.load(config.GROUND_PATH + str(config.carta[config.item]) + '.png')
        self.count_clock = 0

    def speed(self):
        if self.count % self.ost == 0:
            self.TT -= 10
            self.SCREEN_UPDATE = pygame.USEREVENT
            pygame.time.set_timer(self.SCREEN_UPDATE, self.TT)

    def add_block(self):
        self.snake.new_block = True

    def update(self):
        if not self.flag_pause:
            self.snake.move()

        self.check_fruits()

        if not 0 <= self.snake.body[0].x <= cell_number:
            self.game_over()
        if not 0 <= self.snake.body[0].y <= cell_number:
            self.game_over()
        if self.snake.body[0] in self.snake.body[1:]:
            self.game_over()

    def check_fruits(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.x = random.randint(0, cell_number - 1)
            self.fruit.y = random.randint(0, cell_number - 1)
            self.fruit.pos = pygame.math.Vector2(self.fruit.x, self.fruit.y)
            self.add_block()
            self.speed()
            self.count += 1
        elif config.black_apple and self.fruit.pos_black == self.snake.body[0]:
            self.fruit.x_black = random.randint(0, cell_number - 1)
            self.fruit.y_black = random.randint(0, cell_number - 1)
            self.fruit.pos_black = pygame.math.Vector2(self.fruit.x_black, self.fruit.y_black)
            self.speed()
            self.add_block()
            self.count -= 2

        if self.count % 5 != 0: config.clock_c = 0

        if config.level in [3, 4, 5] and self.count % 5 == 0 and config.clock_c <= 3:
            config.clock_ = True
        else:
            config.clock_ = False

        if config.clock_ and self.fruit.pos_clock == self.snake.body[0]:
            self.fruit.x_clock, self.fruit.y_clock = random.randint(0, cell_number - 1), random.randint(0, cell_number - 1)
            self.fruit.pos_clock = pygame.math.Vector2(self.fruit.x_clock, self.fruit.y_clock)
            self.TT += 5
            self.SCREEN_UPDATE = pygame.USEREVENT
            pygame.time.set_timer(self.SCREEN_UPDATE, self.TT)
            self.count_clock += 1
            config.clock_c += 1

    def Pause(self):
        self.flag_pause = True

    def Go(self):
        self.flag_pause = False

    def game_over(self):
        config.end = True
        menu_background = pygame.image.load('Graphics/game_over.png').convert_alpha()
        menu = Button(120, 70, (255, 255, 0), (255, 255, 10))

        while config.end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    config.new_record = False
                    pygame.quit()
                    sys.exit()
            write_to_records(config.input_text, self.count)
            display.blit(menu_background, (0, 0))
            if config.new_record == True:
                print_text("NEW RECORD!!!", 180, 500, font_size=60)
            print_text("GAME OVER", 180, 180, font_size=100)
            print_text("YOUR SCORE:", 180, 300, font_size=60)
            print_text(str(self.count), 580, 300, font_size=60)
            menu.draw(340, 650, 'Back', show_menu, font_size=45)
            pygame.display.update()
            clock.tick(60)


def write_to_records(name='UNKNOWN', score=0):
    dt = {}
    with open('Records/record.txt', 'r') as f:
        for line in f.readlines():
            if '__' in line:
                boof = line.split('__')
                dt[boof[0]] = int(boof[1])

    if name in dt.keys():
        if dt[name] < score:
            print('YES')
            config.new_record = True
            dt[name] = score
    else:
        dt[name] = score

    dt = sorted(dt.items(), key=lambda it: it[1], reverse=True)
   # print(dt)
    with open('Records/record.txt', 'w') as f:
        for tup in dt:
            if '__' in tup[0]:
                f.write(tup[0] + str(tup[1]) + '\n')
            else:
                f.write(tup[0] + '__' + str(tup[1]) + '\n')


def start_game():
    main_game = Game()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == main_game.SCREEN_UPDATE and not main_game.flag_pause:
                main_game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and not main_game.flag_pause:
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN and not main_game.flag_pause:
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_LEFT and not main_game.flag_pause:
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_RIGHT and not main_game.flag_pause:
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1, 0)
                if event.key == pygame.K_SPACE:
                    if main_game.flag_pause:
                        main_game.Go()
                    else:
                        main_game.Pause()
        display.blit(main_game.bg, (0, 0))
        main_game.draw.draw(main_game.snake, main_game.fruit, main_game.game_font, main_game.count, main_game.flag_pause, main_game.pause)
        pygame.display.update()
        clock.tick(60)


def show_menu():
    menu_background, config.show, need_input = pygame.image.load('Graphics/menu.png'), True, True
    btn_array = [Button(265, 70, (13, 162, 50), (100, 200, 40)), Button(100, 70, (13, 162, 50), (100, 200, 40)), Button(140, 70, (13, 162, 50), (100, 200, 40)),
                 Button(280, 70, (13, 162, 50), (100, 200, 40)), Button(110, 70, (13, 162, 50), (100, 200, 40)), Button(200, 70, (13, 162, 50), (100, 200, 40))]
    while config.show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if need_input and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    need_input = False
                elif event.key == pygame.K_BACKSPACE:
                    config.input_text = config.input_text[:-1]
                elif len(config.input_text) < 14: config.input_text += event.unicode
        display.blit(menu_background, (0, 0))
        print_text('SNAKE GAME', 300, 40, font_size=48)
        print_text('USER NAME:', 500, 200, font_size=48)
        btn_array[0].draw(290 - 230, 220, 'Start game', start_game, font_size=45)
        btn_array[1].draw(370 - 230, 720, 'Exit', quit, font_size=45)
        btn_array[2].draw(345 - 230, 320, 'Thema', choose_theme, font_size=45)
        btn_array[3].draw(290 - 230, 420, 'Color snake', choose_color_snake, font_size=45)
        btn_array[4].draw(365 - 230, 520, 'Level', choose_level, font_size=45)
        btn_array[5].draw(330 - 230, 620, 'Records', throw_table, font_size=45)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]: need_input = True
        print_text(config.input_text, 550, 270, font_color=(255, 255, 255))
        pygame.display.update()
        clock.tick(60)