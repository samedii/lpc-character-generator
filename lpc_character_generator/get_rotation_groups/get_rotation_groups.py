import json

from lpc_character_generator.constants import (
    Action,
    ACTION_TO_FILENAME,
    PATH_TO_ROTATION_GROUPS,
)


def get_rotation_groups(action: Action, rotation_column: int) -> list[list[str]]:
    rotation_group_path = (
        PATH_TO_ROTATION_GROUPS / ACTION_TO_FILENAME[action] / f"{rotation_column}.json"
    )
    rotation_groups = json.load(open(rotation_group_path))

    return rotation_groups
