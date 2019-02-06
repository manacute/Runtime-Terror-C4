import pygame, sys

'''
CSC290 Group Project
C4: Four In A Row
University of Toronto Mississauga
'''

class Move:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class GameBoard:
    def __init__(self):
        board = []
        moves = []
        
    def performMove(x, y) -> null:
        pass
        
    def doesMoveWinGame(m: Move) -> bool:
        winrar = False
        return winrar

    def ControllerTick() -> int:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            
            return 1
    
    def ViewTick() -> null:
        pygame.display.flip()    
    
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    screen.fill((255, 255, 255))
    
    filledCross = pygame.image.load("graphics/baseline_cancel_black_48dp.png")
    emptyCross = pygame.image.load("graphics/outline_cancel_black_48dp.png")        
    board = GameBoard()
    
    while True:
        if board.ControllerTick() == 0:
            pygame.quit()
            sys.exit()
        board.ViewTick()
