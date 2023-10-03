from .get_item_characteristics import get_item_characteristics

from lpc_character_generator.constants import Asset, NO_DESCRIPTION_ASSETS


def get_characteristics(settings: dict):
    asset_set = set(Asset)
    characteristics = {}

    for key, value in settings.items():
        if key not in asset_set or key in NO_DESCRIPTION_ASSETS:
            continue

        characteristics[key] = get_item_characteristics(value)

    return characteristics
