import random

from lpc_character_generator.constants import Action, ACTION_TO_COLUMNS


def get_random_column(action: Action) -> int:
    column_number = ACTION_TO_COLUMNS[action]

    return random.randint(0, column_number - 1)
