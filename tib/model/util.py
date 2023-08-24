from typing import Optional, Any


def split_date_string(data: Optional[str]) -> Optional[str]:
    return '.'.join(map(str, data.split('T')[0].split('-')[::-1])) \
        if data else ''


def format_date(date_from: str, date_to: str) -> str:
    return f'between {date_from} and {date_to}' if date_to else date_from


def flatten_list_and_remove_duplicates(list_: list[Any]) -> list[Any]:
    return [item for sublist in list_ for item in sublist if item not in list_]
