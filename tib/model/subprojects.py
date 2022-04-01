from typing import Any, Dict

from tib.model.entity import Entity
from tib.model.team import Team
from tib.util.api_calls import api_call, get_typed_entities_all_results


class Subprojects(Entity):
    def __init__(self, data: Dict[str, Any]):
        super().__init__(data)
        self.sponsors = self.get_relation_label_by_type(
            data['relations'], 'Sponsor')
        self.project = self.get_type_label_by_hierarchy(
            data['types'], 'Project')
        self.project_team = self.get_project_team()

    def get_project_team(self):
        member_links = [entry.relation_to for entry in self.relations
                        if entry.relation_system_class == "person"]
        # Todo: Call dauert zu lange, lieber einen einzelnen call
        #  machen, also query?
        return [Team(api_call(link)) for link in member_links]

    @staticmethod
    def get_subprojects(id_: int):
        return [Subprojects(project['features'][0]) for project in
                get_typed_entities_all_results(id_)]
