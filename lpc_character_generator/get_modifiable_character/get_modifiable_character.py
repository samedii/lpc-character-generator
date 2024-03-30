import random

from .get_new_asset import get_new_asset
from .get_item_icon import get_item_icon
from .get_asset_args import get_asset_args
from .get_new_asset_type import get_new_asset_type
from .get_asset_description import get_asset_description

from lpc_character_generator.constants import Direction, ClothingState
from lpc_character_generator.get_character import get_character
from lpc_character_generator.get_random_character import get_random_character


def get_modifiable_character(
    clothing_state: ClothingState = None, direction: Direction = None
) -> dict:
    clothing_state = (
        clothing_state
        if clothing_state is not None
        else random.choice(list(ClothingState))
    )

    # generate base character
    args = get_asset_args(clothing_state)
    base_character = get_random_character(
        for_rotation_groups=False, direction=direction, **args
    )
    base_settings = base_character["settings"]
    sex = base_settings["sex"]
    base_frames = base_character["animation"]

    # generate new character with an additional item
    new_asset_type = get_new_asset_type(base_settings)
    new_asset = get_new_asset(base_settings, new_asset_type)
    base_settings[new_asset_type] = new_asset
    new_frames = get_character(**base_settings)

    # get item description
    asset_description = get_asset_description(new_asset)

    # return a random frame from the generated stuff
    frame_index = random.randint(0, len(base_frames) - 1)

    result = {
        "Base Character": base_frames[frame_index],
        "New Character": new_frames[frame_index],
        "Item Image": get_item_icon(sex, new_asset, new_asset_type),
        "Item Description": asset_description,
    }

    return result
