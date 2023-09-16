from PIL import Image
from pathlib import Path
from typing import Optional


def fetch_behind(root_path: Path, color, file_ending) -> Optional[Image.Image]:
    path_to_behind = root_path / "_Behind" / color / file_ending

    if path_to_behind.exists():
        return Image.open(path_to_behind)

    return None
