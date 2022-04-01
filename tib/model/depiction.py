from typing import Any, Dict


class Depiction:
    def __init__(self, data: Dict[str, Any]):
        self.link = data['@id']
        self.title = data['title']
        self.license = data['license']
        self.url = data['url']
