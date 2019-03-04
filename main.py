import pygame, sys
from Move import Move
from BoardModel import BoardModel
from MoveController import MoveController
from HelpModel import HelpModel
from MenuModel import MenuModel

'''
CSC290 Group Project
C4: Four In A Row
University of Toronto Mississauga
'''

if __name__ == '__main__':

    pygame.init()   
    pygame.font.init()  

    GAME_TYPE = "menu"  
    playing = False
    
    menu = MenuModel()


    while True:
        GAME_TYPE = menu.select_game_type()
        print(GAME_TYPE)
        if (GAME_TYPE == "start"):
            board = BoardModel()
            controller = MoveController(board)
            playing = True
            while playing:
                controller.controller_tick()
    
        elif (GAME_TYPE == "help"):
            help = HelpModel()
            GAME_TYPE = help.help_menu()
            help = None

        pygame.display.update()
