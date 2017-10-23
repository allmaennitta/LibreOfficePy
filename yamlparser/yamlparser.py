import utils
import yaml
from yamlparser import ENTITY_CONFIG

from typing import Dict, List, Any


# props, subs, flags, presets

# "TextType"

class Node():
    """Node of organization chart. Converted from Yaml via Dict to Object"""

    def __init__(self, myDict):
        # String-Nodes are filtered
        if isinstance(myDict, str) or myDict == {}:
            print("Node is ignored, because it has no type: %s" % myDict)
            self.type = "NoneType"
            return

        if not "type" in myDict:
            raise ValueError("Node has no type attribute: %s" % myDict)

        self.type = myDict["type"]
        self.raw = myDict
        print("Dict: "+str(self.raw))
        self._nodes = []
        self.config = ENTITY_CONFIG[self.type]

        self._set_attributes()
        self._check_subtypes()
        self._incorporate_flags()
        self._incorporate_presets()

        if hasattr(self, "is_text"):
            self.type = "TextNode"
            self.text = self.node_as_text()

            # for k, v in myDict.items():
            #     if k in ("sub"):
            #         pass
            #     elif isinstance(v, (list, tuple)):
            #         setattr(self, k,
            #                 [Node(x) if isinstance(x, dict) else x for x in v])
            #     else:
            #         setattr(self, k, Node(v) if isinstance(v, dict) else v)

    def _set_attributes(self):
        """Only attributes are created which correspond with type config"""
        for prop in self.config["props"]:
            setattr(self, prop, self.raw[prop])

    def _check_subtypes(self):
        """check types of sub-nodes"""
        if "sub" not in self.raw:
            return

        for dict_node in self.raw["sub"]:
            if isinstance(dict_node, str):
                continue
            print(str(dict_node))
            if dict_node["type"] not in self.config["subs"]:
                raise ValueError(
                    "%s-Type not allowed in subs of Type %s" % (
                        dict_node["type"], self.type))

    def _incorporate_flags(self):
        """check flags and set flag-properties"""
        if "flags" not in self.raw:
            return

        for flag in self.raw["flags"]:
            if flag not in self.config["flags"]:
                raise ValueError("%s-Flag not allowed in nodes of Type %s" % (
                        flag, self.type))
            else:
                setattr(self, flag, True)

    def _incorporate_presets(self):
        """set preset-properties"""
        if "presets" not in self.config:
            return

        for preset in self.config["presets"]:
            if not hasattr(self, preset):
                setattr(self, preset, True)

    def node_as_text(self):
        content = ""
        if hasattr(self, "position"):
            content += self.position + ": "
        if hasattr(self, "name"):
            content += self.name
        return content

    @property
    def nodes(self):
        return self._nodes


class YamlParser:
    def __init__(self, filename: str):
        self.filename = filename
        self._model = []
        self._nodes = []

    @property
    def nodes(self):
        return self._nodes

    def parseOrganization(self) -> List[Node]:
        with open(utils.get_filename(self.filename), "r") as f:
            self._model = yaml.safe_load(f)

        self.walk_list(self._model, self)
        return self._nodes

    def parseOrgaUnit(self, yml: str) -> List[Node]:
        self._model = yaml.safe_load(yml)
        self.walk_list(self._model, self)

    def walk_list(self, dict_nodes, parent):
        for dict_node in dict_nodes:
            if isinstance(dict_node, list):
                print("Lists are ignored at this location: %s" % dict_node)
                dict_node = {}

            node = self.parse_node(dict_node)
            parent.nodes.append(node)

    def parse_node(self, dict_node) -> Node:
        node = Node(dict_node)
        if node.type in ("TextType", "NoneType"):
            return node

        if "sub" in dict_node:
            self.walk_list(dict_node["sub"], node)
        return node


if __name__ == '__main__':
    parser = YamlParser()

    # parse(r"E:\Data\GMX_Mediacenter\CW\Rohdateien\example.yaml")
    print(parser.parseOrganization(
        r"C:\Users\ingo\Development\python\LibreOffice\Resources\organization_chart.yaml"))
