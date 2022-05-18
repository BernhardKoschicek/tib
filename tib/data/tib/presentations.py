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
    "date": '12.5.2022',
    'location': 'Wien',
    "category": ["holdura"]
}, {
    "presenter": "Mihailo St. Popović",
    "title": "On the Use and Usefulness of Digital Humanities in the Historical Geography of Byzantium",
    "conference": "Seminar Series: The Balkans Between Empires, Aristotle University of Thessaloniki, Ibn Haldun University Istanbul",
    "date": '1.4.2022',
    'location': 'Thessaloniki',
    "category": ["holdura"]
}, {
    "presenter": "Markus Breier",
    "title": "Beyond East and West – Geocommunicating Historical Sacred Landscapes ",
    "conference": "International Medieval Congress, University of Leeds",
    "date": '7.7.2021',
    'location': 'Leeds',
    "category": ["holdura"]
}, {
    "presenter": "Markus Breier, Karel Kriz, Lukas Neugebauer, Alexander Pucher",
    "title": "Beyond East and West – Geocommunicating Historical Sacred Landscapes ",
    "conference": "30th International Cartographic Conference 2021",
    "date": '18.12.2021',
    'location': 'Florenz',
    "category": ["holdura"]
}]
