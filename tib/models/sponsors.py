from typing import List

from tib.models.entity import get_basic_data, get_relation_to_by_system_class
from tib.util.api_calls import api_call, typed_entities_all_results


def get_sponsors(id_):
    return [get_sponsor_entity(sponsor['features'][0]) for sponsor in typed_entities_all_results(id_)]

def get_sponsor_entity(data):
    entity = get_basic_data(data)
    entity['website'] = api_call(get_relation_to_by_system_class(data['relations'], 'external_reference')[0])['properties']['title']
    return entity
