from typing import Any

from flask import render_template

from tib import app
from tib.model.entity import Entity
from tib.model.types import Types


@app.route('/entity/<id_>')
def entity_view(id_: int) -> str:
    entity = Entity.get_entity_from_oa(id_)
    type_hierarchy = get_types_sorted(entity.types)
    return render_template(
        'openatlas/entity_view.html',
        entity=entity,
        type_hierarchy=type_hierarchy)

def get_types_sorted(types: list[Types]) -> dict[str, Any]:
    type_hierarchy = {}
    for type_ in types:
        type_hierarchy.setdefault(type_.root, []).append(type_.label)
    return type_hierarchy