import time
import pytest
import numpy as np
import lpc_character_generator as generator

from PIL import Image
from lpc_character_generator.constants import (
    Action,
    Direction,
    ALLOWED_DIRECTIONS,
    NON_ROTATION_ACTIONS,
)

_ROTATION_ACTIONS = set(Action) - NON_ROTATION_ACTIONS


def run_test(inputs, prefix):
    generated_characters = []
    for_rotation_group = inputs.get("for_rotation_groups", False)

    start_time = time.time()
    n_times = 10

    for _ in range(n_times):
        generated_character = generator.generate(**inputs)

        animation = generated_character["animation"]
        generated_characters.append(animation)

        settings = generated_character["settings"]

        for param_name, param_value in inputs.items():
            if param_name != "for_rotation_groups":
                assert settings[param_name] == param_value

        if for_rotation_group:
            assert generated_character.get("rotation_groups", None) is not None

        assert isinstance(animation[0], (Image.Image, np.ndarray))

    end_time = time.time()

    for index, images in enumerate(generated_characters):
        animation = Image.fromarray(np.concatenate(images, axis=1))
        animation.save(f"tests/results/{prefix}_{index}.png")

    assert (end_time - start_time) / n_times <= 0.1


def test_full_random():
    run_test({}, "random")


@pytest.mark.parametrize("direction", Direction)
@pytest.mark.parametrize("action", Action)
def test_direction(action, direction):
    inputs = {"action": action, "direction": direction}
    available_dirs = ALLOWED_DIRECTIONS.get(action, set(Direction))

    if direction not in available_dirs:
        return

    run_test(inputs, f"{action}_{direction}")


@pytest.mark.parametrize("action", _ROTATION_ACTIONS)
def test_rotation(action):
    inputs = {"action": action, "is_rotation": True}

    run_test(inputs, f"{action}_rotation")


def test_for_rotation_groups():
    inputs = {"is_rotation": True, "for_rotation_groups": True}

    run_test(inputs, f"rotation_groups")
