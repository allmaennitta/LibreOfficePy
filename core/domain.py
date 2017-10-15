import uno

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

class Page:
    """Dummy Class for Typing"""
    pass


class Shape:
    def __init__(self, shape) -> None:
        self._shape = shape
        self._Style = None

    def applySize(self, width: int, height: int):
        size = uno.createUnoStruct("com.sun.star.awt.Size")
        size.Width = width
        size.Height = height
        self._shape.Size = size

    def applyPosition(self, x: int, y: int):
        position = uno.createUnoStruct("com.sun.star.awt.Point")
        position.X = x
        position.Y = y
        self._shape.Position = position

    def applyText(self, text: str):
        self._shape.String = text

    def unwrap(self):
        return self._shape

    @property
    def Style(self):
        return self._Style

    @Style.setter
    def Style(self, value):
        self._shape.Style = value