from lpc_character_generator.constants import Action, Direction
from .get_random_character import get_random_character


def generate(
    action: Action = None, direction: Direction = None, do_rotation: bool = None
):
    return get_random_character(action, direction, do_rotation)
