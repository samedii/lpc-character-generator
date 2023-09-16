import random

from typing import Optional
from lpc_character_generator.get_character import get_character
from lpc_character_generator.constants import (
    Sex,
    Asset,
    Action,
    Direction,
    ASSET_TO_PARAM,
    GENDERED_ASSETS,
    ALLOWED_DIRECTIONS,
    NON_OPTIONAL_ASSETS,
)

from .should_rotate import should_rotate
from .get_random_column import get_random_column
from .get_available_assets import get_available_assets
from .assets_conflict import assets_conflict


def get_random_character(
    action: Optional[Action],
    direction: Optional[Direction],
    do_rotation: Optional[bool],
) -> dict:
    settings = {}
    character = {}
    included_assets = {}
    sex = random.choice(list(Sex))
    action = random.choice(list(Action)) if action is None else action
    direction_pool = ALLOWED_DIRECTIONS.get(action, list(Direction))
    possible_assets = {asset_type for asset_type in Asset} - GENDERED_ASSETS.get(
        sex, set()
    )

    if direction is None and do_rotation is None:
        do_rotation = should_rotate(action)

    if not do_rotation and direction is None:
        direction = random.choice(direction_pool)

    for asset_type in possible_assets:
        skip = random.randint(0, 1)

        if (skip and asset_type not in NON_OPTIONAL_ASSETS) or assets_conflict(
            included_assets, asset_type
        ):
            continue

        available_assets = get_available_assets(sex, asset_type, action)

        if not available_assets:
            continue

        _, chosen_asset = random.choice(available_assets)

        param = ASSET_TO_PARAM[asset_type]
        settings[param] = chosen_asset
        included_assets[asset_type] = chosen_asset

    settings["sex"] = sex
    settings["action"] = action
    if direction is not None:
        settings["direction"] = direction

    if do_rotation:
        settings["rotation_column"] = get_random_column(action)

    character["settings"] = settings
    character["animation"] = get_character(**settings)

    return character
