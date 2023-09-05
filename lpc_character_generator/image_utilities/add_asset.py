from PIL import Image


def add_asset(base_image: Image, asset_image: Image, starting_position: tuple = (0, 0)):
    base_copy = base_image.copy()
    base_copy.paste(asset_image, starting_position, asset_image)

    return base_copy
