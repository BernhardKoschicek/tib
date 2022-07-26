from typing import Any


class TypeTree:
    def __init__(self, data: dict[str, Any]):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.origin_id = data['origin_id']
        self.first = data['first']
        self.last = data['last']
        self.root = data['root']
        self.subs = data['subs']
        self.count = data['count']
        self.count_subs = data['count_subs']
        self.category = data['category']
