from typing import Dict


class Util:

    @staticmethod
    def get_description(data):
        if not data:
            return None
        desc = [i['value'] for i in data]
        return desc[0]

    @staticmethod
    def get_subtypes(data: Dict):
        return [i['label'] for i in data['features'][0]['relations']]
