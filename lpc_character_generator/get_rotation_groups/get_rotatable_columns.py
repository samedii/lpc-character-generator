from lpc_character_generator.constants import Action

from .get_rotation_groups import get_rotation_groups


def get_rotatable_columns(action: Action) -> list[int]:
    all_rotation_groups = get_rotation_groups()
    rotation_groups = all_rotation_groups[action]

    rotation_columns = [
        int(rotation_column)
        for rotation_column, rotation_group in rotation_groups.items()
        if len(rotation_group) > 0
    ]

    return rotation_columns
