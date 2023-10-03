from lpc_character_generator.constants import Asset, ClothingState


def get_asset_args(clothing_state: ClothingState) -> dict:
    all_assets = set(list(Asset))
    additional_items = all_assets - {Asset.BODY}

    clothing_state_args = {
        ClothingState.NAKED: {"to_exclude": additional_items},
        ClothingState.F_CLOTHED: {"to_include": all_assets},
        ClothingState.P_CLOTHED: {"non_optional_assets": {Asset.BODY}},
    }

    return clothing_state_args[clothing_state]
