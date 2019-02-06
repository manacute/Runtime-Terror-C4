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

class BoardModel:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        screen.fill((255, 255, 255))
        board = []
        moves = []
            
    def view_tick(self) -> None:
        pygame.display.flip()    

class MoveController:
    def __init__(self, board: BoardModel):
        self.board = board
    
    def perform_move(self, x: int) -> None:
        pass  
    
    def move_is_valid(self, m: Move) -> bool:
        
        return False

    def move_wins_game(self, m: Move) -> bool:
        count = 0
        return False

    def controller_tick(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            


    
if __name__ == '__main__':
    
    board = BoardModel()
    controller = MoveController(board)
    
    filledCross = pygame.image.load("graphics/baseline_cancel_black_48dp.png")
    emptyCross = pygame.image.load("graphics/outline_cancel_black_48dp.png")        

    
    while True:
        controller.controller_tick()
