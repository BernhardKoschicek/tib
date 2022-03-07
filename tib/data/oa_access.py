from typing import Optional

from tib.models_org.entity import Entity
from tib.util.api_calls import api_call, get_entity, get_view_class

view_classes = ['actor', 'place', 'event', 'source', 'reference', 'artifact']


def get_data_from_oa(call: str) -> Optional[list[Entity]]:
    print(call)
    if call in view_classes:
        return get_oa_by_view_class(call)
    return None


def get_oa_by_view_class(view) -> list[Entity]:
    data = [Entity(entry['features'][0])
            for entry in get_view_class(
            f'{view}?limit=9999&'
            'show=none&search={"typeID":[{"operator":"equal","values":[9962]}]}')]
    return data


def get_entity_from_oa(id_: int) -> Entity:
    return Entity(get_entity(id_))
