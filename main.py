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

    def get_num(self) -> int:
        return self._player_num

    def is_empty(self) -> bool:
        return self._player_num == 0 

    def get_player(self) -> bool:
        return self._player_num


class Move:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x
	
	def get_y(self):
		return self._y

class BoardModel:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        screen.fill((255, 255, 255))

        #Initialize our board in format self._board[colum_position][row_position].
        self._board = [[], [], [], [], [], [], []]
        i = 0
        j = 0
        while (j < 7):
            while (i < 6):
                if i == 0:
                    board[j][i] = Piece() #This represents an empty place on the board.
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
    
    def perform_move(self, m: Move) -> None:
        self.board.perform_move(m)  
    
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
