from pathlib import Path


def has_subtype(path_to_asset: Path) -> bool:
    directory = next(path_to_asset.iterdir())
    path_to_directory = path_to_asset / directory

    # if there are asset images in the subdirectory then it's not a type
    for file in path_to_directory.iterdir():
        if file.is_file():
            return False

    return True
