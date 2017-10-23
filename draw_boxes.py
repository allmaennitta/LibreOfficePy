from draw.document import Document
from draw.utils import Geometry
from markdownparser.mdparser import parseForBoxes, parseForTitles
from yamlparser.yamlparser import YamlParser


def boxes(filename: str):
    # boxes = parseForBoxes(r"")
    # boxes = parse(r"")
    doc = Document()
    for key in boxes.keys():
        print(key + "; " + "\n".join(boxes[key]))
        doc.create_titled_box(Geometry(0, 0, 5000, 7000), key,
                              "\n".join(boxes[key]))


def titles(filename: str):
    titles = parseForTitles(filename)
    doc = Document()
    doc.go_to_page(1)
    for entry in titles:
        print(entry)
        doc.create_title(Geometry(0, 0, 5000, 1000), entry)


def organization_units(filename: str):
    p = YamlParser(filename)
    ous = p.parseOrganization()
    pass
    # doc = Document()
    # doc.go_to_page(4)
    #
    # for ou in ous:
    #     # if ou.type in ("department", "body", "institution", "team"):
    #     #     if not hasattr(ou, "members"):
    #     #         geometry = Geometry(0, 0, 5000, 3000)
    #     #         content = ""
    #     #     else:
    #     #         geometry = Geometry(0, 0, 5400, 7000)
    #     #         content = "\n".join(ou.members)
    #     #
    #     #     doc.create_titled_box(geometry, ou.name, content,
    #     #                           style_title="o_Title_fat", style_box="o_Box")
    #
    #     if ou.type in ("role", "executive role"):
    #         doc.create_double_title(Geometry(0, 0, 5000, 1600),
    #                          ou.position, ou.name)
    #     # elif ou.type in ("note",):
    #     #     doc.create_box(Geometry(0, 0, 5000, 7000), ou.content,
    #     #                    style="o_Box")
    #     print(ou)


if __name__ == '__main__':
    # titles(r"E:\Data\GMX_Mediacenter\CW\Rohdateien\IT.txt")
    # boxes(r"C:\Users\ingo\Development\python\LibreOffice\Resources\example.md")
    # boxes(r"E:\Data\GMX_Mediacenter\CW\Rohdateien\IT.txt")
    organization_units(
        r"E:\Data\GMX_Mediacenter\CW\Rohdateien\organization_chart.yaml")
    # organization_units(r"C:\Users\ingo\Development\python\LibreOffice\Resources\example.yaml")
