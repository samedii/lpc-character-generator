import time
import pytest
import numpy as np
import lpc_character_generator as generator

from PIL import Image
from itertools import product
from lpc_character_generator.constants import Action, Direction, NON_ROTATION_ACTIONS

_FULL_ACTIONS = set(Action) - {Action.CLIMB}
_DIRECTION_SETTINGS = list(product(_FULL_ACTIONS, Direction)) + [
    (Action.CLIMB, Direction.NORTH)
]


def run_point_test(inputs, is_rotation_test=False):
    animation_skeleton = []
    start_time = time.time()
    n_times = 10

    for _ in range(n_times):
        generated_character = generator.generate(**inputs)
        character_with_points = generator.generate_points(generated_character)
        character_with_points_visualized = generator.generate_points(
            generated_character, visualize_points=True
        )

        animation_skeleton.append(
            character_with_points_visualized["skeleton_animation"]
        )

        assert len(generated_character["animation"]) == len(
            character_with_points["skeleton_points"]
        ) and len(generated_character["animation"]) == len(
            character_with_points_visualized["skeleton_points"]
        )

    end_time = time.time()

    file_prefix = "dir" if not is_rotation_test else "rot"

    for index, images in enumerate(animation_skeleton):
        animation = Image.fromarray(np.concatenate(images, axis=1))
        animation.save(f"tests/results/{file_prefix}_skeleton_{index}.png")

    assert (end_time - start_time) / (2 * n_times) <= 0.05


@pytest.mark.parametrize("params", _DIRECTION_SETTINGS)
def test_point_animations(params):
    action, direction = params
    inputs = {"action": action, "direction": direction}
    run_point_test(inputs)


@pytest.mark.parametrize("action", Action)
def test_point_rotations(action):
    if action in NON_ROTATION_ACTIONS:
        return

    inputs = {"action": action, "is_rotation": True}
    run_point_test(inputs, is_rotation_test=True)
