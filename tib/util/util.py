from typing import Any, Dict, List, Tuple


def get_subtypes(data: Dict) -> List[Any]:
    return [i['label'] for i in data['features'][0]['relations']]


def uc_first(string: str) -> str:
    return str(string)[0].upper() + str(string)[1:] if string else ''


def get_prev_and_next_item_of_dict(
        key: str,
        dict_: Dict[Any, Any]) -> Tuple[Any, Any]:
    list_of_dict = list(dict_)
    index = list_of_dict.index(key)
    prev = list_of_dict[-1] if index == 0 else list_of_dict[(index - 1)]
    next_ = list_of_dict[0] if index == len(list_of_dict) - 1 \
        else list_of_dict[(index + 1)]
    return prev, next_
