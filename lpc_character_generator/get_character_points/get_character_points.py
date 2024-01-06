from .get_points import get_points
from .format_file_name import format_file_name

from lpc_character_generator.general_utilities import (
    extract_direction_points,
    extract_rotation_points,
)


def get_character_points(generated_character: dict):
    settings = generated_character["settings"]
    action = settings["action"]
    direction = settings.get("direction", None)
    rotation_column = settings.get("rotation_column", None)

    animation_coordinates = (
        extract_rotation_points(rotation_column)
        if direction is None
        else extract_direction_points(
            action, direction, frame_count=len(generated_character["animation"])
        )
    )

    file_names = [
        format_file_name(row=coordinates[0], column=coordinates[1])
        for coordinates in animation_coordinates
    ]
    animation_points = [get_points(action, file_name) for file_name in file_names]

    return animation_points
