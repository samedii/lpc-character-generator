def get_item_characteristics(item_name: str) -> dict:
    split_value = item_name.split()
    characteristics = {
        "color": split_value[-1],
        "name": " ".join(split_value[:-1]),
    }

    return characteristics
