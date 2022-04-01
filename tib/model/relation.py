from typing import Any, Dict


class Relation:
    def __init__(self, data: Dict[str, Any]):
        self.label = data['label']
        self.relation_to = data['relationTo']
        self.relation_type = data['relationType']
        self.relation_system_class = data['relationSystemClass']
        self.type = data['type']
