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