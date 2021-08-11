import requests

from tib import app
from tib.models.entity import get_description, get_profile_depiction


def system_class_results(parameter: str):
    url = f"{app.config['API_PATH']}/system_class/"
    return requests.get(f"{url}{parameter}").json()['results']


def typed_entities_all_results(id_: int):
    url = f"{app.config['API_PATH']}/type_entities_all/"
    return requests.get(f"{url}{id_}").json()['results']

