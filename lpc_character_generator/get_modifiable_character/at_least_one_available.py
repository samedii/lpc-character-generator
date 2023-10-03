from lpc_character_generator.constants import Asset, Action
from lpc_character_generator.general_utilities import get_path_to_asset_type
from lpc_character_generator.get_random_character.has_action import has_action
from lpc_character_generator.get_random_character.has_subtype import has_subtype


def at_least_one_available(sex, asset_type, action):
    path_to_assets = get_path_to_asset_type(sex, asset_type)

    if has_subtype(path_to_assets):
        return any(
            has_action(action, subtype_path)
            for subtype_path in path_to_assets.iterdir()
        )

    return has_action(action, path_to_assets)
