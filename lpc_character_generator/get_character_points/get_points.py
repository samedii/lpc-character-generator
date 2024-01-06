import json

from lpc_character_generator.constants import (
    Action,
    ACTION_TO_FILENAME,
    PATH_TO_SKELETON_TRACKING,
)


def get_points(action: Action, file_name: str):
    action_file = ACTION_TO_FILENAME[action]
    point_path = PATH_TO_SKELETON_TRACKING / action_file / file_name

    return json.load(open(point_path))
