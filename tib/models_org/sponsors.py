from typing import Any, Dict

from tib.models_org.entity import Entity
from tib.util.api_calls import api_call, typed_entities_all_results


class Sponsors(Entity):
    def __init__(self, data: Dict[str, Any]):
        super().__init__(data)
        self.website = api_call(
            Entity.get_relation_to_by_system_class(
                data['relations'],
                'external_reference')[0])['properties']['title']

    @staticmethod
    def get_sponsors(id_):
        return [Sponsors(sponsor['features'][0]) for sponsor in
                typed_entities_all_results(id_)]

# def get_sponsor_entity(data):
#     entity = get_basic_data(data)
#     entity['website'] = api_call(get_relation_to_by_system_class(data['relations'], 'external_reference')[0])['properties']['title']
#     return entity
