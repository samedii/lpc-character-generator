from lpc_character_generator.constants import Action, Direction
from .get_random_character import get_random_character


def generate(
    action: Action = None,
    direction: Direction = None,
    is_rotation: bool = None,
    for_rotation_groups: bool = False,
):
    return get_random_character(for_rotation_groups, action, direction, is_rotation)
