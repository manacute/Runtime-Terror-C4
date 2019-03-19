import pygame
from Move import Move
from Piece import Piece
from Model import Model

class BoardModel(Model):
    def __init__(self):
        super(BoardModel, self).__init__()
        pygame.display.set_caption('4-in-a-row')

        # Initialize our board in format self._board[column_position][row_position].
        self._board = [[], [], [], [], [], [], []]
        j = 0
        while (j < 7):
            i = 0
            while (i < 6):
                self._board[j].append(Piece(0)) #This represents an empty place on the board.
                i += 1
            j += 1

        self._moves = []


    def perform_move(self, m: Move) -> None:
        self.add_move(m)
        self._board[m.get_x()][m.get_y()] = Piece(m.get_player())

    def add_move(self, m: Move) -> None:
        self._moves.append(m)

    def get_board(self) -> list:
        return(self._board)

    def draw(self, screen):

        # Colour variables
        BLUE = (0, 0, 255)
        RED = (255, 0, 0)
        WHITE = (255, 255, 255)
        YELLOW = (255, 255, 0)

        # Making the background white
        screen.fill(WHITE)
        # Creating the blue background of the board
        pygame.draw.rect(screen, BLUE,(100,50,700,600))

        # Creating the circles for the tokens on the board
        # 42 equal circles arranged in 7 columns and 6 rows
        position = [150, 600]
        board = self.get_board()

        for column in board:
            position[1] = 600
            for row in column:
                n = row.get_player()
                if (n is 0):
                    pygame.draw.circle(screen, WHITE, tuple(position), 40)
                elif (n is 1):
                     pygame.draw.circle(screen, YELLOW, tuple(position), 40)
                else:
                     pygame.draw.circle(screen, RED, tuple(position), 40)
                position[1] = position[1] - 100
            position[0] = position[0] + 100


    def get_event(self, event, screen, controller):
        if event.type == pygame.QUIT:
            self.quit = True
            
        elif event.type == pygame.MOUSEBUTTONDOWN and screen == "board":
            controller.perform_move(event)
