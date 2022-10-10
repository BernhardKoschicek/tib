from flask_babel import lazy_gettext as _l

gallery_path = 'images/gallery/'

tib_balkan_long_term = [{
    'path': f'{gallery_path}tib_regions_hunger.jpg',
    'description': _l('The division of the TIB Balkan working areas in the northern half of the Balkan Peninsula according to Herbert Hunger'),
    'citation': '',
    'category': ['tib_history']
}, {
    'path': f'{gallery_path}tib_balkan_overview.jpg',
    'description': _l('General map of the TIB Balkans'),
    'citation': 'Bernhard Koschiček-Krombholz, 2022',
    'category': ['tib_balkan']
},
]
