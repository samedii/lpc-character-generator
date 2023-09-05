from PIL import Image
from lpc_character_generator.constants import (
    Sex,
    Action,
    Asset,
    PATH_TO_DATA,
    SHARED_ASSETS,
    ACTION_TO_FILENAME,
)


def get_asset(
    sex: Sex, action: Action, asset_type: Asset, asset_name: str
) -> Image.Image:
    file_ending = f"{ACTION_TO_FILENAME[action]}.png"
    is_shared = asset_type in SHARED_ASSETS
    split_name = asset_name.split()
    color = split_name.pop().capitalize()
    subtype = " ".join([word.capitalize() for word in split_name])

    base_path = PATH_TO_DATA / "Shared" if is_shared else PATH_TO_DATA / sex.value
    final_path = base_path / asset_type.value / subtype / color / file_ending

    asset = Image.open(final_path)

    return asset
