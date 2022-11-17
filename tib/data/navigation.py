from flask_babel import lazy_gettext as _l

from tib.data.subprojects import subprojects

tib_nav_items = {
    'history': _l('history'),
    'current_status': _l('current_status'),
    'sub_projects': _l('sub_projects'),
    'publications': _l('publications'),
    'digtib': _l('digtib'),
    'aieb': _l('aieb'),
    'team': _l('team')}

balkan_nav_items = {
    'balkan_tib': [
        'balkan_long_term',
        'balkan_historical_geographie',
        'balkan_outreach',
        'balkan_team',
        'balkan_volumes'],
    'balkan_subprojects': [i for i in subprojects if subprojects[i]['part'] == 'balkan'],
    'balkan_digital': ['3dobjects', 'explore']}

balkan_nav_translations = {
    'balkan_tib': _l('balkan_tib'),
    'balkan_long_term': _l('balkan_long_term'),
    'balkan_historical_geographie': _l('balkan_historical_geographie'),
    'balkan_outreach': _l('balkan_outreach'),
    'balkan_team': _l('balkan_team'),
    'balkan_volumes': _l('balkan_volumes'),
    'balkan_subprojects': _l('balkan_subprojects'),
    'balkan_digital': _l('balkan_digital'),
    '3dobjects': _l('3dobjects'),
    'explore': _l('explore'),
    'holdura': _l('holdura'),
    'digtib': _l('digtib'),
    'borderzones': _l('borderzones'),
    'montenegro': _l('montenegro'),
}
balkan_jumbotron = {
    'balkan_tib': {
        'title': balkan_nav_translations['balkan_tib'],
        'icon': 'bi-image-alt',
    },
    'balkan_subprojects': {
        'title': balkan_nav_translations['balkan_subprojects'],
        'icon': 'bi-images',
    },
    'balkan_digital': {
        'title': balkan_nav_translations['balkan_digital'],
        'icon': 'bi-qr-code',
    },
}
tib_digtib_submenu_items = [
    {
        'title': _l('toponym_register'),
        'icon': 'bi-list-columns-reverse',
        'link': 'tib-register',
        'link_type': 'int',
        'tooltip': _l('A complete list of geographic registers of the published TIB volumes 1-13 and 15')
    },
    {
        'title': _l('image_collection'),
        'icon': 'bi-images',
        'link_type': 'ext',
        'link': 'https://catalogue.tib.oeaw.ac.at/',
        'tooltip': _l('Access to more than 7,000 slides of the TIB volumes 5, 12 and 16 enriched with metadata')
    },
    {
        'title': _l('map_application'),
        'icon': 'bi-map-fill',
        'link_type': 'ext',
        'link': 'https://data1.geo.univie.ac.at/projects/tibapp/',
        'tooltip': _l('Graphical map application to access, browse and query data from TIB Balkans')

    },
    {
        'title': _l('browse_tib_balkans_data'),
        'icon': 'bi-stack',
        'link': 'balkan/digital/explore',
        'link_type': 'int',
        'tooltip': _l('Browse data from TIB Balkans directly from the OpenAtlas database')
    }, ]

balkan_digital_submenu_items = [
    {
        'title': _l('map_application'),
        'icon': 'bi-map-fill',
        'link_type': 'ext',
        'link': 'https://data1.geo.univie.ac.at/projects/tibapp/',
        'tooltip': _l('Graphical map application to access, browse and query data from TIB Balkans')

    },
    {
        'title': _l('browse_tib_balkans_data'),
        'icon': 'bi-stack',
        'link': 'balkan/digital/explore',
        'link_type': 'int',
        'tooltip': _l('Browse data from TIB Balkans directly from the OpenAtlas database')
    },
    {
        'title': _l('View 3D Objects'),
        'icon': 'bi-badge-3d-fill',
        'link': 'balkan/digital/3dobjects',
        'link_type': 'int',
        'tooltip': _l('Examine different 3D objects')
    },
]
