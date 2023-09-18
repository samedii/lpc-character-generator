from lpc_character_generator.generate import generate


def test_generate_non_rotations():
    for _ in range(20):
        generate(do_rotation=False)
