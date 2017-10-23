import utils
import yaml

ENTITY_CONFIG = {}
with open(utils.get_filename(r"C:\Users\ingo\Development\python\LibreOffice\entity_config.yaml"), "r") as f:
    ENTITY_CONFIG = yaml.safe_load(f)