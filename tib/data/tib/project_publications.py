from typing import Dict, List, Union

def get_project_publication(
        categories: Union[str, List[str]]) -> List[Dict[str, str]]:
    categories = [categories] if type(categories) == str else categories
    return [publications for publications in project_publications
            if any(item in categories for item in publications['category'])]


project_publications = [{
    "author": "A. Bracanović, M. Breier, M. Hernández Cordero u. a.",
    "title": "On the Crossroads between East and West: Geocommunicating Medieval Sacred Landscapes in Today’s Montenegro – First Project Results. ",
    "location": "Krems",
    "date": "TBA",
    "pages": "",
    "category": ['holdura']
}]
