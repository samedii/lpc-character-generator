from typing import Optional

from lpc_character_generator.constants import (
    Action,
    Direction,
    UNAVAILABLE_ACTIONS,
    NON_ROTATION_ACTIONS,
)


def get_available_actions(direction: Optional[Direction], do_rotation: Optional[bool]):
    # filter by rotation
    action_set = set(Action)
    available_actions = (
        action_set if not do_rotation else action_set - NON_ROTATION_ACTIONS
    )

    # filter by direction
    available_actions = (
        available_actions
        if direction is None
        else available_actions - UNAVAILABLE_ACTIONS.get(direction, set())
    )

    return list(available_actions)
