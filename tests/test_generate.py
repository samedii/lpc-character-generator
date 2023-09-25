import time
import pytest
import numpy as np
import lpc_character_generator as generator

from PIL import Image
from itertools import product
from lpc_character_generator.constants import Action, Direction

_FULL_ACTIONS = set(Action) - {Action.CLIMB}
_TEST_SETTINGS = list(product(_FULL_ACTIONS, Direction))


@pytest.mark.parametrize("params", _TEST_SETTINGS)
def test_generate(params):
    action, direction = params
    base_input = {"action": action}
    direction_input = base_input.copy()
    direction_input["direction"] = direction
    rotation_input = base_input.copy()
    rotation_input["do_rotation"] = True
    generated_characters = []
    character_prefixes = [
        "random_character",
        "direction_character",
        "rotation_character",
    ]
    inputs = [base_input, direction_input, rotation_input]
    start_time = time.time()
    n_times = 10

    for i in range(n_times):
        for curr_input in inputs:
            generated_character = generator.generate(**curr_input)

            animation = generated_character["animation"]
            generated_characters.append(animation)

            settings = generated_character["settings"]

            for param_name, param_value in curr_input.items():
                assert settings[param_name] == param_value

            assert isinstance(animation[0], (Image.Image, np.ndarray))

    end_time = time.time()

    for index, images in enumerate(generated_characters):
        animation = Image.fromarray(np.concatenate(images, axis=1))
        animation.save(
            f"tests/results/{character_prefixes[index % len(inputs)]}_{index}.png"
        )

    assert (end_time - start_time) / (len(inputs) * n_times) <= 0.15
