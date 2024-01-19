import pytest
import numpy as np
import lpc_character_generator as generator

from PIL import Image
from pathlib import Path
from lpc_character_generator.constants import (
    Direction,
    Action,
    Sex,
    DEFAULT_DIRECTION_ROW,
    ROTATION_ORDER,
)
from lpc_character_generator.image_utilities import get_frame, add_asset

_TEST_ASSETS = {
    "hair": "balding head blue",
    "neck": "bowtie amber",
    "over_shirt": "cardigan amethyst",
    "pants": "cuffed pants charcoal",
    "shirt": "polo forest",
    "shoes": "shoes ice",
    "eyebrows": "thick blonde",
    "eyes": "eyes gray",
    "head_accessory": "bascinet closed helmet gold",
    "helmet_accessory": "bascinet plumage coffee",
    "shield_base": "brown",
    "shield_paint": "apple",
    "shield_pattern": "barry apricot",
    "facial_hair": "chevron mustache blonde",
    "shield_trim": "copper",
    "sword": "sword brass",
}


@pytest.fixture
def default_character():
    return {"sex": Sex.MAN, "body": "old porcelain", "action": Action.COMBAT_IDLE}


@pytest.mark.parametrize("asset", _TEST_ASSETS.items())
@pytest.mark.parametrize("direction", list(Direction))
def test_direction_create(default_character, asset, direction):
    default_character["is_rotation"] = False
    asset_type, asset_name = asset
    path_to_asset = Path(f"tests/assets/{asset_type}.png")
    additional_asset = Image.open(path_to_asset)
    additional_frames = [
        get_frame(DEFAULT_DIRECTION_ROW[direction], i, additional_asset)
        for i in range(2)
    ]
    path_to_behind = Path(f"tests/assets/behind {asset_type}.png")
    behind_asset = None

    if path_to_behind.exists():
        behind_asset = Image.open(path_to_behind)
        behind_frames = [
            get_frame(DEFAULT_DIRECTION_ROW[direction], i, behind_asset)
            for i in range(2)
        ]

    default_character["direction"] = direction
    new_character_settings = default_character.copy()
    new_character_settings[asset_type] = asset_name

    base_character = generator.create(**default_character)
    new_character = generator.create(**new_character_settings)
    test_character = [
        add_asset(base, new) for new, base in zip(additional_frames, base_character)
    ]

    if behind_asset is not None:
        test_character = [
            add_asset(base, new) for new, base in zip(test_character, behind_frames)
        ]

    np_new = [np.array(frame) for frame in new_character]
    np_test = [np.array(frame) for frame in test_character]

    assert np.array_equal(np_new, np_test)


@pytest.mark.parametrize("asset", _TEST_ASSETS.items())
@pytest.mark.parametrize("rotation_column", [0, 1, 2, 3])
def test_rotation_create(default_character, asset, rotation_column):
    default_character["is_rotation"] = True
    asset_type, asset_name = asset
    path_to_asset = f"tests/assets/{asset_type}.png"
    additional_asset = Image.open(path_to_asset)
    index_order = [DEFAULT_DIRECTION_ROW[direction] for direction in ROTATION_ORDER]
    additional_frames = [
        get_frame(i, rotation_column, additional_asset) for i in index_order
    ]

    path_to_behind = Path(f"tests/assets/behind {asset_type}.png")
    behind_asset = None

    if path_to_behind.exists():
        behind_asset = Image.open(path_to_behind)
        behind_frames = [
            get_frame(i, rotation_column, behind_asset) for i in index_order
        ]

    default_character["rotation_column"] = rotation_column
    new_character_settings = default_character.copy()
    new_character_settings[asset_type] = asset_name

    base_character = generator.create(**default_character)
    new_character = generator.create(**new_character_settings)
    test_character = [
        add_asset(base, new) for new, base in zip(additional_frames, base_character)
    ]

    if behind_asset is not None:
        test_character = [
            add_asset(base, new) for new, base in zip(test_character, behind_frames)
        ]

    np_new = [np.array(frame) for frame in new_character]
    np_test = [np.array(frame) for frame in test_character]

    assert np.array_equal(np_new, np_test)
