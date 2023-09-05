from PIL import Image
from lpc_character_generator.constants import FRAME_SIZE


def get_frame(row: int, column: int, image: Image.Image):
    left = column * FRAME_SIZE
    upper = row * FRAME_SIZE
    right = left + FRAME_SIZE
    lower = upper + FRAME_SIZE

    cropped_frame = image.crop((left, upper, right, lower))

    return cropped_frame
