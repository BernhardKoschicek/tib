from typing import Any


def get_subtypes(data: dict):
    return [i['label'] for i in data['features'][0]['relations']]


def uc_first(string):
    return str(string)[0].upper() + str(string)[1:] if string else ''


def get_prev_and_next_item_of_dict(key: str, dict_: dict[Any, Any]) -> tuple[
    Any, Any]:
    list_of_dict = list(dict_)
    index = list_of_dict.index(key)
    prev = list_of_dict[-1] if index == 1 else list_of_dict[(index - 1)]
    next = list_of_dict[0] if index == len(list_of_dict) - 1 else list_of_dict[
        (index + 1)]
    return prev, next
