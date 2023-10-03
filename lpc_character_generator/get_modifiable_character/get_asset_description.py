from lpc_character_generator.get_characteristics import get_item_characteristics


def get_asset_description(item_name: str) -> str:
    characteristics = get_item_characteristics(item_name)
    description = f"{characteristics['color']} {characteristics['name']}"

    return description
