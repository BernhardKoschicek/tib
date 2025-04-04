from typing import Optional


def split_date_string(data: Optional[str]) -> Optional[str]:
    return '.'.join(map(str, data.split('T')[0].split('-')[::-1])) \
        if data else ''


def format_date(date_from: str, date_to: str) -> str:
    return f'between {date_from} and {date_to}' if date_to else date_from

