import uno
import yaml
from math import ceil
from draw.utils import Geometry
from draw.page import Page
from draw.shape import Shape
from typing import List

C = yaml.load("""
box:
    title:
        # 1000 is equivalent to 1.00 cm
        base_height: 800
        characters_to_linebreak: 15
""")


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
        self._page = Page(uno_page, index)
        return self._page

    def create_box(self, geometry: Geometry, content: str,
                   style: str = "Box_Content"):
        box_content = Shape(self._uno_shape_ref(), content,
                            Geometry(geometry.x, geometry.y,
                                     geometry.width,
                                     geometry.height),
                            self._uno_style_ref(style))

    def create_title(self, geometry: Geometry, title: str,
                     style: str = "Box_Title"):
        title_height = calc_title_height(title)
        title = Shape(self._uno_shape_ref(), title, geometry,
                      self._uno_style_ref(style))

    def create_titled_box(self, geometry: Geometry, title: str, content: str,
                          style_title="Box_Title", style_box="Box_Content"):
        title_height = calc_title_height(title)

        if geometry.height < title_height * 2:
            geometry.height = title_height * 2

        box_title = Shape(self._uno_shape_ref(), title,
                          Geometry(geometry.x, geometry.y, geometry.width,
                                   title_height),
                          self._uno_style_ref(style_title))

        box_content = Shape(self._uno_shape_ref(), content,
                            Geometry(geometry.x, geometry.y + title_height,
                                     geometry.width,
                                     geometry.height - title_height),
                            self._uno_style_ref(style_box))

        self.group(box_title, box_content)

    def create_double_title(self, geometry: Geometry, title1: str, title2: str,
                          style_title1="o_Title_fat", style_title2="o_Title"):
        # title_height = calc_title_height(title)

        # if geometry.height < title_height * 2:
        #     geometry.height = title_height * 2

        box_title1 = Shape(self._uno_shape_ref(), title1,
                          Geometry(geometry.x, geometry.y, geometry.width,
                                   geometry.height/2),
                          self._uno_style_ref(style_title1))

        box_title2 = Shape(self._uno_shape_ref(), title2,
                            Geometry(geometry.x, geometry.y + geometry.height/2,
                                     geometry.width,
                                     geometry.height / 2),
                            self._uno_style_ref(style_title2))

        self.group(box_title1, box_title2)


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


def calc_title_height(title):
    wordlength = len(title)
    factor = ceil(
        wordlength / C["box"]["title"]["characters_to_linebreak"])
    return factor * C["box"]["title"]["base_height"]
