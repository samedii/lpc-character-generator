import time
import pytest
import numpy as np

from PIL import Image
from itertools import product

import lpc_character_generator as generator
from lpc_character_generator.constants import ClothingState, Direction

_TEST_SETTINGS = product(ClothingState, Direction)


def generate_dress_up(params):
    clothing_state, direction = params
    result = generator.generate_dress_up(clothing_state, direction)
    return [
        result["Base Character"],
        result["New Character"],
        result["Item Image"],
    ], result["Item Description"]


@pytest.mark.parametrize("params", _TEST_SETTINGS)
def test_dress_up(params):
    clothing_state, direction = params
    param_options = [(clothing_state, None), (None, direction), (None, None)]
    starting_title = [clothing_state, direction, "random"]
    images_to_save = []

    n_times = 10
    start_time = time.time()
    for j, param in enumerate(param_options):
        last_generated = {}
        for i in range(n_times):
            images, description = generate_dress_up(param)
            image = Image.fromarray(np.concatenate(images, axis=1))
            last_generated["image"] = image
            last_generated["file_name"] = f"{starting_title[j]}_{description}_{i}.png"

        images_to_save.append(last_generated)

    end_time = time.time()

    for image_dict in images_to_save:
        image = image_dict["image"]
        file_name = image_dict["file_name"]

        image.save(f"tests/results/{file_name}")

    assert (end_time - start_time) / (len(param_options) * n_times) <= 0.15
