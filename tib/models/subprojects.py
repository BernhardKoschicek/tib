from tib.models.entity import get_basic_data, get_relation_by_system_class, \
    get_relation_by_type
from tib.util.api_calls import typed_entities_all_results


def get_subprojects(id_: int):
    projects = []
    for project in typed_entities_all_results(id_):
        projects.append(get_project_details(project['features'][0]))
    return projects


def get_project_details(data):
    entity = get_basic_data(data)
    entity['sponsors'] = get_relation_by_type(data['relations'], 'Sponsor')
    entity['team'] = get_relation_by_system_class(data['relations'], 'person')
    print(entity)
    return entity


