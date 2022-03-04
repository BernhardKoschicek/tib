from typing import Any, Dict



class Relation:
    def __init__(self, data: Dict[str, Any]):
        self.label = data['label']
        self.relationTo = data['relationTo']
        self.relationType = data['relationType']
        self.relationSystemClass = data['relationSystemClass']
        self.type = data['type']

