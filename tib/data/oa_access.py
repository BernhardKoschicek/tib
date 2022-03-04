from tib.models_org.entity import Entity
from tib.util.api_calls import view_class


def get_actors():
    data = [Entity(entry['features'][0])
            for entry in view_class(
            'actor?limit=9999999&show=none&search={"typeID":[{"operator":"equal","values":[9962]}]}')]
    return data
