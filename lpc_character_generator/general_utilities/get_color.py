import random


def get_color(seed):
    local_random = random.Random(seed)
    random_color = "#{:06x}".format(local_random.randint(0, 0xFFFFFF))

    return random_color
