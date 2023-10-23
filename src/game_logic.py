import src.config as cfg
import src.show_button as sb
import src.snake as sn
import src.fruit as fr
import src.draw as dr
import sys


class Game:
    def __init__(self):

        self.snake = sn.Snake()

        self.gover = cfg.pygame.image.load(cfg.GAME_OVER_PATH).convert_alpha()

        self.fruit = fr.Fruit()

        self.draw = dr.Draw()

        self.pause = cfg.pygame.image.load(cfg.PAUSE_PATH).convert_alpha()
        self.flag_pause = False

        self.game_font = cfg.pygame.font.Font(cfg.FONT_PATH, 25)

        self.TT = 150
        self.SCREEN_UPDATE = cfg.pygame.USEREVENT
        cfg.pygame.time.set_timer(self.SCREEN_UPDATE, self.TT)

        self.count = 0

        mas_ost = [10, 8, 6, 4, 2]
        self.ost = mas_ost[cfg.level - 1]

        self.bg = cfg.pygame.image.load(cfg.GROUND_PATH + str(cfg.carta[cfg.item]) + '.png')
        self.count_clock = 0

    def speed(self):
        if self.count % self.ost == 0:
            self.TT -= 10
            self.SCREEN_UPDATE = cfg.pygame.USEREVENT
            cfg.pygame.time.set_timer(self.SCREEN_UPDATE, self.TT)

    def add_block(self):
        self.snake.new_block = True

    def update(self):
        if not self.flag_pause:
            self.snake.move()

        self.check_fruits()

        if not 0 <= self.snake.body[0].x <= cfg.cell_number:
            self.game_over()
        if not 0 <= self.snake.body[0].y <= cfg.cell_number:
            self.game_over()
        if self.snake.body[0] in self.snake.body[1:]:
            self.game_over()

    def check_fruits(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.x = fr.random.randint(0, cfg.cell_number - 1)
            self.fruit.y = fr.random.randint(0, cfg.cell_number - 1)
            self.fruit.pos = cfg.pygame.math.Vector2(self.fruit.x, self.fruit.y)
            self.add_block()
            self.speed()
            self.count += 1
        elif cfg.black_apple and self.fruit.pos_black == self.snake.body[0]:
            self.fruit.x_black = fr.random.randint(0, cfg.cell_number - 1)
            self.fruit.y_black = fr.random.randint(0, cfg.cell_number - 1)
            self.fruit.pos_black = cfg.pygame.math.Vector2(self.fruit.x_black, self.fruit.y_black)
            self.speed()
            self.add_block()
            self.count -= 2

        if self.count % 5 != 0: cfg.clock_c = 0

        if cfg.level in [3, 4, 5] and self.count % 5 == 0 and cfg.clock_c <= 3:
            cfg.clock_ = True
        else:
            cfg.clock_ = False

        if cfg.clock_ and self.fruit.pos_clock == self.snake.body[0]:
            self.fruit.x_clock, self.fruit.y_clock = fr.random.randint(0, cfg.cell_number - 1), fr.random.randint(0, cfg.cell_number - 1)
            self.fruit.pos_clock = cfg.pygame.math.Vector2(self.fruit.x_clock, self.fruit.y_clock)
            self.TT += 5
            self.SCREEN_UPDATE = cfg.pygame.USEREVENT
            cfg.pygame.time.set_timer(self.SCREEN_UPDATE, self.TT)
            self.count_clock += 1
            cfg.clock_c += 1

    def Pause(self):
        self.flag_pause = True

    def Go(self):
        self.flag_pause = False

    def game_over(self):
        cfg.end = True
        menu_background = cfg.pygame.image.load('Graphics/game_over.png').convert_alpha()
        menu = sb.btn.Button(120, 70, (255, 255, 0), (255, 255, 10))

        while cfg.end:
            for event in cfg.pygame.event.get():
                if event.type == cfg.pygame.QUIT:
                    cfg.new_record = False
                    cfg.pygame.quit()
                    sys.exit()
            write_to_records(cfg.input_text, self.count)
            cfg.display.blit(menu_background, (0, 0))
            if cfg.new_record == True:
                sb.btn.prt.print_text("NEW RECORD!!!", 180, 500, font_size=60)
            sb.btn.prt.print_text("GAME OVER", 180, 180, font_size=100)
            sb.btn.prt.print_text("YOUR SCORE:", 180, 300, font_size=60)
            sb.btn.prt.print_text(str(self.count), 580, 300, font_size=60)
            menu.draw(340, 650, 'Back', show_menu, font_size=45)
            cfg.pygame.display.update()
            cfg.clock.tick(60)


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
            cfg.new_record = True
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
        for event in cfg.pygame.event.get():
            if event.type == cfg.pygame.QUIT:
                cfg.pygame.quit()
                sys.exit()
            if event.type == main_game.SCREEN_UPDATE and not main_game.flag_pause:
                main_game.update()
            if event.type == cfg.pygame.KEYDOWN:
                if event.key == cfg.pygame.K_UP and not main_game.flag_pause:
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = dr.Vector2(0, -1)
                if event.key == cfg.pygame.K_DOWN and not main_game.flag_pause:
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = dr.Vector2(0, 1)
                if event.key == cfg.pygame.K_LEFT and not main_game.flag_pause:
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = dr.Vector2(-1, 0)
                if event.key == cfg.pygame.K_RIGHT and not main_game.flag_pause:
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = dr.Vector2(1, 0)
                if event.key == cfg.pygame.K_SPACE:
                    if main_game.flag_pause:
                        main_game.Go()
                    else:
                        main_game.Pause()
        cfg.display.blit(main_game.bg, (0, 0))
        main_game.draw.draw(main_game.snake, main_game.fruit, main_game.game_font, main_game.count, main_game.flag_pause, main_game.pause)
        cfg.pygame.display.update()
        cfg.clock.tick(60)


def show_menu():
    menu_background, cfg.show, need_input = cfg.pygame.image.load('Graphics/menu.png'), True, True
    btn_array = [sb.btn.Button(265, 70, (13, 162, 50), (100, 200, 40)), sb.btn.Button(100, 70, (13, 162, 50), (100, 200, 40)), sb.btn.Button(140, 70, (13, 162, 50), (100, 200, 40)),
                 sb.btn.Button(280, 70, (13, 162, 50), (100, 200, 40)), sb.btn.Button(110, 70, (13, 162, 50), (100, 200, 40)), sb.btn.Button(200, 70, (13, 162, 50), (100, 200, 40))]
    while cfg.show:
        for event in cfg.pygame.event.get():
            if event.type == cfg.pygame.QUIT:
                cfg.pygame.quit()
                quit()
            if need_input and event.type == cfg.pygame.KEYDOWN:
                if event.key == cfg.pygame.K_RETURN:
                    need_input = False
                elif event.key == cfg.pygame.K_BACKSPACE:
                    cfg.input_text = cfg.input_text[:-1]
                elif len(cfg.input_text) < 14: cfg.input_text += event.unicode
        cfg.display.blit(menu_background, (0, 0))
        sb.btn.prt.print_text('SNAKE GAME', 300, 40, font_size=48)
        sb.btn.prt.print_text('USER NAME:', 500, 200, font_size=48)
        btn_array[0].draw(290 - 230, 220, 'Start game', start_game, font_size=45)
        btn_array[1].draw(370 - 230, 720, 'Exit', quit, font_size=45)
        btn_array[2].draw(345 - 230, 320, 'Thema', sb.choose_theme, font_size=45)
        btn_array[3].draw(290 - 230, 420, 'Color snake', sb.choose_color_snake, font_size=45)
        btn_array[4].draw(365 - 230, 520, 'Level', sb.choose_level, font_size=45)
        btn_array[5].draw(330 - 230, 620, 'Records', sb.throw_table, font_size=45)

        keys = cfg.pygame.key.get_pressed()
        if keys[cfg.pygame.K_TAB]: need_input = True
        sb.btn.prt.print_text(cfg.input_text, 550, 270, font_color=(255, 255, 255))
        cfg.pygame.display.update()
        cfg.clock.tick(60)