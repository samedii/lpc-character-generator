from lpc_character_generator.get_character_skeleton_points import (
    get_character_skeleton_points,
)


def generate_points(
    generated_character: dict,
    include_skeleton: bool = True,
    visualize_points: bool = False,
):
    new_character = generated_character

    if include_skeleton:
        new_character = get_character_skeleton_points(new_character, visualize_points)

    return new_character
