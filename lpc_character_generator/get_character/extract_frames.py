from PIL import Image
from typing import Optional
from lpc_character_generator.constants import Action, Direction

from .extract_direction_frames import extract_direction_frames
from .extract_rotation_frames import extract_rotation_frames


def extract_frames(
    action_type: Action,
    direction: Optional[Direction],
    rotation_column: Optional[int],
    asset_image: Image.Image,
) -> list[Image.Image]:
    if direction is None:
        return extract_rotation_frames(rotation_column, asset_image)

    return extract_direction_frames(action_type, direction, asset_image)
