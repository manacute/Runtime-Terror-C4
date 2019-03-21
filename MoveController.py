import pygame, sys
from Move import Move
from BoardModel import BoardModel


class MoveController:
    def __init__(self, model: BoardModel):
        '''
        Creates a move controller object.
        '''
        self._model = model
        self._current_player = 1
        # Prints initial message for player 1
        print("Current Move: Player " + (str) (self.get_current_player()))

    def get_current_player(self):
        return self._current_player

    def get_next_player(self) -> int:
        '''Change current player then return player number.'''
        if self._current_player == 1:
            self._current_player = 2
            return 2
        elif self._current_player == 2:
            self._current_player = 1
            return 1

    def perform_move(self, event) -> None:
        '''
        Perform move iff the move is valid (i.e. in a
        non-full column, not outside of the board).
        Afterwards, check if a player has won, or if
        the board is filled up. Else, switch players.
        '''
        x_position = event.pos[0]
        column_index = (int) ((x_position // 100) - 1)
        row_index = self.get_row_index(column_index)
        possible_move = Move(column_index, row_index, self.get_current_player())
        if self.move_is_valid(possible_move):
            self._model.perform_move(possible_move)
            if self.move_wins_game(possible_move):
                print("Player " + str(self.get_current_player()) + " wins!")
                self._model.game_over(self.get_current_player())
            elif self.board_is_full():
                print("Neither player wins!")
                self._model.game_over(-1)
            else:
                print("Current Move: Player " + (str) (self.get_next_player()))



    def move_is_valid(self, move: Move) -> bool:
        '''
        This function takes in a move object and then checks if it is valid.
        If it is valid, the function returns True and False otherwise.
        Pre: move is a valid move object and self is a valid board.
        Post: bool
        '''
        return move.get_y() != None and move.get_x() >= 0 and move.get_x() <= 6

    def move_wins_game(self, m: Move) -> bool:
        '''
        Return True iff there are four tokens in
        a row of the same type in the BoardModel
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
                    displacement = (abs(displacement) + 1) * magnitude
        return False

    def board_is_full(self) -> bool:
        '''Return True iff the board is filled with player tokens.'''
        for j in range(7):
            for i in range(6):
                  if self._model.get_board()[j][i].get_player() == 0:
                      return False
        return True

    def get_row_index(self, column_index):
        '''Return index of highest empty slot for a given column.'''
        selected_column = self._model.get_board()[column_index]

        i = 0
        while i < len(selected_column):
            if selected_column[i].is_empty():
                return i
            i += 1

        # In case that there is no empty slot, we return "None" which we use as
        # a indication later in our check if the move is invalid.
        return None
