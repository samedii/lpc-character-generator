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

            # if one asset of the subtype has the action, assume all of them do
            first_asset = next(
                (asset for asset in subtype_path.iterdir() if asset.stem != "_Behind"),
                None,
            )
            if first_asset and has_action(action, first_asset):
                last_directories.extend(
                    (asset, f"{subtype_path.stem} {asset.stem}")
                    for asset in subtype_path.iterdir()
                    if asset.stem != "_Behind"
                )
    else:
        first_asset = next(
            (asset for asset in path_to_assets.iterdir() if asset.stem != "_Behind"),
            None,
        )
        if first_asset and has_action(action, first_asset):
            last_directories = [
                (path, f"{path.stem}")
                for path in path_to_assets.iterdir()
                if path.stem != "_Behind" and has_action(action, path)
            ]  # This is a temporary solution

    return last_directories
