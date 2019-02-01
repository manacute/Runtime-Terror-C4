import pygame, sys

'''
CSC290 Group Project
C4: Four In A Row
University of Toronto Mississauga
'''

class Move:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        

class GameBoard:
    def __init__ (self):
        board = []
    
   
    def doesMoveWinGame(m: Move) -> bool:
        winrar = False
        return winrar
    






if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    
    filledCross = pygame.image.load("graphics/baseline_cancel_black_48dp.png")
    emptyCross = pygame.image.load("graphics/outline_cancel_black_48dp.png")
    white = 255, 255, 255




    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

    
        screen.fill(white)
        pygame.display.flip()

    