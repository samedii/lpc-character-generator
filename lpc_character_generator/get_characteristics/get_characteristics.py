from lpc_character_generator.constants import Asset, NO_DESCRIPTION_ASSETS


def get_characteristics(settings: dict):
    asset_set = set(Asset)
    characteristics = {}

    for key, value in settings.items():
        if key not in asset_set or key in NO_DESCRIPTION_ASSETS:
            continue

        split_value = value.split()
        characteristics[key] = {
            "color": split_value[-1],
            "name": " ".join(split_value[:-1]),
        }

    return characteristics
