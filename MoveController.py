import pygame, sys
from Move import Move
from BoardModel import BoardModel


class MoveController:
    def __init__(self, model: BoardModel):
        self._model = model

    def perform_move(self, x: int) -> None:
        self._model.perform_move(m)

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
        if (self._model[move.get_y-1][5] == 0):
            return True

        # Otherwise return False
        return False

    def move_wins_game(self, m: Move) -> bool:
        '''
        Pre: m is a move that has been made on the BoardModel
        Post: Return True iff there are four tokens in a row of the same type in the BoardModel
        '''

        x = m.get_x()
        y = m.get_y()
        player_num = m.get_player()

        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        reverse = [1, -1]

        for axes in directions:
            tokens = 1
            for magnitude in reverse:
                displacement = magnitude
                while abs(displacement) <= 3:
                    check_x = displacement * axes[0] + x
                    check_y = displacement * axes[1] + y
                    if ((check_x <= 6) and (check_x >= 0) and (check_y <= 5) and (check_y >= 0)):
                        if self._model.get_board()[check_x][check_y].get_player() == player_num:
                            tokens += 1
                        else:
                            displacement = 3
                        if tokens == 4:
                            return True
                    displacement = (abs(i) + 1) * magnitude
        return False

    def controller_tick(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
