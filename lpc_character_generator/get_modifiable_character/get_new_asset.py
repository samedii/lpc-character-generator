import random

from lpc_character_generator.constants import Asset, ASSET_COMPLEMENTARITY
from lpc_character_generator.get_random_character.get_available_assets import (
    get_available_assets,
)
from lpc_character_generator.get_random_character.get_by_complementarity import (
    get_by_complementarity,
)


def get_new_asset(base_settings: dict, asset_type: Asset):
    sex = base_settings["sex"]
    action = base_settings["action"]
    is_complementary = asset_type in ASSET_COMPLEMENTARITY
    # get all possible assets
    available_assets = (
        get_available_assets(sex, asset_type, action)
        if not is_complementary
        else get_by_complementarity(sex, action, asset_type, base_settings)
    )

    # remove currently equipped if present
    asset_in_base = base_settings.get(asset_type, None)
    if asset_in_base:
        try:
            available_assets.remove(asset_in_base)
        except ValueError:
            pass

    random_asset = random.choice(available_assets)

    return random_asset
