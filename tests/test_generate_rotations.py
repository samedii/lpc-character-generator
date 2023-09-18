from lpc_character_generator.generate import generate
from PIL import Image
import numpy as np


def test_generate_rotations():
    for _ in range(20):
        generate(do_rotation=True)
