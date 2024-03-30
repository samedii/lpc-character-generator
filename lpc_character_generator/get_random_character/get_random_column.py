import random

from lpc_character_generator.constants import Action, ACTION_TO_COLUMNS
from lpc_character_generator.get_rotation_groups import get_rotatable_columns


def get_random_column(action: Action, for_rotation_groups: bool) -> int:
    column_number = ACTION_TO_COLUMNS[action]

    return (
        random.choice(get_rotatable_columns(action))
        if for_rotation_groups
        else random.randint(0, column_number - 1)
    )
