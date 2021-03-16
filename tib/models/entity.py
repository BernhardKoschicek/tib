class Entity:

    @staticmethod
    def get_entity(data):

        entity = {
            'name': data['properties']['title'],
            'description': Entity.get_description(data['description'])
        }
        return entity

    @staticmethod
    def get_description(desc):
        if not desc:
            return None
        desc = [i['value'] for i in desc]
        return desc[0]
