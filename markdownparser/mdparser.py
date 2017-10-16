import utils


def parse(filename: str):
    boxes = {}
    title = None
    content = []
    with open(utils.get_filename(filename), "r") as f:
        for line in f:
            line = line.strip()
            if line.isspace():
                continue
            if line.startswith("# "):
                if title and content and len(title) > 0 and len(content) > 0:
                    boxes[title] = content
                title = line[2:]
                content = []
                continue
            if line.startswith("* "):
                content.append(line[2:])
                continue
    return boxes

if __name__ == '__main__':
    parse("test")
