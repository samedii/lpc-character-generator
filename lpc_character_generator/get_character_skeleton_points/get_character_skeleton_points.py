import copy

from .draw_skeleton import draw_skeleton
from lpc_character_generator.get_character_points import get_character_points


def get_character_skeleton_points(
    generated_character: dict,
    visualize_points: bool = False,
):
    new_character = copy.deepcopy(generated_character)
    new_character["skeleton_points"] = get_character_points(new_character)

    if visualize_points:
        draw_skeleton(new_character)

    return new_character
