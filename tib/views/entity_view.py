from typing import Any, Dict, List

from flask import render_template
import numpy
from tib import app
from tib.model.entity import Entity, Relation
from tib.model.types import Types


@app.route('/entity/<id_>')
def entity_view(id_: int) -> str:
    entity = Entity.get_entity_from_oa(id_)
    type_hierarchy = get_types_sorted(entity.types)
    relations = get_relations(entity.relations)
    return render_template(
        'openatlas/entity_view.html',
        entity=entity,
        type_hierarchy=type_hierarchy,
        images=numpy.array_split(entity.depictions, 4)
        if entity.depictions else None,
        relations=relations
    )


def get_types_sorted(types: List[Types]) -> Dict[str, Any]:
    type_hierarchy = {}
    for type_ in types:
        type_hierarchy.setdefault(type_.root, []).append(type_.label)
    return type_hierarchy


def get_relations(relations: List[Relation]) -> Dict[str, List[Relation]]:
    relation_dict = {}
    for relation in relations:
        if relation.relation_system_class in \
                ['type', 'file', 'appellation', 'object_location']:
            continue
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


