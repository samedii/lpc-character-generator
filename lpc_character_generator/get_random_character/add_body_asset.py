import random

from .get_available_assets import get_available_assets
from lpc_character_generator.constants import Sex, Asset, Action


def add_body_asset(included_assets: dict, sex: Sex, action: Action):
    head_options = list(get_available_assets(sex, Asset.HEAD, action))
    rand_head = random.choice(head_options)
    head_color = rand_head.split()[1]

    included_assets[Asset.HEAD] = rand_head
    included_assets[Asset.BODY] = head_color
