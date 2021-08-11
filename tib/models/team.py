from collections import defaultdict

from tib.models.entity import get_basic_data, get_type_label_by_hierarchy
from tib.util.api_calls import system_class_results


def get_team():
    entity = []
    for i in system_class_results('person'):
        entity.append(get_team_member(i['features'][0]))
    team = defaultdict(list)
    for e in entity:
        team[e['category'][0]].append(e)
    return team


def get_team_member(data):
    entity = get_basic_data(data)
    entity['titles'] = get_type_label_by_hierarchy(data['types'], 'Title')
    entity['current_employment'] = get_type_label_by_hierarchy(
        data['types'],
        'Current Employment')
    entity['projects'] = get_type_label_by_hierarchy(data['types'], 'Project')
    entity['category'] = get_type_label_by_hierarchy(
        data['types'],
        'Actor Category')
    return entity


