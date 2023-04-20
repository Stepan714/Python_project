import src.button as btn
import src.config as cfg

def Back():
    cfg.end = False
    cfg.new_record = False

def choose_col_sn(sub):
    cfg.regular_word = sub

def choose_th(sub):
    cfg.item = sub

def choose_lev(sub):
    cfg.level = sub[0]
    cfg.black_apple = sub[1]
    cfg.clock_ = sub[2]

def choose_theme():
    menu_background = cfg.pygame.image.load('Graphics/menu_2.png')
    btn_theme = [btn.Button(250, 70, (50, 50, 50), (100, 200, 40)) for i in range(3)]
    back = btn.Button(250, 70, (50, 50, 50), (100, 200, 40))
    cfg.end = True

    while cfg.end:
        for event in cfg.pygame.event.get():
            if event.type == cfg.pygame.QUIT:
                cfg.end = False
        cfg.display.blit(menu_background, (0, 0))
        btn_theme[0].draw(290, 250, 'Theme 1', choose_th, font_size=45, sub=1)
        btn_theme[1].draw(290, 350, 'Theme 2', choose_th, font_size=45, sub=2)
        btn_theme[2].draw(290, 450, 'Theme 3', choose_th, font_size=45, sub=3)
        back.draw(290, 650, 'Back', Back, font_size=45)
        cfg.pygame.display.update()
        cfg.clock.tick(60)

def choose_color_snake():
    menu_background = cfg.pygame.image.load('Graphics/menu_2.png')
    btn_color = [btn.Button(250, 70, (50, 50, 50), (100, 200, 40)) for i in range(3)]
    back = btn.Button(250, 70, (50, 50, 50), (100, 200, 40))
    cfg.end = True

    while cfg.end:
        for event in cfg.pygame.event.get():
            if event.type == cfg.pygame.QUIT:
                cfg.end = False
        cfg.display.blit(menu_background, (0, 0))
        btn_color[0].draw(290, 250, 'Blue', choose_col_sn, font_size=45, sub=1)
        btn_color[1].draw(290, 350, 'Purple', choose_col_sn, font_size=45, sub=2)
        btn_color[2].draw(290, 450, 'Orange', choose_col_sn, font_size=45, sub=3)
        back.draw(290, 650, 'Back', Back, font_size=45)
        cfg.pygame.display.update()
        cfg.clock.tick(60)

def choose_level():
    menu_background = cfg.pygame.image.load('Graphics/menu_2.png')
    btn_level = [btn.Button(250, 70, (50, 50, 50), (100, 200, 40)) for i in range(5)]
    back = btn.Button(250, 70, (50, 50, 50), (100, 200, 40))

    cfg.end = True

    while cfg.end:
        for event in cfg.pygame.event.get():
            if event.type == cfg.pygame.QUIT:
                cfg.end = False
        cfg.display.blit(menu_background, (0, 0))
        btn_level[0].draw(290, 150, 'Level 1', choose_lev, font_size=45, sub=[1, False, False])
        btn_level[1].draw(290, 250, 'Level 2', choose_lev, font_size=45, sub=[2, False, False])
        btn_level[2].draw(290, 350, 'Level 3', choose_lev, font_size=45, sub=[3, False, True])
        btn_level[3].draw(290, 450, 'Level 4', choose_lev, font_size=45, sub=[4, True, True])
        btn_level[4].draw(290, 550, 'Level 5', choose_lev, font_size=45, sub=[5, True, True])
        back.draw(290, 650, 'Back', Back, font_size=45)
        cfg.pygame.display.update()
        cfg.clock.tick(60)

def throw_table():
    menu_background = cfg.pygame.image.load('Graphics/top_result.png')
    back, mas = btn.Button(250, 70, (255, 255, 50), (255, 255, 40)), []

    with open('Records/record.txt', 'r') as f:
        for line in f.readlines():
            mas.append(line.split('__'))

    mas = mas[:8]
    cfg.end = True

    while cfg.end:
        for event in cfg.pygame.event.get():
            if event.type == cfg.pygame.QUIT:
                cfg.end = False
        cfg.display.blit(menu_background, (0, 0))
        i = 0
        btn.prt.print_text('TOP RESULTS', 265, 50, font_size=50)
        btn.prt.print_text('NAME', 300, 150, font_size=30)
        btn.prt.print_text('SCORE', 480, 150, font_size=30)
        for j in range(len(mas)):
            btn.prt.print_text(str(j + 1) + '.', 260, 200 + i, font_size=30)
            btn.prt.print_text(mas[j][0], 300, 200 + i, font_size=30)
            btn.prt.print_text(mas[j][1][:-1], 500, 200 + i, font_size=30)
            i += 50
        back.draw(290, 650, 'Back', Back, font_size=45)
        cfg.pygame.display.update()
        cfg.clock.tick(60)