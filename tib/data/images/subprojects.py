from flask_babel import lazy_gettext as _l

path = 'images/gallery/'

montenegro = [
    {
        'path': f'{path}montenegro-relief.jpg',
        'description': _l('Detail of the Relief Map of Montenegro in the Courtyard of the Museum Biljarda (Cetinje)'),
        'citation': 'Museum Biljarda',
        'category': ['montenegro']
    }, {
        'path': f'{path}montenegro-pavilion.jpg',
        'description': _l('Pavilion of the Relief Map in the Courtyard of the Museum Biljarda (Cetinje)'),
        'citation': 'Museum Biljarda',
        'category': ['montenegro']
    }, {
        'path': f'{path}montenegro-budva-bay.jpg',
        'description': _l('The Bay of Budva in Montenegro'),
        'citation': 'M. Popović, 2016',
        'category': ['montenegro']
    }, {
        'path': f'{path}montenegro-aerial.jpg',
        'description': _l('Aerial Photo of Montenegro'),
        'citation': 'M. Popović, 2016',
        'category': ['montenegro']
    },
    {
        'path': f'{path}montenegro_pavillion.jpg',
        'description': _l(
            'The pavilion where the relief map of Montenegro is now located, '
            'Cetinje, Republic of Montenegro'),
        'citation': 'M. St. Popović 2020',
        'category': ['montenegro']
    },
    {
        'path': f'{path}montenegro_bucht_relief.jpg',
        'description': _l(
            'The Bay of Kotor on the relief map of Montenegro, Cetinje, '
            'Republic of Montenegro'),
        'citation': 'M. St. Popović 2020',
        'category': ['montenegro']
    },
    {
        'path': f'{path}montenegro_relief.jpg',
        'description': _l(
            'The relief map of Montenegro, in the foreground Lake Skadar, '
            'Cetinje, Republic of Montenegro'),
        'citation': 'M. St. Popović 2020',
        'category': ['montenegro']
    },
    {
        'path': f'{path}montenegro_relief_model.jpg',
        'description': _l('The 3D model of the relief map of Montenegro'),
        'citation': 'Moisés Hernández Cordero 2020',
        'category': ['montenegro']
    },
    {
        'path': f'{path}montenegro_relief_layer.jpg',
        'description': _l(
            'The 3D model of the relief map of Montenegro as a layer in the '
            '"Maps of Power" web application'),
        'citation': 'M. Breier, M. St. Popović 2021',
        'category': ['montenegro']
    },]

borderzones = [
    {
        'path': f'{path}border_all.png',
        'description': _l('Interpretation of the Byzantino-Serbian Border between 1228 and 1334 from Different Authors'),
        'citation': 'Bernhard Koschicek, 2018',
        'category': ['borderzones']
    }, {
        'path': f'{path}fortifications.png',
        'description': _l('Fortifications in the Northern Macedonian Region in the 13/14th century'),
        'citation': 'Bernhard Koschicek, 2019',
        'category': ['borderzones']
    }, {
        'path': f'{path}Marschroute_Abstract_cyrillic_km.png',
        'description': _l('Road Model based on a k. u k. Marching Map'),
        'citation': 'Bernhard Koschicek, 2018',
        'category': ['borderzones']
    },{
        'path': f'{path}borderzones_markovi_kuli.jpg',
'description': _l('Markovi Kuli Castle near Prilep from the south, Republic of Northern Macedonia'),
        'citation': 'M. St. Popović, TIB 16, 2007',
        'category': ['borderzones']
    },
    {
        'path': f'{path}borderzones_kale_skopje.jpg',
'description': _l('The Kale elevation in Skopje, Republic of Northern Macedonia'),
        'citation': 'M. St. Popović, TIB 16, 2016',
        'category': ['borderzones']
    },
    {
        'path': f'{path}borderzones_ohrid_stadttor.jpg',
'description': _l('The old city gate of Ohrid, Republic of Northern Macedonia'),
        'citation': 'M. St. Popović, TIB 16, 2018',
        'category': ['borderzones']
    },
    {
        'path': f'{path}borderzones_ohrid_samuilova.jpg',
'description': _l('Ohrid and Samuilova tvrdina Castle, Republic of Northern Macedonia'),
        'citation': 'M. St. Popović, TIB 16, 2018',
        'category': ['borderzones']
    },]

