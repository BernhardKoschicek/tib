from typing import Optional

from tib.models_org.entity import Entity
from tib.util.api_calls import get_entity, get_view_class

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



def get_oa_by_view_class(view: str, project_id: int) -> list[Entity]:
    if view not in view_classes:
        return []
    data = [Entity(entry['features'][0])
            for entry in get_view_class(
            f'{view}?limit=9999&'
            f'show=none&search='
            '{"typeID":[{"operator":"equal",'
            f'"values":[{project_id}]'
            '}]}')]
    return data


def get_entity_from_oa(id_: int) -> Entity:
    return Entity(get_entity(id_))
