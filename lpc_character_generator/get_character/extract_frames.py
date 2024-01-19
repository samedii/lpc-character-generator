from PIL import Image
from typing import Optional

from lpc_character_generator.image_utilities import get_frame
from lpc_character_generator.constants import Action, Direction, FRAME_SIZE
from lpc_character_generator.general_utilities import (
    extract_rotation_points,
    extract_direction_points,
)


def extract_frames(
    is_rotation: bool,
    action_type: Action,
    direction: Optional[Direction],
    rotation_column: Optional[int],
    asset_image: Image.Image,
) -> list[Image.Image]:
    image_width = asset_image.size[0]
    frame_count = int(image_width / FRAME_SIZE)
    extracted_points = (
        extract_rotation_points(rotation_column)
        if is_rotation
        else extract_direction_points(action_type, direction, frame_count)
    )

    extracted_frames = [
        get_frame(row, column, asset_image) for row, column in extracted_points
    ]
    return extracted_frames
