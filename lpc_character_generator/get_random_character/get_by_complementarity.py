from .get_available_assets import get_available_assets

from lpc_character_generator.constants import Sex, Action, Asset, ASSET_COMPLEMENTARITY


def get_by_complementarity(
    sex: Sex, action: Action, asset: Asset, included_assets: dict
):
    prerequisite_type, subtypes = ASSET_COMPLEMENTARITY[asset]

    # if prerequisite is not present
    if prerequisite_type not in included_assets:
        return []

    # if prerequisite is present, but doesn't have subtype requirements
    if not subtypes:
        return get_available_assets(sex, asset, action)

    # if prerequisite has subtype requirements
    prerequisite_value = included_assets[prerequisite_type].split()[0]
    if prerequisite_value not in subtypes:
        return []

    return get_available_assets(sex, asset, action, prerequisite_value)
