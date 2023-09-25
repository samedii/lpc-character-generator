import random

from typing import Optional
from lpc_character_generator.get_character import get_character
from lpc_character_generator.get_characteristics import get_characteristics
from lpc_character_generator.get_character_description import get_character_description
from lpc_character_generator.constants import (
    Sex,
    Action,
    Direction,
    PUT_ON_ORDER,
    ASSET_TO_PARAM,
    GENDERED_ASSETS,
    ALLOWED_DIRECTIONS,
    ACTION_DESCRIPTIONS,
    NON_OPTIONAL_ASSETS,
    NON_ROTATION_ACTIONS,
    ASSET_COMPLEMENTARITY,
)

from .should_rotate import should_rotate
from .assets_conflict import assets_conflict
from .get_random_column import get_random_column
from .get_available_assets import get_available_assets
from .get_by_complementarity import get_by_complementarity


def get_random_character(
    action: Optional[Action],
    direction: Optional[Direction],
    do_rotation: Optional[bool],
) -> dict:
    settings = {}
    character = {}
    included_assets = {}
    sex = random.choice(list(Sex))
    available_actions = (
        list(Action) if not do_rotation else list(set(Action) - NON_ROTATION_ACTIONS)
    )
    action = random.choice(available_actions) if action is None else action
    direction_pool = ALLOWED_DIRECTIONS.get(action, list(Direction))
    gendered_set = GENDERED_ASSETS.get(sex, set())
    possible_assets = [x for x in PUT_ON_ORDER if x not in gendered_set]

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

        is_complementary = asset_type in ASSET_COMPLEMENTARITY
        available_assets = (
            get_available_assets(sex, asset_type, action)
            if not is_complementary
            else get_by_complementarity(sex, action, asset_type, included_assets)
        )

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
    characteristics = get_characteristics(included_assets)

    character["action_description"] = ACTION_DESCRIPTIONS[action]
    character["description"] = get_character_description(sex, characteristics)
    character["animation"] = get_character(**settings)
    settings["do_rotation"] = False if do_rotation is None else do_rotation
    character["settings"] = settings

    return character
