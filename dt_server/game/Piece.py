class Piece(object):

    def __init__(self, column, row, shape, color):
        self._x = column
        self._y = row
        self._shape = shape
        self._color = color
        self.rotation = 0  # number from 0-3

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def shape(self):
        return self._shape

    @property
    def color(self):
        return self._color

    @y.setter
    def y(self, value):
        self._y = value

    @x.setter
    def x(self, value):
        self._x = value