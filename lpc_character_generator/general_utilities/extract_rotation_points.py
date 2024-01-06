from lpc_character_generator.constants import ROTATION_ORDER, DEFAULT_DIRECTION_ROW


def extract_rotation_points(rotation_column: int) -> list[tuple[int, int]]:
    return [
        (DEFAULT_DIRECTION_ROW[direction], rotation_column)
        for direction in ROTATION_ORDER
    ]
