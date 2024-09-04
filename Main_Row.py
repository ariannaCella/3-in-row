import g2d
from time import time
from random import choice
from BoardGame import BoardGame, abstract, print_game, console_play, BoardGameGui, gui_play
from RowGame import three_Row

def main():
    n = int(input("cols/rows? [6-8-10-12-14]: "))
    level = int(input("Level? (0=easy, 1=medium): "))
    game = three_Row(n,n,level)
    gui_play(game)
    console_play(game)
    
    
main()
