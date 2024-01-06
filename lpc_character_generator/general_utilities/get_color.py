import random


def get_color(seed):
    random.seed(seed)
    random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))

    return random_color
