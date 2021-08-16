from typing import Any, Dict

from tib.models.depiction import Depiction
from tib.models.relation import Relation



class Entity:
    def __init__(self, data: Dict[str, Any]):
        self.name = data['properties']['title']
        self.description = self.get_description(data['description'])
        self.profile_image = self.get_profile_depiction(data['depictions'])
        self.alias = data['names']
        self.begin = self.get_date(data['when']['timespans'], 'start')
        self.end = self.get_date(data['when']['timespans'], 'end')
        self.relations = self.get_relations(data['relations'])
        self.depictions = self.get_depiction(data['depictions'])

    # def get_basic_data(data):
    #     entity = {
    #         'name': data['properties']['title'],
    #         'description': get_description(data['description']),
    #         'profile_image': get_profile_depiction(data['depictions']),
    #         'alias': data['names'],
    #         'begin': get_date(data['when']['timespans'], 'start'),
    #         'end': get_date(data['when']['timespans'], 'end')
    #     }
    #     return entity

    @staticmethod
    def get_depiction(data):
        if not data:
            return None
        return [Depiction(depiction) for depiction in data]

    @staticmethod
    def get_relations(data):
        if not data:
            return None
        return [Relation(relation) for relation in data]

    @staticmethod
    def get_description(data):
        if not data:
            return None
        desc = [i['value'] for i in data]
        return desc[0]

    @staticmethod
    def get_profile_depiction(data):
        if not data:
            return None
        return \
        [img['url'] for img in data if img['title'].startswith('profile_')][0]

    @staticmethod
    def get_date(data, time):
        if not data:
            return None
        timestamp = [timespan[time]['earliest'] for timespan in data]
        return timestamp[0]

    @staticmethod
    def get_relation_label_by_type(data, type_):
        if not data:
            return None
        return [titles['label'] for titles in data if
                titles['type'] == type_]

    @staticmethod
    def get_relation_to_by_type(data, type_):
        if not data:
            return None
        return [titles['relationTo'] for titles in data if
                titles['type'] == type_]

    @staticmethod
    def get_relation_label_by_system_class(data, system_class):
        if not data:
            return None
        return [titles['label'] for titles in data if
                titles['relationSystemClass'] == system_class]

    @staticmethod
    def get_relation_to_by_system_class(data, system_class):
        if not data:
            return None
        return [titles['relationTo'] for titles in data if
                titles['relationSystemClass'] == system_class]

    @staticmethod
    def get_type_label_by_hierarchy(data, hierarchy):
        if not data:
            return None
        return [titles['label'] for titles in data if
                titles['hierarchy'] == hierarchy]
        # Problem: what is, if Title is changed? I have no ID to get by
