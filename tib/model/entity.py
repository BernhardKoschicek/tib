import os
from typing import Any, Dict, List, Optional

from tib.model.types import Types
from tib.model.util import split_date_string, format_date
from tib.util.api_calls import get_entity
from tib.util.util import uc_first


class Entity:
    def __init__(self, data: Dict[str, Any]) -> None:
        self.id_ = data['@id'].rsplit('/', 1)[-1]
        self.name = data['properties']['title']
        self.description = self.get_description(data['descriptions'])
        self.system_class = uc_first(data['systemClass'].replace('_', ' '))
        self.types = self.get_types(data['types']) if 'types' in data else None
        self.alias = self.get_alias(data['names']) if 'names' in data else None
        self.relations = data['relations'] if 'relations' in data else None
        self.depictions = self.get_depiction(data['depictions']) \
            if 'depictions' in data else None
        self.links = data['links'] if 'links' in data else None
        self.begin_from = None
        self.begin_to = None
        self.begin_comment = None
        self.end_from = None
        self.end_to = None
        self.begin = None
        self.end = None
        self.geometry = self.handling_geometry(data)
        if 'when' in data:
            self.begin_from = split_date_string(
                data['when']['timespans'][0]['start']['earliest'])
            self.begin_to = split_date_string(
                data['when']['timespans'][0]['start']['latest'])
            self.end_from = split_date_string(
                data['when']['timespans'][0]['end']['earliest'])
            self.end_to = split_date_string(
                data['when']['timespans'][0]['end']['latest'])
            self.begin = format_date(self.begin_from, self.begin_to)
            self.end = format_date(self.end_from, self.end_to)

    @staticmethod
    def get_entity_from_oa(id_: int):
        return Entity(get_entity(id_))

    @staticmethod
    def get_alias(data: List[Dict[str, str]]) -> str:
        return ', '.join(map(str, [alias['alias'] for alias in data])) \
            if data else ''

    @staticmethod
    def get_types(data):
        if not data:
            return None
        return [Types(types) for types in data]

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
    def handling_geometry(
            data: dict[str, Any]) -> Optional[list[dict[str, Any]]]:
        if geometry := data.get('geometry'):
            if geometry['type'] == 'GeometryCollection':
                return geometry['geometries']
            else:
                return geometry
        return None


class Depiction:
    def __init__(self, data: Dict[str, Any]):
        self.link = data['@id']
        self.title = data['title']
        self.license = data['license']
        self.url = data['url']
        self.extension = os.path.splitext(self.url.rsplit('/', 1)[-1])[1]



class Relation(Entity):
    def __init__(self, data: Dict[str, Any]):
        super().__init__(data)
        self.label = data['label']
        self.relation_to_id = data['relationTo'].rsplit('/', 1)[-1]
        self.relation_to = data['relationTo']
        self.relation_type = data['relationType']
        self.relation_system_class = data['relationSystemClass']
        self.relation_description = data['relationDescription']
        self.type = data['type']
