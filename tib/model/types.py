from typing import Any, Dict


class Types:
    def __init__(self, data: Dict[str, Any]):
        self.label = data['label']
        self.hierarchy = data['hierarchy']
        self.value = data['value']
        self.unit = data['unit']
        self.identifier = data['identifier'].rsplit('/', 1)[-1]
        self.root = self.hierarchy.split('>')[0].rstrip()
