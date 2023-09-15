from pathlib import Path
from lpc_character_generator.constants import Action, ACTION_TO_FILENAME


def has_action(action: Action, path_to_asset: Path) -> bool:
    file_stem_name = ACTION_TO_FILENAME[action]
    potential_path = path_to_asset / f"{file_stem_name}.png"

    return potential_path.exists()
