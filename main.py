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

    def get_x(self):
        '''Returns the x value of the move'''
        return self.x

    def get_y(self):
        '''Returns the y value of the move'''
        return self.y

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

    def move_is_valid(self, move: Move) -> bool:
        '''
        This function takes in a move object and then checks if it is valid.
        If it is valid, the function returns True and False otherwise.
        Pre: move is a valid move object and self is a valid board.
        Post: bool
        '''

        # To check if the move is valid we have to check if that space is empty
        # The board is stored as a nested list with 7 sublists each 6 ints large
        # An empty location is represented by 0
        # Each sublist is a column
        # A board has 7 columns (y) and 6 rows (x)

        # First check that the coordinates are valid
        if ( (move.get_x > 6) or (move.get_x < 0) or (move.get_x > 7) or (move.get_x < 0) ):
            return False

        # Check that location is empty - the column should have space
        if (self.board[move.get_y-1][5] == 0):
            return True

        # Otherwise return False
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
