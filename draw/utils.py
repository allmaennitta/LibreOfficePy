class Geometry:
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def __str__(self) -> str:
        return "x: %s\n" \
               "y: %s\n" \
               "width: %s\n" \
               "height: %s\n" % (self._x, self._y, self._width, self._height)