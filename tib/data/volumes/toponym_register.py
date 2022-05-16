from tib.data.volumes.tib1 import tib1_table_data
from tib.data.volumes.tib10 import tib10_table_data
from tib.data.volumes.tib12 import tib12_table_data
from tib.data.volumes.tib13 import tib13_table_data
from tib.data.volumes.tib15 import tib15_table_data
from tib.data.volumes.tib2 import tib2_table_data
from tib.data.volumes.tib3 import tib3_table_data
from tib.data.volumes.tib4 import tib4_table_data
from tib.data.volumes.tib5 import tib5_table_data
from tib.data.volumes.tib6 import tib6_table_data
from tib.data.volumes.tib7 import tib7_table_data
from tib.data.volumes.tib8 import tib8_table_data
from tib.data.volumes.tib9 import tib9_table_data

toponym_register = tib1_table_data + tib2_table_data + tib3_table_data + \
                   tib4_table_data + tib5_table_data + tib6_table_data + \
                   tib7_table_data + tib8_table_data + tib9_table_data + \
                   tib10_table_data + tib12_table_data + tib13_table_data + \
                   tib15_table_data

register_volume = {
    'tib1': {
        'title': 'TIB 1 Hellas and Thessaly',
        'icon': '',
        'published': True,
    },
    'tib2': {
        'title': 'TIB 2 Cappadocia (Kappadokia, Charsianon, Sebasteia and Lykandos)',
        'icon': '',
        'published': True,
    },
    'tib3': {
        'title': 'TIB 3 Nicopolis and Cephalonia',
        'icon': '',
        'published': True,
    },
    'tib4': {
        'title': 'TIB 4 Galatia and Lycaonia',
        'icon': '',
        'published': True,
    },
    'tib5': {
        'title': 'TIB 5 Cilicia and Isauria',
        'icon': '',
        'published': True,
    },
    'tib6': {
        'title': 'TIB 6 Thrace (Thrakē, Rodopē and Haimimontos)',
        'icon': '',
        'published': True,
    },
    'tib7': {
        'title': 'TIB 7 Phrygia and Pisidia',
        'icon': '',
        'published': True,
    },
    'tib8': {
        'title': 'TIB 8 Lycia and Pamphylia',
        'icon': '',
        'published': True,
    },
    'tib9': {
        'title': 'TIB 9 Paphlagonia and Honorias',
        'icon': '',
        'published': True,
    },
    'tib10': {
        'title': 'TIB 10 Nothern Aegean',
        'icon': '',
        'published': True,
    },
    'tib11': {
        'title': 'TIB 11 Macedonia, Southern Part',
        'icon': '',
        'published': True,
    },
    'tib12': {
        'title': 'TIB 12 Eastern Thrace (Eurōpē)',
        'icon': '',
        'published': True,
    },
    'tib13': {
        'title': 'TIB 13 Bithynia and Hellespont',
        'icon': '',
        'published': True,
    },
    'tib14': {
        'title': 'TIB 14 Western Asia Minor: Lydia and Asia',
        'icon': '',
        'published': True,
    },
    'tib15': {
        'title': 'TIB 15 Syria (Syria Prōtē, Syria Deutera, Syria Euphratēsia)',
        'icon': '',
        'published': True,
    },
    'tib16': {
        'title': 'TIB 16 Macedonia, Northern Part',
        'icon': '',
        'published': True,
    },
    'tib17': {
        'title': 'TIB 17 Nea Epeiros and Praevalis',
        'icon': '',
        'published': True,
    },
    'tib18': {
        'title': 'TIB 18 Caria',
        'icon': '',
        'published': True,
    },
}
