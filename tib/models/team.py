from tib.models.util import Util


class Team:

    @staticmethod
    def get_entity(data):

        entity = {
            'name': data['properties']['title'],
            #'description': Util.get_description(data['description']),
            'titles': Team.get_type_label_by_hierarchy(data['types'], 'Title'),
            'profile_image': Team.get_profile_depiction(data['depictions']),
            'current_employment': Team.get_type_label_by_hierarchy(data['types'],
                                                                     'Current Employment'),
            'projects': Team.get_type_label_by_hierarchy(data['types'], 'Project'),
            'category': Team.get_type_label_by_hierarchy(data['types'], 'Actor Category')
        }
        return entity

    @staticmethod
    def get_type_label_by_hierarchy(data, hierarchy):
        if not data:
            return None
        return [titles['label'] for titles in data if titles['hierarchy'] == hierarchy]
        # Problem: what is, if Title is changed? I have no ID to get by

    @staticmethod
    def get_profile_depiction(data):
        if not data:
            return None
        return [img['url'] for img in data if img['title'].startswith('profile_')]
