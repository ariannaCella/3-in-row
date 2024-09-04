import g2d
from time import time
from random import choice

def abstract():
    raise NotImplementedError("Abstract method")

class BoardGame:
    def play_at(self, x: int, y: int): abstract()
    def flag_at(self, x: int, y: int): abstract()
    def value_at(self, x: int, y: int) -> str: abstract()
    def cols(self) -> int: abstract()
    def rows(self) -> int: abstract()
    def finished(self) -> bool: abstract()
    def message(self) -> str: abstract()


def print_game(game: BoardGame):
    for y in range(game.rows()):
        for x in range(game.cols()):
            val = game.value_at(x, y)
            print(f"{val:3}", end='')
        print()

def console_play(game: BoardGame):
    print_game(game)
    while not game.finished():
        x, y = input().split()
        game.play_at(int(x), int(y))
        print_game(game)

    print(game.message())

W, H = 40, 40
LONG_PRESS = 0.5

class BoardGameGui:
    def __init__(self, g: BoardGame):
        self._game = g
        self._downtime = 0
        self.update_buttons()

    def tick(self):
        if g2d.key_pressed("LeftButton"):
            self._downtime = time()
        elif g2d.key_released("LeftButton"):
            mouse = g2d.mouse_position()
            x, y = mouse[0] // W, mouse[1] // H
            if 0<=y<self._game.rows() and 0<=x<self._game.cols():
                if time() - self._downtime > LONG_PRESS:
                    self._game.flag_at(x, y)
                else:
                    self._game.play_at(x, y)
        elif g2d.key_pressed("a"):
            self._game.automatismi()
            
        elif g2d.key_pressed("u"):
            if self._game.unsolvable()==True:
                g2d.alert("Vicolo cieco")
            else:
                g2d.alert("Continua così")

        elif g2d.key_pressed("h"):
            self._game.suggerimenti()

        elif g2d.key_pressed("b"):
            self._game.solved()  
        self.update_buttons()


    def update_buttons(self):
        g2d.clear_canvas()
        cols, rows = self._game.cols(), self._game.rows()
        for y in range(rows):
            for x in range(cols):
                value = self._game.value_at(x, y)
                if value=="1":
                    g2d.set_color((0,0,0))
                    g2d.fill_rect((x*W, y*H, W,H))
                if value=="0":
                    g2d.set_color((255,255,255))
                    g2d.fill_rect((x*W, y*H, W,H))
                if value=="-":
                    g2d.set_color((96, 95, 99))
                    g2d.fill_rect((x*W, y*H, W,H))
        for y in range(1, rows):
            g2d.set_color((59, 58, 61))
            g2d.draw_line((0, y * H), (cols * W, y * H))
        for x in range(1, cols):
            g2d.set_color((59, 58, 61))
            g2d.draw_line((x * W, 0), (x * W, rows * H))
        g2d.update_canvas()
        if self._game.finished():
            g2d.alert(self._game.message())
            g2d.close_canvas()

def gui_play(game: BoardGame):
    g2d.init_canvas((game.cols() * W, game.rows() * H))
    ui = BoardGameGui(game)
    g2d.main_loop(ui.tick)

