from datetime import datetime
from typing import Any, Dict, List, Tuple, Union


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


def get_dict_entries_by_category(
        categories: Union[List[str], str],
        list_: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    categories = [categories] if type(categories) == str else categories
    return [entry for entry in list_
            if any(item in categories for item in entry['category'])]


def get_table_dates_formatted(year: int, month: int, day: int) -> str:
    return datetime(year, month, day).strftime('%Y/%m/%d')


def get_news_dates_formatted(year: int, month: int, day: int) -> str:
    return datetime(year, month, day).strftime('%d %B %Y')


def get_dates_formatted(year: int, month: int, day: int) -> str:
    return datetime(year, month, day).strftime('%d.%m.%Y')


def format_link(link_: str) -> str:
    return f'<a href="{link_}" target=_blank>{link_}</a>'


def format_video_tag(src: str) -> str:
    return f"""
        <div class="col align-self-center text-center">
            <video preload loop muted autoplay controls>
                <source
                    src="/static/video/{src}"
                    type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>
        """


def format_link_text(link_: str, text: str) -> str:
    return f'<a href="{link_}" target=_blank>{text}</a>'


def youtube_iframe(link_: str) -> str:
    return '<iframe width="560" height="315" ' \
           f'src="{link_}" ' \
           'title="YouTube video  player" ' \
           'allow="accelerometer; autoplay; clipboard-write;  ' \
           'encrypted-media; gyroscope; picture-in-picture" ' \
           'allowfullscreen></iframe>'
