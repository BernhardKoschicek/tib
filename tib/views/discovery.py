from typing import Any, Dict, List, Optional

from flask import render_template
import numpy
from tib import app
from tib.data.openatlas.oa_access import get_oa_by_view_class, view_classes
from tib.data.openatlas.subprojects import subprojects_ger_discover
from tib.model.entity import Entity, Relation
from tib.model.types import Types
from tib.util.api_calls import get_entities_linked_to_entity


@app.route('/entity/<id_>')
def entity_view(id_: int) -> str:
    entity = Entity.get_entity_from_oa(id_)
    linked_entities = get_entities_linked_to_entity(id_)
    return render_template(
        'openatlas/entity_view.html',
        entity=entity,
        type_hierarchy=get_types_sorted(entity.types),
        images=numpy.array_split(entity.depictions, 4)
        if entity.depictions else None,
        relations=get_relations(
            get_relation_entities(linked_entities, entity.relations))
    )


def get_relation_entities(
        linked: List[Dict[str, Any]],
        relations: List[Dict[str, Any]]) -> List[Relation]:
    linked_entities = {}
    for entry in linked:
        linked_entities[entry['features'][0]['@id'].rsplit('/', 1)[-1]] = entry['features'][0]
    for relation in relations:
        linked_entities[relation['relationTo'].rsplit('/', 1)[-1]].update(relation)
    list_ = [value for value in linked_entities.values()]
    return [Relation(entity) for entity in list_]


def get_types_sorted(types: List[Types]) -> Optional[Dict[str, Any]]:
    if not types:
        return None
    type_hierarchy = {}
    for type_ in types:
        type_hierarchy.setdefault(type_.root, []).append(type_)
    return type_hierarchy


def get_relations(
        relations: List[Relation]) -> Dict[str, List[Relation]]:
    relation_dict = {}
    for relation in relations:
        if relation.relation_system_class in \
                ['file', 'appellation',
                 'object_location', 'reference_system']:
            continue
        elif relation.relation_system_class == 'type':
            relation_dict.setdefault('types', []).append(relation)
        elif relation.relation_system_class == 'source':
            relation_dict.setdefault('sources', []).append(relation)
        elif relation.relation_system_class == 'source_translation':
            relation_dict.setdefault('source_translations', []).append(relation)
        elif relation.relation_system_class in \
                ['place', 'feature', 'stratigraphic_unit']:
            relation_dict.setdefault('places', []).append(relation)
        elif relation.relation_system_class == 'administrative_unit':
            relation_dict.setdefault(
                'administrative_unit', []).append(relation)
        elif relation.relation_system_class in ['artifact', 'human_remains']:
            relation_dict.setdefault('artifacts', []).append(relation)
        elif relation.relation_system_class in \
                ['bibliography', 'edition', 'external_reference']:
            relation_dict.setdefault('references', []).append(relation)
        elif relation.relation_system_class in \
                ['acquisition', 'activity', 'event', 'move', 'production']:
            relation_dict.setdefault('events', []).append(relation)
        elif relation.relation_system_class in ['group', 'person']:
            relation_dict.setdefault('actors', []).append(relation)
        else:
            relation_dict.setdefault('others', []).append(relation)
    return relation_dict


@app.route('/digital/<project>/<view>')
def digital_oa_access(project: str, view: str) -> str:
    data = False
    try:
        data = get_oa_by_view_class(
                view,
                subprojects_ger_discover[project]['oaID'])
    except:
        pass
    return render_template(
            'openatlas/entity_table.html',
            data=data,
            project=subprojects_ger_discover[project],
            view_classes=view_classes[view])
