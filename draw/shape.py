import uno
from draw.utils import Geometry

class Shape:
    def __init__(self, shape_ref, text: str, geometry: Geometry, uno_style,
                 ) -> None:
        self._text = text
        self._geometry = geometry
        self._uno_style = uno_style
        self._uno_shape = self._create(shape_ref)

    @property
    def uno_shape(self):
        return self._uno_shape

    def _create(self, shape_ref):
        uno_shape = shape_ref
        uno_shape.Size = self._size(self._geometry.width,
                                    self._geometry.height)
        uno_shape.Position = self._position(self._geometry.x, self._geometry.y)
        uno_shape.String = self._text
        uno_shape.Style = self._uno_style
        return uno_shape

    def _size(self, width: int, height: int):
        size = uno.createUnoStruct("com.sun.star.awt.Size")
        size.Width = width
        size.Height = height
        return size

    def _position(self, x: int, y: int):
        position = uno.createUnoStruct("com.sun.star.awt.Point")
        position.X = x
        position.Y = y
        return position