from pathlib import Path
from lpc_character_generator.constants import Action, ACTION_TO_FILENAME


def has_action(action: Action, path_to_assets: Path) -> bool:
    # if one asset of the asset colors has the action, assume all of them do
    first_asset = None
    for asset_path in path_to_assets.iterdir():
        if asset_path.stem != "_Behind":
            first_asset = asset_path
            break

    file_stem_name = ACTION_TO_FILENAME[action]
    potential_path = first_asset / f"{file_stem_name}.webp"

    return potential_path.exists()
