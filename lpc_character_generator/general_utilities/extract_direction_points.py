from lpc_character_generator.constants import (
    Action,
    Direction,
    DEFAULT_DIRECTION_ROW,
    DIRECTION_ROW,
)


def extract_direction_points(
    action_type: Action, direction: Direction, frame_count: int
) -> list[tuple[int, int]]:
    direction_to_row = DIRECTION_ROW.get(action_type, DEFAULT_DIRECTION_ROW)
    row = direction_to_row[direction]

    points = [(row, i) for i in range(frame_count)]
    return points
