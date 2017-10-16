import uno
from draw.utils import Geometry
from draw.page import Page
from draw.shape import Shape
from typing import List


class Document:
    def __init__(self):
        self._uno_document = self._create()
        self._page = self.go_to_page(0)
        self._styles = self._uno_document.StyleFamilies.getByName("graphics")

    @property
    def uno_document(self):
        return self._uno_document

    def go_to_page(self, index: int = 0) -> Page:
        uno_page = self.uno_document.DrawPages[index]
        return Page(uno_page, index)

    def create_box(self, geometry: Geometry, title: str, content: str):
        TITLE_HEIGHT = 1000  # equivalent to 1.00 cm
        if geometry.height < TITLE_HEIGHT * 2:
            geometry.height = TITLE_HEIGHT * 2

        box_title = Shape(self._uno_shape_ref(), title,
                          Geometry(geometry.x, geometry.y, geometry.width,
                                   TITLE_HEIGHT),
                          self._uno_style_ref("Box_Title"))

        box_content = Shape(self._uno_shape_ref(), content,
                            Geometry(geometry.x, geometry.y, geometry.width,
                                     geometry.height - TITLE_HEIGHT),
                            self._uno_style_ref("Box_Content"))

        self.group(box_title, box_content)

    def group(self, *shapes: List[Shape]):
        uno_group = self._uno_document.createInstance(
            "com.sun.star.drawing.GroupShape")
        self._page.uno_page.add(uno_group)
        for shape in shapes:
            uno_group.add(shape.uno_shape)

    def _uno_shape_ref(self):
        shape_ref = self._uno_document.createInstance(
            "com.sun.star.drawing.TextShape")
        self._page.uno_page.add(shape_ref)
        return shape_ref

    def _uno_style_ref(self, name: str):
        return self._styles.getByName(name)

    def _create(self):
        localContext = uno.getComponentContext()
        resolver = localContext.ServiceManager.createInstanceWithContext(
            "com.sun.star.bridge.UnoUrlResolver", localContext)
        context = resolver.resolve(
            "uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
        desktop = context.ServiceManager.createInstanceWithContext(
            "com.sun.star.frame.Desktop", context)
        return desktop.getCurrentComponent()
