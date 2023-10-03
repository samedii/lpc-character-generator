import random
from PIL import Image

from lpc_character_generator.constants import Sex, Asset, SHARED_ASSETS, PATH_TO_ICONS


def get_item_icon(sex: Sex, item_name: str, asset_type: Asset) -> Image.Image:
    is_shared = asset_type in SHARED_ASSETS
    base_path = PATH_TO_ICONS / "Shared" if is_shared else PATH_TO_ICONS / sex.value
    path_to_icons = base_path / item_name

    icon_path_list = list(path_to_icons.iterdir())
    random_icon_path = random.choice(icon_path_list)
    icon = Image.open(random_icon_path)

    return icon
