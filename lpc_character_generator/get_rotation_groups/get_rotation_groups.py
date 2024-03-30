import json

from lpc_character_generator.constants import PATH_TO_ROTATION_GROUPS


def get_rotation_groups() -> dict:
    rotation_groups = json.load(open(PATH_TO_ROTATION_GROUPS))
    return rotation_groups
