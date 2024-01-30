from PIL import Image, ImageDraw

from lpc_character_generator.general_utilities.get_color import get_color


def draw_points(image: Image, points: list[dict], scale_factor, dot_size=2):
    draw = ImageDraw.Draw(image)

    for point_dict in points:
        y = point_dict["y"] * scale_factor
        x = point_dict["x"] * scale_factor

        label_seed = point_dict["label"]
        random_color = get_color(label_seed)

        left_upper = (x - dot_size), (y - dot_size)
        right_lower = (x + dot_size), (y + dot_size)

        # draw.point((x, y), fill=random_color)
        draw.ellipse(
            (left_upper, right_lower),
            fill=random_color,
        )
