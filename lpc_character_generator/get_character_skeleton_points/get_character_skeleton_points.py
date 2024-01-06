import copy

from lpc_character_generator.constants import ROTATION_ORDER
from lpc_character_generator.get_character_points import get_character_points
from lpc_character_generator.image_utilities import upscale_image, draw_edges


def get_character_skeleton_points(
    generated_character: dict,
    visualize_points: bool = False,
):
    scale_factor = 4
    direction = generated_character["settings"].get("direction", None)
    new_character = copy.deepcopy(generated_character)
    new_character["skeleton_points"] = get_character_points(new_character)

    new_character["skeleton_animation"] = []

    if visualize_points:
        for i, (character_image, point_coordinates) in enumerate(
            zip(new_character["animation"], new_character["skeleton_points"])
        ):
            rescaled_image = upscale_image(character_image, scale_factor)

            if direction is None:
                draw_edges(
                    rescaled_image, point_coordinates, ROTATION_ORDER[i], scale_factor
                )
            else:
                draw_edges(rescaled_image, point_coordinates, direction, scale_factor)

            new_character["skeleton_animation"].append(rescaled_image)

    return new_character
