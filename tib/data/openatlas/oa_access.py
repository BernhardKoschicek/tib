from typing import List

from tib.model.entity import Entity
from tib.util.api_calls import get_view_class

from flask_babel import lazy_gettext as _l

view_classes = {
    'actor': {
        'display_name': _l('Actors'),
        'description': _l('Persons and Groups')},
    'place': {
        'display_name': _l('Places'),
        'description': _l('Physical places and their locations')},
    'event': {
        'display_name': _l('Events'),
        'description': _l('Linking places and actors')},
    'source': {
        'display_name': _l('Sources'),
        'description': _l('Documents, manuscripts, etc.')},
    'reference': {
        'display_name': _l('References'),
        'description': _l('Research literature')},
    'artifact': {
        'display_name': _l('Artefacts'),
        'description': _l('Physical objects')}}


def get_oa_by_view_class(view: str, project_id: object) -> List[Entity]:
    print(project_id)
    if view not in view_classes:
        return []
    data = [Entity(entry['features'][0])
            for entry in get_view_class(
            f'{view}?limit=0&'
            f'show=description&search='
            '{"typeID":[{"operator":"equal",'
            f'"values":[{project_id}]'
            '}]}')]

    return data
