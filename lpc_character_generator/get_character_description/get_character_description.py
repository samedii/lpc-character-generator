import random

from itertools import permutations
from lpc_character_generator.constants import Sex, Asset

from .arrange_sentences import arrange_sentences
from .get_with_description import get_with_description
from .get_holdable_description import get_holdable_description


def get_character_description(sex: Sex, characteristics: dict) -> str:
    body_characteristics = characteristics[Asset.HEAD]
    age, color = body_characteristics["name"], body_characteristics["color"]
    base_description = f"{color} skinned {age} {sex.value}"
    general_description = get_with_description(characteristics)
    holdable_description = get_holdable_description(characteristics)

    sentence_permutations = list(
        permutations([general_description, holdable_description])
    )
    chosen_arrangement = list(random.choice(sentence_permutations))
    final_sentence = arrange_sentences([base_description] + chosen_arrangement)

    return final_sentence.lower()
