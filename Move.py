class Move:
    '''
    Move class keeps track of the location and the player of the move.
    '''
    def __init__(self, x, y, player_num):
        '''
        Creates a move object.
        '''
        self._x = x
        self._y = y
        self._player_num = player_num

    def get_x(self):
        '''
        Returns the x position of the move
        '''
        return self._x

    def get_y(self):
        '''
        Returns the y position of the move.
        '''
        return self._y

    def get_player(self):
        '''
        Returns the number of the player who made the move, either 1 or 2.
        '''
        return self._player_num
