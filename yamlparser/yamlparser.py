import utils
import yaml
import argparse

from typing import Dict, List

class Node(argparse.Namespace):
    """Node of organization chart. Converted from Yaml via Dict to Object"""
    def __init__(self, myDict):
        for k, v in myDict.items():
            if k in ("sub"):
                pass
            elif isinstance(v, (list, tuple)):
                setattr(self, k,
                        [Node(x) if isinstance(x, dict) else x for x in v])
            else:
                setattr(self, k, Node(v) if isinstance(v, dict) else v)

class YamlParser:
    def __init__(self):
        self._nodes = []
        self._model = {}

    @property
    def nodes(self):
        return self._nodes

    def parseOrganization(self, filename: str) -> List[Node]:
        with open(utils.get_filename(filename), "r") as f:
            self._model = yaml.safe_load(f)

        self.parse_model(self._model)
        return self._nodes

    def parseOrgaUnit(self, yml: str):
        self._model = yaml.safe_load(yml)
        self.parse_model(self._model)

    def parse_model(self, model):
        for k, v in model.items():
            if isinstance(v, dict):
                self.parse_model(v)
                if v["type"]:
                    self._nodes.append(Node(v))
            elif isinstance(v, list):
                self.walk_list(v)

    def walk_list(self, mylist):
        for v in mylist:
            if isinstance(v, dict):
                if v["type"]:
                    self._nodes.append(Node(v))
                self.parse_model(v)
            elif isinstance(v, list):
                self.walk_list(v)




if __name__ == '__main__':
    parser = YamlParser()

    # parse(r"E:\Data\GMX_Mediacenter\CW\Rohdateien\example.yaml")
    print(parser.parseOrganization(
        r"C:\Users\ingo\Development\python\LibreOffice\Resources\organization_chart.yaml"))
