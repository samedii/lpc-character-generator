import random

from typing import Optional
from lpc_character_generator.get_character import get_character
from lpc_character_generator.get_rotation_groups import get_rotation_groups
from lpc_character_generator.get_characteristics import get_characteristics
from lpc_character_generator.get_character_description import get_character_description
from lpc_character_generator.constants import (
    Sex,
    Action,
    Direction,
    PUT_ON_ORDER,
    GENDERED_ASSETS,
    ALLOWED_DIRECTIONS,
    ACTION_DESCRIPTIONS,
    NON_OPTIONAL_ASSETS,
    ASSET_COMPLEMENTARITY,
)

from .skip_asset import skip_asset
from .should_rotate import should_rotate
from .add_body_asset import add_body_asset
from .assets_conflict import assets_conflict
from .get_random_column import get_random_column
from .get_available_assets import get_available_assets
from .get_available_actions import get_available_actions
from .get_by_complementarity import get_by_complementarity


def get_random_character(
    action: Optional[Action] = None,
    direction: Optional[Direction] = None,
    do_rotation: Optional[bool] = None,
    to_include: set = None,
    to_exclude: set = None,
    non_optional_assets=NON_OPTIONAL_ASSETS,
) -> dict:
    if to_exclude is None:
        to_exclude = set()
    if to_include is None:
        to_include = set()

    settings = {}
    character = {}
    included_assets = {}
    sex = random.choice(list(Sex))

    # filter according to direction
    available_actions = get_available_actions(direction, do_rotation)
    action = random.choice(available_actions) if action is None else action

    add_body_asset(included_assets, sex, action)
    gendered_set = GENDERED_ASSETS.get(sex, set())
    possible_assets = [
        asset
        for asset in PUT_ON_ORDER
        if asset not in gendered_set and asset not in included_assets
    ]

    if direction is None and do_rotation is None:
        do_rotation = should_rotate(action)

    direction_pool = ALLOWED_DIRECTIONS.get(action, list(Direction))
    if not do_rotation and direction is None:
        direction = random.choice(direction_pool)

    for asset_type in possible_assets:
        skip = skip_asset(sex, asset_type)
        is_optional = (
            asset_type not in non_optional_assets and asset_type not in to_include
        )

        if (
            asset_type in to_exclude
            or (skip and is_optional)
            or assets_conflict(included_assets, asset_type)
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

        chosen_asset = random.choice(available_assets)

        included_assets[asset_type] = chosen_asset

    if direction is not None:
        settings["direction"] = direction

    if do_rotation:
        settings["is_rotation"] = True
        rotation_column = get_random_column(action)
        settings["rotation_column"] = rotation_column
        character["rotation_groups"] = get_rotation_groups(action, rotation_column)
    else:
        settings["is_rotation"] = False

    settings["sex"] = sex
    settings["action"] = action
    settings.update(included_assets)

    characteristics = get_characteristics(included_assets)

    character["action_description"] = ACTION_DESCRIPTIONS[action]
    character["description"] = get_character_description(sex, characteristics)
    character["animation"] = get_character(**settings)
    character["settings"] = settings

    return character
