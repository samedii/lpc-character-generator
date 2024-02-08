import json

from lpc_character_generator.constants import PATH_TO_COLOR_NAMES


def get_item_characteristics(item_name: str) -> dict:
    color_dict = json.load(open(PATH_TO_COLOR_NAMES))
    split_value = item_name.split()
    custom_color = split_value[-1]
    converted_color = color_dict.get(custom_color, custom_color)

    characteristics = {
        "color": converted_color,
        "name": " ".join(split_value[:-1]),
    }

    return characteristics
