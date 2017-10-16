from draw.document import Document
from draw.utils import Geometry
from markdownparser.mdparser import parse

def main():
    boxes = parse(r"C:\Users\ingo\Development\python\LibreOffice\Resources\example.md")
    doc = Document()
    for key in boxes.keys():
        print(key+"; "+"\n".join(boxes[key]))
        doc.create_box(Geometry(0, 0, 5000, 8000), key, boxes[key])


if __name__ == '__main__':
    main()