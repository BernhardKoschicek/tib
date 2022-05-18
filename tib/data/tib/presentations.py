from datetime import datetime
from typing import Dict, List, Union


def get_presentations(
        categories: Union[str, List[str]]) -> List[Dict[str, str]]:
    categories = [categories] if type(categories) == str else categories
    return [presentation for presentation in presentations
            if any(item in categories for item in presentation['category'])]


presentations = [{
    "presenter": "Mihailo St. Popović",
    "title": "Historical Geography, Digital Humanities and Database Systems: an Approach to reconstruct “Sacred Landscapes” – the Case of Medieval Duklja and Raška (today’s Montenegro and Serbia)",
    "conference": "Global Eurasia, Workshop II: Handlungsspielräume, Netzwerke und transregionale Kontexte",
    "date": datetime(2022, 5, 12).strftime('%d/%m/%Y'),
    'location': 'Wien',
    "category": ["holdura"]
}, {
    "presenter": "Mihailo St. Popović",
    "title": "On the Use and Usefulness of Digital Humanities in the Historical Geography of Byzantium",
    "conference": "Seminar Series: The Balkans Between Empires, Aristotle University of Thessaloniki, Ibn Haldun University Istanbul",
    "date": datetime(2022, 4, 1).strftime('%d/%m/%Y'),
    'location': 'Thessaloniki',
    "category": ["holdura"]
}, {
    "presenter": "Markus Breier",
    "title": "Beyond East and West – Geocommunicating Historical Sacred Landscapes ",
    "conference": "International Medieval Congress, University of Leeds",
    "date": datetime(2021, 7, 7).strftime('%d/%m/%Y'),
    'location': 'Leeds',
    "category": ["holdura"]
}, {
    "presenter": "Markus Breier, Karel Kriz, Lukas Neugebauer, Alexander Pucher",
    "title": "Beyond East and West – Geocommunicating Historical Sacred Landscapes ",
    "conference": "30th International Cartographic Conference 2021",
    "date": datetime(2021, 12, 18).strftime('%d/%m/%Y'),
    'location': 'Florenz',
    "category": ["holdura"]
}]
