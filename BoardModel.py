import pygame
from Move import Move
from Piece import Piece
from Model import Model
from Button import Button

class BoardModel(Model):
    def __init__(self):
        '''
        Creates a BoardModel object
        '''
        super(BoardModel, self).__init__()
        pygame.display.set_caption('4-in-a-row')
        pygame.mixer.init()
        self._drop = pygame.mixer.Sound(file="sound/drop.wav")
        
        # Initialize our board in format self._board[column_position][row_position].
        self._board = [[], [], [], [], [], [], []]
        self._moves = []
        self._winner = 0
        self.reset_board()

    def reset_board(self):
        '''
        Resets the BoardModel to default arrangement
        '''
        self._board = [[], [], [], [], [], [], []]
        self._moves = []
        self._winner = 0
        j = 0
        for j in range(7):
            for i in range(6):
                self._board[j].append(Piece(0)) #This represents an empty place on the board.0

    def perform_move(self, m: Move) -> None:
        '''
        Implements moves performed by player
        '''
        self._drop.play()
        self.add_move(m)
        self._board[m.get_x()][m.get_y()] = Piece(m.get_player())


    def add_move(self, m: Move) -> None:
        '''
        Adds move to BoardModel's move list
        '''
        self._moves.append(m)

    def get_board(self) -> list:
        '''
        Returns BoardModel's list representation of the board
        '''
        return(self._board)
    
    def undo_move(self) -> None:
        '''Undo the most recently stored move.'''
        m = self._moves.pop()
        self._board[m.get_x()][m.get_y()] = Piece(0)

    def draw(self, screen):
        '''
        Draws the visual display of the game board on the game window.
        The game board consists of a blue square and 42 circles arranged
        in 7 columns and 6 rows.
        '''

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

        font = pygame.font.SysFont('Arial', 40)
        self._undo_button = Button(810, 600, 80, 40, "Undo", 
            font, self.text_color, self.button_color0, 
            self.button_color1, self.button_outline, screen)
        if self._moves:
            self._undo_button.draw()
        
        if self._winner != 0:
            if self._winner == -1:
                msg = "Stalemate! Nobody wins!"
            else:
                if self._winner is 1:
                    msg = "Player 1 has won!"
                else:
                    msg = "Player 2 has won!"

            win_msg = Button(250, 250, 400, 200, msg,
                   font, self.text_color, self.button_color0,
                   self.button_color0, self.button_outline, screen)
            win_msg.draw()

    def game_over(self, winning_player):
        '''
        Assigns the winner of the game, after it has been detected that the game
        has been won
        '''
        self._winner = winning_player
        if self._winner == -1:
            pygame.mixer.music.load('sound/failure.mp3')
        else:
            pygame.mixer.music.load('sound/victory.mp3')
        pygame.mixer.music.play(0)

    def get_event(self, event, controller):
        '''
        Gets user defined event
        '''
        if event.type == pygame.QUIT:
            self.quit = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self._undo_button.mouse_over() and self._moves:
                self.undo_move()
            elif self._winner != 0:
                self.next_model = "menu"
                self.done = True
                self.reset_board()
            elif event.pos[0] >= 100 and event.pos[0] < 800:   
                controller.perform_move(event)
