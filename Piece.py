class Piece:
    '''Piece class to keep track of of each place on the board. On default the
        player number is set to 0, which represents an unclaimed spot (this allows us
        to check if a current position of the board is empty safely).
    '''
    def __init__(self, num=0):
        '''
        Creates a Piece object
        '''
        self._player_num = num

    def is_empty(self) -> bool:
        '''
        Returns True if place on board is empty and False otherwise.
        '''
        return self._player_num == 0

    def get_player(self) -> int:
        '''
        Returns number of player who placed a piece in that place on the board.
        If place is empty, returns 0. Otherwise it returns player number.
        '''
        return self._player_num
