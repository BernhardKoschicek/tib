class Entity:

    @staticmethod
    def get_entity(data):

        entity = {
            'name': data['properties']['title'],
            'description': Entity.get_description(data['description']),
            'titles': Entity.get_type_label_by_hierarchy(data['types'], 'Title'),
            'profile_image': Entity.get_profile_depiction(data['depictions']),
            'current_employment': Entity.get_type_label_by_hierarchy(data['types'],
                                                                     'Current Employment'),
            'projects': Entity.get_type_label_by_hierarchy(data['types'], 'Project')
        }
        return entity

    @staticmethod
    def get_description(data):
        if not data:
            return None
        desc = [i['value'] for i in data]
        return desc[0]

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
