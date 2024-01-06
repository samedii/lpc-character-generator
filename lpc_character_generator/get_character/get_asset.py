from PIL import Image

from .fetch_behind import fetch_behind

from typing import Optional
from lpc_character_generator.general_utilities import get_path_to_asset_type
from lpc_character_generator.constants import (
    Sex,
    Action,
    Asset,
    ACTION_TO_FILENAME,
)


def get_asset(
    sex: Sex, action: Action, asset_type: Asset, asset_name: str
) -> tuple[Image.Image, Optional[Image.Image]]:
    file_ending = f"{ACTION_TO_FILENAME[action]}.png"
    split_name = asset_name.split()
    color = split_name.pop().capitalize()
    subtype = " ".join([word.capitalize() for word in split_name])

    path_to_subtype = get_path_to_asset_type(sex, asset_type) / subtype
    path_to_asset = path_to_subtype / color / file_ending

    behind = fetch_behind(path_to_subtype, color, file_ending)
    asset = Image.open(path_to_asset)

    return asset, behind
