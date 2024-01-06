from pathlib import Path

from pathlib import Path


def has_subtype(path_to_asset: Path) -> bool:
    # exclude _Behind
    for directory in path_to_asset.iterdir():
        if directory.stem == "_Behind":
            continue

        # Check if there are asset images in the subdirectory
        if any(file.is_file() for file in directory.iterdir()):
            return False

    return True
