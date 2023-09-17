from PIL import Image
from lpc_character_generator.image_utilities import add_asset
from lpc_character_generator.constants import (
    Sex,
    Action,
    Direction,
    Asset,
    PUT_ON_ORDER,
)

from .get_asset import get_asset
from .extract_frames import extract_frames


def get_character(
    sex: Sex,
    action: Action,
    body: str,
    direction: Direction = None,
    rotation_column: int = None,
    hair: str = None,
    neck: str = None,
    head: str = None,
    eyes: str = None,
    wings: str = None,
    shirt: str = None,
    pants: str = None,
    shoes: str = None,
    socks: str = None,
    sword: str = None,
    eyebrows: str = None,
    over_shirt: str = None,
    facial_hair: str = None,
    shield_base: str = None,
    shield_trim: str = None,
    shield_paint: str = None,
    shield_pattern: str = None,
    head_accessory: str = None,
) -> list[Image.Image]:
    asset_type_to_value = {
        Asset.BODY: body,
        Asset.HAIR: hair,
        Asset.NECK: neck,
        Asset.HEAD: head,
        Asset.EYES: eyes,
        Asset.WINGS: wings,
        Asset.SHIRT: shirt,
        Asset.PANTS: pants,
        Asset.SHOES: shoes,
        Asset.SOCKS: socks,
        Asset.SWORD: sword,
        Asset.EYEBROWS: eyebrows,
        Asset.OVER_SHIRT: over_shirt,
        Asset.FACIAL_HAIR: facial_hair,
        Asset.SHIELD_BASE: shield_base,
        Asset.SHIELD_TRIM: shield_trim,
        Asset.SHIELD_PAINT: shield_paint,
        Asset.SHIELD_PATTERN: shield_pattern,
        Asset.HEAD_ACCESSORY: head_accessory,
    }

    final_asset = None
    for asset_type in PUT_ON_ORDER:
        asset_name = asset_type_to_value[asset_type]

        if asset_name is None:
            continue

        asset_front, asset_behind = get_asset(sex, action, asset_type, asset_name)

        if not final_asset:
            final_asset = asset_front
            continue

        if asset_behind is not None:
            final_asset = add_asset(asset_behind, final_asset)

        final_asset = add_asset(final_asset, asset_front)

    final_frames = extract_frames(action, direction, rotation_column, final_asset)

    return final_frames
