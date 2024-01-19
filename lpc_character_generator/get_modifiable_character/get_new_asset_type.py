import random

from .at_least_one_available import at_least_one_available

from lpc_character_generator.get_random_character.assets_conflict import assets_conflict
from lpc_character_generator.constants import (
    Asset,
    GENDERED_ASSETS,
    ASSET_COMPLEMENTARITY,
    NO_DESCRIPTION_ASSETS,
)


def get_new_asset_type(base_settings):
    sex = base_settings["sex"]
    action = base_settings["action"]
    gendered_set = GENDERED_ASSETS.get(sex, set())

    possible_items = set(list(Asset)) - {Asset.BODY, Asset.HEAD}
    # it shouldn't be in conflict with any current assets
    # it shouldn't be a complementary asset
    # it shouldn't be incorrect sex asset
    # it should be describable
    # it should be available for current action
    possible_items = [
        asset_type
        for asset_type in possible_items
        if not assets_conflict(base_settings, asset_type)
        and asset_type not in ASSET_COMPLEMENTARITY
        and asset_type not in gendered_set
        and asset_type not in NO_DESCRIPTION_ASSETS
        and at_least_one_available(sex, asset_type, action)
    ]

    new_asset_type = random.choice(possible_items)

    return new_asset_type
