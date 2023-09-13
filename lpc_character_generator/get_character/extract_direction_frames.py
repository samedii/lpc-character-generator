from PIL import Image
from lpc_character_generator.image_utilities import get_frame
from lpc_character_generator.constants import (
    Action,
    Direction,
    DEFAULT_DIRECTION_ROW,
    DIRECTION_ROW,
    FRAME_SIZE,
)


def extract_direction_frames(
    action_type: Action, direction: Direction, asset_image: Image.Image
):
    width = asset_image.size[0]
    direction_to_row = DIRECTION_ROW.get(action_type, DEFAULT_DIRECTION_ROW)
    row = direction_to_row[direction]
    frame_count = int(width / FRAME_SIZE)

    frames = [get_frame(row, i, asset_image) for i in range(frame_count)]
    return frames
