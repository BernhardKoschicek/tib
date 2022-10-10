from flask_babel import lazy_gettext as _l

gallery_path = 'images/gallery/'

balkan_hist_geo = [{
    'path': f'{gallery_path}RilskaGramota.jpg',
    'description': _l('The document for the Rila Monastery of the Bulgarian Tsar Ivan III. Šišman (1378)'),
    'citation': '<a href="https://bg.wikipedia.org/wiki/%D0%A0%D0%B8%D0%BB%D1%81%D0%BA%D0%B0_%D0%B3%D1%80%D0%B0%D0%BC%D0%BE%D1%82%D0%B0">bg.wikipedia.org/wiki/Рилска_грамота</a>',
    'text': 'Wir lesen die schriftlichen Quellen der Zeit des 4. bis 15. Jahrhunderts, die in verschiedenen Sprachen verfasst sind (z. B. griechisch, lateinisch, altslawisch, etc.), und filtern alle Informationen zu den oben genannten Fragen heraus. <br />     Wir sammeln Daten zu Flurnamen aus den Quellen, neuzeitlichen Karten und Lexika.',
    'category': ['hist-geo']
}, {
    'path': f'{gallery_path}vlaska_carkva.jpg',
    'description': _l('Die verlassene Kirche Vlaška cărkva in Popovi livadi, SW-Bulgarien'),
    'citation': 'M. St. Popović, TIB 16, 2010',
    'text': 'Wir verschaffen uns einen Überblick über archäologische Grabungen und bestehende Denkmäler (Kirchen, Klöster, Burgen, etc.) vor Ort.',
    'category': ['hist-geo']
},{
    'path': f'{gallery_path}11Ezeba018.jpg',
    'description': _l('Peter Soustal with Kostantinos, a resident of the village of Daphni, Greece'),
    'citation': 'M. St. Popović, TIB 11, 2004',
    'text': '',
    'category': ['hist-geo']
},{
    'path': f'{gallery_path}altwege_2014.jpg',
    'description': _l('Documentation of an Old Way Relic in Northern Greece'),
    'citation': 'M. St. Popović, TIB 11, 2014',
    'text': '',
    'category': ['hist-geo']
},{
    'path': f'{gallery_path}bulgarisch_landwirt.jpg',
    'description': _l('Enquiry with a Bulgarian farmer, Bulgaria'),
    'citation': 'P. Soustal, TIB 16, 2010',
    'text': '',
    'category': ['hist-geo']
},{
    'path': f'{gallery_path}bar_22.jpg',
    'description': _l('Documentation of an early Christian basilica in Bar, Montenegro'),
    'citation': 'M. St. Popović, TIB 17, 2022',
    'text': '',
    'category': ['hist-geo']
},
]

