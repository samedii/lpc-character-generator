import random

from lpc_character_generator.constants import Action, NON_ROTATION_ACTIONS


def should_rotate(action: Action) -> bool:
    if action not in NON_ROTATION_ACTIONS:
        # rotate with some probability
        rotation_probability = 1 / (len(Action) + 1)
        return random.random() < rotation_probability

    return False
