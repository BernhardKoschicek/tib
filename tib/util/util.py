from typing import Dict


def get_subtypes(data: Dict):
    return [i['label'] for i in data['features'][0]['relations']]


def uc_first(string):
    return str(string)[0].upper() + str(string)[1:] if string else ''

