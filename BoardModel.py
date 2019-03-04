import pygame
from Move import Move
from Piece import Piece

class BoardModel:
    def __init__(self):

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

    def get_board(self) -> list:
        return(self._board)

    def update(self) -> None:
        pass