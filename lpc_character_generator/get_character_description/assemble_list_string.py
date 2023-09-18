def assemble_list_string(item_list: list) -> str:
    list_string = ""

    for i, asset in enumerate(item_list):
        if i != 0 and i == len(item_list) - 1:
            list_string += " and"
        elif i != 0:
            list_string += ","

        name, color = asset
        list_string += f" {color} {name}" if color is not None else f" {name}"

    return list_string
