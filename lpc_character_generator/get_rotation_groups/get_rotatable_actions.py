from lpc_character_generator.constants import Action

from .get_rotation_groups import get_rotation_groups


def get_rotatable_actions():
    actions = []
    rotation_groups = get_rotation_groups()

    for action, all_rotation_groups in rotation_groups.items():
        if any(
            len(rotation_group) != 0 for rotation_group in all_rotation_groups.values()
        ):
            actions.append(Action(action))

    return set(actions)
