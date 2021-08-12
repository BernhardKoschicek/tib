from tib.models.entity import get_basic_data, get_relation_label_by_type, \
    get_relation_to_by_type, \
    get_type_label_by_hierarchy
from tib.util.api_calls import typed_entities_all_results


def get_subprojects(id_: int):
    return [get_project_details(project['features'][0]) for project in typed_entities_all_results(id_)]


def get_project_details(data):
    entity = get_basic_data(data)
    entity['sponsors'] = get_relation_label_by_type(data['relations'], 'Sponsor')
    entity['project'] = get_type_label_by_hierarchy(data['types'], 'Project')
    return entity





