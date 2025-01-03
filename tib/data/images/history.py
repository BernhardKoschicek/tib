from flask_babel import lazy_gettext as _l

history_path = 'images/history/'

tib_history_images = {
    '1978': {
        'path': f'{history_path}1978.jpg',
        'description': _l('The State of the Project TIB in 1978'),
        'citation': 'Johannes Koder, Überlegungen zu Konzept und Methode der „Tabula Imperii Byzantini“. Österreichische Osthefte 20 (1978) 254-262, p. 255.',
        'category': ['tib_history']
    },
    '1991': {
        'path': f'{history_path}1991.jpg',
        'description': _l('The State of the Project TIB in 1991'),
        'citation': 'Herbert Hunger, Bericht über die Tabula Imperii Byzantini. Entstehung – Aufbau – Fortschritte, in: XVIIIth International Congress of Byzantine Studies. Major Papers. Moscow 1991, 275-281, p. 281.',
        'category': ['tib_history']
    },
    '1996': {
        'path': f'{history_path}1996.jpg',
        'description': _l('The State of the Project TIB in 1996'),
        'citation': 'Johannes Koder, Perspektiven der Tabula Imperii Byzantini. Zu Planung, Inhalt und Methode, Geographia antiqua 5 (1996), 75-86, p. 86.',
        'category': ['tib_history']
    },
    '2006': {
        'path': f'{history_path}2006.jpg',
        'description': _l('The State of the Project TIB in 2006'),
        'citation': 'Elisabeth Charlotte Beer',
        'category': ['tib_history']
    },
    '2012': {
        'path': f'{history_path}2012.jpg',
        'description': _l('The State of the Project TIB in 2012'),
        'citation': '',
        'category': ['tib_history']
    },
    '2017': {
        'path': f'{history_path}2017.jpg',
        'description': _l('The State of the Project TIB in 2017'),
        'citation': 'Mihailo St. Popović',
        'category': ['tib_history']
    },
    '2021': {
        'path': f'{history_path}2021.png',
        'description': _l('The State of the Project TIB in 2022'),
        'citation': 'Bernhard Koschiček-Krombholz, 2022',
        'category': ['tib_history']
    },
    'hunger': {
        'path': f'{history_path}hunger.jpg',
        'description': 'Herbert Hunger',
        'citation': '',
        'category': ['tib_history']
    },
    'core': {
        'path': f'{history_path}kerngebiete.jpg',
        'description': _l('The Core Areas of the Byzantine Empire according to Johannes Koder'),
        'citation': 'Johannes Koder, Perspektiven der Tabula Imperii Byzantini. Zu Planung, Inhalt und Methode, Geographia antiqua 5 (1996), 75-86, p. 86.',
        'category': ['tib_history']
    },
    'koder': {
        'path': f'{history_path}koder.jpg',
        'description': _l('Johannes Koder receiving His PhD-Degree by Professor Herbert Hunger in 1965'),
        'citation': '',
        'category': ['tib_history']
    },
    'overview': {
        'path': f'{history_path}overview.jpg',
        'description': _l('The Overview of the Entire Map of the TIB based on the Calculations by the Geographer and Cartographer Fritz Kelnhofer'),
        'citation': 'Fritz Kelnhofer, Die topographische Bezugsgrundlage der Tabula Imperii Byzantini. Mit 12 Tabellen und 16 Abbildungen im Text. Wien 1976 (Tabula Imperii Byzantini, Beiheft zu Band 1), 6.',
        'category': ['tib_history']
    },
    'turkey_road_1960': {
        'path': f'{history_path}turkey_road_1960.jpg',
        'description': _l('On the Road for the TIB in Turkey in the 1960s'),
        'citation': 'TIB Archive',
        'category': ['tib_history']
    },
    'survey_cappadocia_1960_1': {
        'path': f'{history_path}survey_cappadocia_1960_1.jpg',
        'description': _l('Surveying in Cappadocia in the 1960s'),
        'citation': 'TIB Archive',
        'category': ['tib_history']
    },
    'survey_cappadocia_1960_2': {
        'path': f'{history_path}survey_cappadocia_1960_2.jpg',
        'description': _l('Surveying in Cappadocia in the 1960s'),
        'citation': 'TIB Archive',
        'category': ['tib_history']
    },
    'albania_1960': {
        'path': f'{history_path}albania_1960.jpg',
        'description': _l('Travelling in Albania in the 1960s'),
        'citation': 'TIB Archive',
        'category': ['tib_history']
    },
    'survey_bulgaria_1970': {
        'path': f'{history_path}survey_bulgaria_1970.jpg',
        'description': _l('Surveying in Bulgaria in the 1970s'),
        'citation': 'TIB Archive',
        'category': ['tib_history']
    },
    'rila_1970': {
        'path': f'{history_path}rila_1970.jpg',
        'description': _l('A Visit to the Monastery of Rila in Bulgaria in the 1970s'),
        'citation': 'TIB Archive',
        'category': ['tib_history']
    },
}
