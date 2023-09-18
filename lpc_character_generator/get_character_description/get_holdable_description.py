import random
from lpc_character_generator.constants import Asset


def get_holdable_description(characteristics: dict) -> str:
    drop_probability = 0.2

    if random.random() < drop_probability:
        return ""

    sword_description = characteristics.get(Asset.SWORD, None)

    if sword_description is None:
        return ""

    name, color = sword_description["name"], sword_description["color"]
    return f" holding {color} {name}"
