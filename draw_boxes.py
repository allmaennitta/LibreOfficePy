import uno
import typing
from core.domain import Geometry, Page, Shape


class Document:
    def __init__(self):
        self._doc = self._get_document()
        self._page = self.go_to_page(0)
        self._styles = self._doc.StyleFamilies.getByName("graphics")


    def applyStyle(self, shape: Shape, name: str):
        shape.Style = self._styles.getByName(name)

    def create_box(self, geometry: Geometry, title: str, content: str,
                   page: Page = None):
        
        TITLE_HEIGHT = 1000
        if geometry.height < TITLE_HEIGHT * 2:
            geometry.height = TITLE_HEIGHT * 2

        if page is None:
            page = self._page

        box_title = self._create_shape()
        box_title.applySize(geometry.width, TITLE_HEIGHT)
        box_title.applyPosition(geometry.x, geometry.y)
        self.applyStyle(box_title, "Box_Title")
        box_title.applyText(title)

        box_content = self._create_shape()
        box_content.applySize(geometry.width, geometry.height - TITLE_HEIGHT)
        box_content.applyPosition(geometry.x, geometry.y+ TITLE_HEIGHT)
        self.applyStyle(box_content, "Box_Content")
        box_content.applyText(content)

        self._group(box_title,box_content)


    def go_to_page(self, no: int = 0) -> Page:
        self._page = self._doc.DrawPages[no]
        return typing.cast(Page, self._page)

    def _group(self, *shapes):
        group = self._doc.createInstance("com.sun.star.drawing.GroupShape")
        self._page.add(group)
        for shape in shapes:
            group.add(shape.unwrap())

    def _create_shape(self) -> Shape:
        shape = self._doc.createInstance("com.sun.star.drawing.TextShape")
        self._page.add(shape)
        return Shape(shape)

    def _get_document(self):
        localContext = uno.getComponentContext()
        resolver = localContext.ServiceManager.createInstanceWithContext(
            "com.sun.star.bridge.UnoUrlResolver", localContext)
        context = resolver.resolve(
            "uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
        desktop = context.ServiceManager.createInstanceWithContext(
            "com.sun.star.frame.Desktop", context)

        return desktop.getCurrentComponent()


if __name__ == '__main__':
    doc = Document()
    doc.create_box(Geometry(0, 0, 5000, 8000), "myTitle", "myContent")
