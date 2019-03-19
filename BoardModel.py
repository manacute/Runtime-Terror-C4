import pygame
from Move import Move
from Piece import Piece
from Model import Model
from Button import Button

class BoardModel(Model):
    def __init__(self):
        super(BoardModel, self).__init__()
        pygame.display.set_caption('4-in-a-row')
        # Initialize our board in format self._board[column_position][row_position].  
        self._board = [[], [], [], [], [], [], []]
        self._moves = []
        self._winner = 0
        j = 0
        while (j < 7):
            i = 0
            while (i < 6):
                self._board[j].append(Piece(0)) #This represents an empty place on the board.
                i += 1
            j += 1
      #  self.reset_board
        
  #  def reset_board(self):


        
    def perform_move(self, m: Move) -> None:
        self.add_move(m)
        self._board[m.get_x()][m.get_y()] = Piece(m.get_player())

    def add_move(self, m: Move) -> None:
        self._moves.append(m)

    def get_board(self) -> list:
        return(self._board)

    def draw(self, screen):

        # Making the background white
        screen.fill(pygame.Color("white"))
        # Creating the blue background of the board
        pygame.draw.rect(screen, pygame.Color("blue"),(100,50,700,600))

        # Creating the circles for the tokens on the board
        # 42 equal circles arranged in 7 columns and 6 rows
        position = [150, 600]
        board = self.get_board()

        for column in board:
            position[1] = 600
            for row in column:
                n = row.get_player()
                if (n is 0):
                    pygame.draw.circle(screen, pygame.Color("white"), tuple(position), 40)
                elif (n is 1):
                     pygame.draw.circle(screen, pygame.Color("yellow"), tuple(position), 40)
                else:
                     pygame.draw.circle(screen, pygame.Color("Red"), tuple(position), 40)
                position[1] = position[1] - 100
            position[0] = position[0] + 100

        if self._winner != 0:
            font = pygame.font.SysFont('Arial', 40)
            button = Button(250, 250, 400, 200, "Player " + str(self._winner) + " has won!", 
                   font, self.text_color, self.button_color0, 
                   self.button_color0, self.button_outline, screen) 
            button.draw()

    def game_over(self, winning_player):
        self._winner = winning_player

    def get_event(self, event, controller):
        if event.type == pygame.QUIT:
            self.quit = True
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self._winner != 0:
                self.next_model = "menu"
                self.done = True
         #       self.reset_board()
            else:
                controller.perform_move(event)
            