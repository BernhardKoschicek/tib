from typing import List

import requests

from tib import app
from tib.model.typetree import TypeTree


def get_view_class(parameter: str):
    url = f"{app.config['API_PATH']}/view_class/"
    return requests.get(f"{url}{parameter}").json()['results']


def system_class_results(parameter: str):
    url = f"{app.config['API_PATH']}/system_class/"
    return requests.get(f"{url}{parameter}").json()['results']


def get_typed_entities_all_results(id_: int):
    url = f"{app.config['API_PATH']}/type_entities_all/"
    return requests.get(f"{url}{id_}").json()['results']


def get_type_tree() -> List[TypeTree]:
    url = f"{app.config['API_PATH']}/type_tree/"
    type_tree = requests.get(url).json()['typeTree']
    return [TypeTree(types) for types in type_tree.values()]


def get_entity(id_: int):
    url = f"{app.config['API_PATH']}/entity/"
    return requests.get(f"{url}{id_}").json()['features'][0]


def api_call(url):
    return requests.get(url).json()['features'][0]
