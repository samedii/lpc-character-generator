from lpc_character_generator.constants import ROTATION_ORDER
from lpc_character_generator.image_utilities import upscale_image, draw_edges


def draw_skeleton(new_character) -> None:
    scale_factor = 2
    new_character["skeleton_animation"] = []
    direction = new_character["settings"].get("direction", None)

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
