from PIL import Image
from lpc_character_generator.constants import ROTATION_ORDER, DEFAULT_DIRECTION_ROW
from lpc_character_generator.image_utilities import get_frame


def extract_rotation_frames(rotation_column: int, asset_image: Image.Image):
    return [
        get_frame(DEFAULT_DIRECTION_ROW[direction], rotation_column, asset_image)
        for direction in ROTATION_ORDER
    ]
