import random

from .assemble_list_string import assemble_list_string

from lpc_character_generator.constants import WITH_ASSETS, MAX_ITEMS


def get_with_description(characteristics: dict) -> str:
    drop_probability = 0.2

    if random.random() < drop_probability:
        return ""

    item_list = []
    next_probability = 1
    items_to_iterate = WITH_ASSETS.copy()
    random.shuffle(items_to_iterate)

    for asset_type in items_to_iterate:
        item_description = characteristics.get(asset_type, None)

        if item_description is None:
            continue

        name, color = item_description["name"], item_description["color"]
        # pick an item with some probability as long as the list isn't over the limit
        if random.random() < next_probability and len(item_list) < MAX_ITEMS:
            item_list.append((name, color))
            next_probability *= 0.1

    return "" if len(item_list) == 0 else " with" + assemble_list_string(item_list)
