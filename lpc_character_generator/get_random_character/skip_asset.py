import random

from lpc_character_generator.general_utilities import get_path_to_asset_type
from lpc_character_generator.constants import (
    Sex,
    Asset,
    ProbabilityType,
    ASSET_SKIP_PROBABILITIES,
)


def skip_asset(sex: Sex, asset_type: Asset) -> bool:
    path_to_assets = get_path_to_asset_type(sex, asset_type)
    probability_type = ASSET_SKIP_PROBABILITIES.get(asset_type, ProbabilityType.DEFAULT)

    probability_threshold = 0

    if probability_type == ProbabilityType.DEFAULT:
        probability_threshold = 0.5
    elif ProbabilityType.UNIFORM:
        type_count = len(list(path_to_assets.iterdir())) + 1
        probability_threshold = 1 / type_count

    random_num = random.random()
    return random_num < probability_threshold
