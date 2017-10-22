import utils
import yaml
import argparse

from typing import Dict

entities = []

def parseOrganization(filename: str):
    model = {}
    with open(utils.get_filename(filename), "r") as f:
        model = yaml.safe_load(f)

    parse_model(model)
    return entities


def parse_model(model):
    for k, v in model.items():
        if isinstance(v, dict):
            if v["type"]:
                entities.append(Entity(v))
            parse_model(v)
        elif isinstance(v, list):
            walk_list(v)


def walk_list(mylist):
    for v in mylist:
        if isinstance(v, dict):
            if v["type"]:
                entities.append(Entity(v))
            parse_model(v)
        elif isinstance(v, list):
            walk_list(v)

class Entity(argparse.Namespace):
    def __init__(self, myDict):
        for k, v in myDict.items():
            if k in ("sub"):
                pass
            elif isinstance(v, (list, tuple)):
               setattr(self, k, [Entity(x) if isinstance(x, dict) else x for x in v])
            else:
               setattr(self, k, Entity(v) if isinstance(v, dict) else v)



if __name__ == '__main__':
    # parse(r"E:\Data\GMX_Mediacenter\CW\Rohdateien\example.yaml")
    parseOrganization(
        r"C:\Users\ingo\Development\python\LibreOffice\Resources\organization_chart.yaml")
    print(entities)
