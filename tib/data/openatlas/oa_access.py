from typing import List

from tib.model.entity import Entity
from tib.util.api_calls import get_view_class

view_classes = {
    'actor': {
        'display_name': 'Akteure',
        'description': 'Personen und Gruppen'},
    'place': {
        'display_name': 'Orte',
        'description': 'Physische Orte und deren Lokation'},
    'event': {
        'display_name': 'Ereignisse',
        'description': 'Verknüpfung von Ort und Akteur'},
    'source': {
        'display_name': 'Quellen',
        'description': 'Inhalt von Manuskripten'},
    'reference': {
        'display_name': 'Referenzen',
        'description': 'Forschungsliteratur'},
    'artifact': {
        'display_name': 'Artefakte',
        'description': 'Physische Objekte'}}


def get_oa_by_view_class(view: str, project_id: object) -> List[Entity]:
    if view not in view_classes:
        return []
    data = [Entity(entry['features'][0])
            for entry in get_view_class(
            f'{view}?limit=0&'
            f'show=none&search='
            '{"typeID":[{"operator":"equal",'
            f'"values":[{project_id}]'
            '}]}')]
    return data


