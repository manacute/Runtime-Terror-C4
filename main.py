import pygame, sys

'''
CSC290 Group Project
C4: Four In A Row
University of Toronto Mississauga
'''

class Piece:
    '''Piece class to keep track of of each place on the board. On default the
        player number is set to 0, which represents an unclaimed spot (this allows us 
        to check if a current position of the board is empty safely).	
    '''
    def __init__(self, num=0: int):
        self._player_num = num

    def is_empty(self) -> bool:
        return self._player_num == 0 

    def get_player(self) -> int:
        return self._player_num


class Move:
    def __init__(self, x, y, player_num):
        self._x = x
        self._y = y
        self._player_num = player_num

    def get_x(self):
        return self._x
	
    def get_y(self):
        return self._y

    def get_player(self):
        return self._player_num

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
        #Initialize our board in format self._board[colum_position][row_position].
        self._board = [[], [], [], [], [], [], []]
        j = 0
        while (j < 7):
            i = 0
            while (i < 6):
                self._board[j].append(Piece()) #This represents an empty place on the board.
                i += 1
            j += 1
			
			
        self._moves = []
            
    def view_tick(self) -> None:
        pygame.display.flip()


    def perform_move(self, m: Move) -> None:
        self.add_move(m)
        self._board[m.get_x()][m.get_y()] = Piece(m.get_player())
        self.update()
	
    def add_move(self, m: Move) -> None:
        self._moves.add(m)

    def update(self) -> None:
        pass
			    


class MoveController:
    def __init__(self, board: BoardModel):
        self.board = board

    def perform_move(self, x: int) -> None:
        self.board.perform_move(m)

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
