from pathlib import Path
from lpc_character_generator.constants import (
    ASSET_TO_FILENAME,
    SHARED_ASSETS,
    PATH_TO_DATA,
    Sex,
    Asset,
)


def get_path_to_asset_type(sex: Sex, asset_type: Asset) -> Path:
    is_shared = asset_type in SHARED_ASSETS
    base_path = PATH_TO_DATA / "Shared" if is_shared else PATH_TO_DATA / sex.value
    final_path = base_path / ASSET_TO_FILENAME[asset_type]

    return final_path
