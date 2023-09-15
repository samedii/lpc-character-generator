from lpc_character_generator.constants import CONFLICTING_ASSETS, Asset


def assets_conflict(included_assets: dict, asset: Asset) -> bool:
    if asset not in CONFLICTING_ASSETS:
        return False

    conflicting_assets = CONFLICTING_ASSETS[asset]
    conflict_results = [
        second_asset in included_assets for second_asset in conflicting_assets
    ]

    return any(conflict_results)
