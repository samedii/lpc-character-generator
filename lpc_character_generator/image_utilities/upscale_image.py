from PIL import Image


def upscale_image(image: Image, scale_factor: int):
    original_width, original_height = image.size
    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)

    rescaled_image = image.resize((new_width, new_height), Image.NEAREST)

    return rescaled_image
