from collections import defaultdict
from typing import Any, Dict

from tib.models_org.entity import Entity
from tib.util.api_calls import system_class_results


class Team(Entity):
    def __init__(self, data: Dict[str, Any]):
        super().__init__(data)
        self.titles = self.get_type_label_by_hierarchy(data['types'], 'Title')
        self.current_employment = self.get_type_label_by_hierarchy(
            data['types'], 'Current Employment')
        self.projects = self.get_type_label_by_hierarchy(data['types'], 'Project')
        self.category = self.get_type_label_by_hierarchy(
            data['types'], 'Actor Category')

    @staticmethod
    def get_team_categorized():
        team = defaultdict(list)
        for e in Team.get_team_members():
            if not e.category:
                continue
            team[e.category[0]].append(e)
        return team

    @staticmethod
    def get_team_members():
        return [Team(i['features'][0]) for i in
                system_class_results('person')]
#
#
# def get_member(data):
#     entity = get_basic_data(data)
#     entity['titles'] = get_type_label_by_hierarchy(data['types'], 'Title')
#     entity['current_employment'] = get_type_label_by_hierarchy(
#         data['types'],
#         'Current Employment')
#     entity['projects'] = get_type_label_by_hierarchy(data['types'], 'Project')
#     entity['category'] = get_type_label_by_hierarchy(
#         data['types'],
#         'Actor Category')
#     return entity
