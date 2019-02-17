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
    def __init__(self, num=0):
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

        # Careating the display
        screen = pygame.display.set_mode((900, 700))
        pygame.display.set_caption('4-in-a-row')

        # Colour variables
        BLUE = (0, 0, 255)
        RED = (255, 0, 0)
        WHITE = (255, 255, 255)
        YELLOW = (255, 255, 0)

        # Making the background white
        screen.fill(WHITE)

        # Initialize our board in format self._board[column_position][row_position].
        self._board = [[], [], [], [], [], [], []]
        j = 0
        while (j < 7):
            i = 0
            while (i < 6):
                self._board[j].append(Piece()) #This represents an empty place on the board.
                i += 1
            j += 1


        self._moves = []


        # Creating the blue background of the board
        pygame.draw.rect(screen,BLUE,(100,50,700,600))
        pygame.display.update()

        # Creating the circles for the tokens on the board
        # 42 equal white circles arranged in 7 columns and 6 rows
        num_of_columns = 0
        position = [150, 100]

        while(num_of_columns != 7):
            num_of_circles = 0
            position[1] = 100
            while (num_of_circles != 6):
                pygame.draw.circle(screen, WHITE, tuple(position), 40)
                pygame.display.update()
                num_of_circles += 1
                position[1] = position[1] + 100
            position[0] = position[0] + 100
            num_of_columns = num_of_columns + 1



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
        x = move.get_x
        y = move.get_y
        if ( (x > 5) or (x < 0) or (y > 6) or (y < 0) ):
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
