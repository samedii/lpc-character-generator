import json

from .draw_points import draw_points

from PIL import Image, ImageDraw
from lpc_character_generator.constants import Direction, PATH_TO_EDGES


def draw_edges(
    image: Image, points: list[dict], direction: Direction, scale_factor: int
):
    draw = ImageDraw.Draw(image)
    edge_configs = json.load(open(PATH_TO_EDGES))[direction.value]
    point_dict = {point["label"]: point for point in points}
    points_ordered = []

    for edge in edge_configs:
        start_node, end_node = point_dict[edge[0]], point_dict[edge[1]]

        if start_node not in points_ordered:
            points_ordered.append(start_node)

        if end_node not in points_ordered:
            points_ordered.append(end_node)

    edge_coordinates = [
        (
            point_dict[edge[0]]["x"] * scale_factor,
            point_dict[edge[0]]["y"] * scale_factor,
            point_dict[edge[1]]["x"] * scale_factor,
            point_dict[edge[1]]["y"] * scale_factor,
        )
        for edge in edge_configs
    ]

    for i, edge in enumerate(edge_coordinates):
        draw.line(edge, fill="black", width=2)

    draw_points(image, points_ordered, scale_factor)
