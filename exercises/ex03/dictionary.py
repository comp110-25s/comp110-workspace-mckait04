"""a program to practice some dictionary functions"""

__author__: str = "730560970"


def invert(dict_1: dict[str, str]) -> dict[str, str]:
    inverted_dict = {}

    for key in dict_1:
        value = dict_1[key]
        if value in inverted_dict:
            raise KeyError(f"Duplicate value: {value}")
        inverted_dict[value] = key

    return inverted_dict


def count(dict_2: list[str]) -> dict[str, int]:
    result = {}

    for item in dict_2:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def favorite_color(dict_3: dict[str, str]) -> str:
    color_list: dict[str, int] = {}

    for key in dict_3:
        if dict_3[key] in color_list:
            color_list[dict_3[key]] += 1
        else:
            color_list[dict_3[key]] = 1

    most_frequent_color: str = ""
    highest_count = 0

    for key in color_list:
        if color_list[key] > highest_count:
            most_frequent_color = key
            highest_count = color_list[key]

    return most_frequent_color


def bin_len(strings: list[str]) -> dict[int, set[str]]:
    length_dict = {}

    for key in strings:
        length = len(key)

        if length in length_dict:
            length_dict[length].add(key)
        else:
            length_dict[length] = {key}

    return length_dict
