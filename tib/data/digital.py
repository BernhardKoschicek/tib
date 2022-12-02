from flask_babel import lazy_gettext as _l

objects3d = {
    'montenegro': {
        'description': _l(
            'The following objects were created within the project <a href="../subprojekte/montenegro">"Cultural heritage in the period of the First World War: the case of the Austro-Hungarian relief map of Montenegro (1916-1918)"</a>.'),
        'models': {
            "montenegro-relief": {
                "title": ("Relief Map of Montenegro"),
                "icon": "images/boxes_background/cetinje_relief_icon.jpg",
                "icon_description": _l(
                    "The Austro-Hungarian Relief Map of Montenegro (1917/18, M. Hernández Cordero, 2021)"),
                "path": "3dhop/relief.html",
            },
            "icon": {
                "title": _l("Icon of the Holy Mother"),
                "icon": "images/boxes_background/icon_icon.jpg",
                "icon_description": _l(
                    "Icon of the Holy Mother of God (20th Century, Metropolis of Austria and M. Hernández Cordero, 2021)"),
                "path": "3dhop/icon.html",
            },
            "mitra": {
                "title": _l("Orthodox Bishop's Mitra"),
                "icon": "images/boxes_background/mitra_icon.jpg",
                "icon_description": _l(
                    "Orthodox Bishop's Mitra (20th Century, Metropolis of Austria and M. Hernández Cordero, 2021)"),
                "path": "3dhop/mitra.html",
            }}},
    'holdura': {
        'description': _l(
            'The following objects were created within the project <a href="../subprojekte/holdura">"Beyond East and West: Geocommunicating the Sacred Landscapes of “Duklja” and “Raška” through Space and Time (11th-14th Cent.)"</a>.'),
        'models': {
            "sveti_jovan": {
                "title": _l("Church of St. John"),
                "icon": "images/boxes_background/sveti_jovan.png",
                "icon_description": _l(
                    "The Church of St. John the Baptist in Zaton, Montenegro (9th/10th Cent., Lukas Neugebauer, 2022)"),
                "path": "3dhop/sveti_jovan.html",
            },
            "krajinska": {
                "title": _l("Monastery of the Most Pure Mother of God"),
                "icon": "images/boxes_background/krajinska.png",
                "icon_description": _l(
                    "The Monastery of the Most Pure Mother of God of Krajina, Montenegro (10th/11th Cent., Lukas Neugebauer, 2022)"),
                "path": "3dhop/krajinska.html",
            },
            "moraca": {
                "title": _l("Monastery of Morača"),
                "icon": "images/boxes_background/moraca.png",
                "icon_description": _l(
                    "The Monastery of Morača, Montenegro (13th Cent., Lukas Neugebauer, 2022)"),
                "path": "3dhop/moraca.html",
            },
            "ratac": {
                "title": _l("Monastery of Bogorodica Ratačka"),
                "icon": "images/boxes_background/ratac.png",
                "icon_description": _l(
                    "The Monastery of Bogorodica Ratačka, Church C, Montenegro (11th Cent., Lukas Neugebauer, 2022)"),
                "path": "3dhop/ratac.html",
            }}}}
