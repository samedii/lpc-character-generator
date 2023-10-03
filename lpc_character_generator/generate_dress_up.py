from lpc_character_generator.constants import Direction, ClothingState
from lpc_character_generator.get_modifiable_character import get_modifiable_character


def generate_dress_up(
    clothing_state: ClothingState = None, direction: Direction = None
):
    return get_modifiable_character(clothing_state, direction)