digtib = [
    {
        'path': f'{path}lesnovo_1920_30.jpg',
        'description': _l('Lesnovo, Monastery of St. Archangel Michael and St. Hermit Gabriel 1920/30. Cross-domed church with naos, narthex and exonarthex added in the 16th century'),
        'citation': 'unknown',
        'category': ['digtib']
    }, {
        'path': f'{path}lesnovo_2010.jpg',
        'description': _l('Lesnovo, Monastery of St. Archangel Michael and St. Hermit Gabriel 2010. cross-domed church with rebuilt exonarthex'),
        'citation': 'M. Popović, ÖAW, 2010',
        'category': ['digtib']
    }, {
        'path': f'{path}Ohrid_Ancient_Theatre_1988.jpg',
        'description': _l('Ohrid, Ancient Theatre 1988. Ancient theatre in Ohrid, abandoned by the locals after the end of the Roman Empire due to executions of Christians by the Romans'),
        'citation': 'M. Popović, 2016',
        'category': ['digtib']
    }, {
        'path': f'{path}Ohrid_Ancient_Theatre_2008.jpg',
        'description': _l('Ohrid, Ancient Theatre 2008. Gradual renovation of the theatre from the 1980s onwards'),
        'citation': 'Mihailo Popović, ÖAW, 2008',
        'category': ['digtib']
    }, {
        'path': f'{path}Pylai_Kilikias_Gülek Bogazi_Blick_thumb.jpg',
        'description': _l('The Cilician Gate (Pylai Kilikias) as the most important connection between Cilicia and the highlands in Anatolia'),
        'citation': 'Friedrich Hild, ÖAW, 1973',
        'category': ['digtib']
    }, {
        'path': f'{path}Pylai_Kilikias_google.jpg',
        'description': _l('Pylai Kilikias 2016. From the 1970s onwards, massive damage to the Cilician Gate for the purpose of widening the roadway as part of road construction works'),
        'citation': 'Müzik life https://goo.gl/maps/xe4UMk8DBjaEWX898, 2016',
        'category': ['digtib']
    }, {
        'path': f'{path}euboia_1967.png',
        'description': _l('Euboia, Panagia Monomeritissa 1967. Extension to the church of the monastery of Eria, which also served as a dwelling house'),
        'citation': 'Johannes Koder, ÖAW, 1967',
        'category': ['digtib']
    }, {
        'path': f'{path}euboia_1972.png',
        'description': _l('Euboia, Panagia Monomeritissa 1972. Deconstruction of this annexe in 1972'),
        'citation': 'Johannes Koder, ÖAW, 1972',
        'category': ['digtib']
    },
{
        'path': f'{path}digtib_melnik.jpg',
'description': _l('The town of Melnik in south-west Bulgaria, Republic of Bulgaria, 1970'),
        'citation': 'F. Hild, 1970',
        'category': ['digtib']
    },
    {
        'path': f'{path}digtib_melnik_2010.jpg',
'description': _l('The town of Melnik in south-west Bulgaria, Republic of Bulgaria, 2010'),
        'citation': 'M. St. Popović, 2010',
        'category': ['digtib']
    },
    {
        'path': f'{path}digtib_rila.jpg',
'description': _l('The monastery church of the Rila Monastery, Republic of Bulgaria, 1977'),
        'citation': 'P. Soustal, 1977',
        'category': ['digtib']
    },
    {
        'path': f'{path}digtib_rila_2010.jpg',
'description': _l('The monastery church of the Rila Monastery, Republic of Bulgaria,2014'),
        'citation': 'M. St. Popović,2014',
        'category': ['digtib']
    },
    {
        'path': f'{path}digtib_ohrid_bucht_1968.jpg',
'description': _l('The bay near the town of Ohrid, Republic of Northern Macedonia, 1968'),
        'citation': 'J. Koder, 1968',
        'category': ['digtib']
    },
    {
        'path': f'{path}digtib_ohrid_bucht_2017.jpg',
'description': _l('The bay near the town of Ohrid, Republic of Northern Macedonia, 2017'),
        'citation': 'M. St. Popović, 2017',
        'category': ['digtib']
    },
]

holdura = [
    {
        'path': f'{path}holdura_doclea_1.jpg',
'description': _l('Bird\'s eye view of the Doclea archaeological excavation, A: Basilica A, B: Basilica B and cruciform church, Republic of Montenegro'),
        'citation': 'L. Neugebauer, 2021',
        'category': ['holdura']
    }, {
        'path': f'{path}holdura_doclea_2.jpg',
'description': _l('Bird\'s eye view of the Doclea archaeological excavation, the western part of the city in the foreground, Republic of Montenegro'),
        'citation': 'L. Neugebauer, 2021',
        'category': ['holdura']
    }, {
        'path': f'{path}holdura_sveti_nikola.jpg',
'description': _l('The monastery of Sveti Nikola Vranjina (in the centre of the picture) on Lake Skadar, Republic of Montenegro'),
        'citation': 'B. Koschiček-Krombholz, 2021',
        'category': ['holdura']
    }, {
        'path': f'{path}holdura_ratac.jpg',
'description': _l('The former Latin (Catholic) monastery of Ratac from the 12th/13th century near the town of Bar, Republic of Montenegro.'),
        'citation': 'M. St. Popović, 2021',
        'category': ['holdura']
    },]
