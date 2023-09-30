from lpc_character_generator.constants import Sex, Asset, Action
from lpc_character_generator.general_utilities import get_path_to_asset_type

from .has_action import has_action
from .has_subtype import has_subtype


def get_available_assets(
    sex: Sex, asset_type: Asset, action: Action, allowed_subtype: str = None
):
    path_to_assets = get_path_to_asset_type(sex, asset_type)
    last_directories = []

    if has_subtype(path_to_assets):
        for subtype_path in path_to_assets.iterdir():
            if not subtype_path.is_dir() or (
                allowed_subtype is not None and subtype_path.stem == allowed_subtype
            ):
                continue

            if has_action(action, subtype_path):
                last_directories.extend(
                    f"{subtype_path.stem} {asset.stem}"
                    for asset in subtype_path.iterdir()
                    if asset.stem != "_Behind"
                )
    else:
        if has_action(action, path_to_assets):
            last_directories = [
                f"{path.stem}"
                for path in path_to_assets.iterdir()
                if path.stem != "_Behind"
            ]

    return last_directories
