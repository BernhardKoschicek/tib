from tib.data.register.tib1 import tib1_table_data
from tib.data.register.tib10 import tib10_table_data
from tib.data.register.tib11 import tib11_table_data
from tib.data.register.tib12 import tib12_table_data
from tib.data.register.tib13 import tib13_table_data
from tib.data.register.tib15 import tib15_table_data
from tib.data.register.tib2 import tib2_table_data
from tib.data.register.tib3 import tib3_table_data
from tib.data.register.tib4 import tib4_table_data
from tib.data.register.tib5 import tib5_table_data
from tib.data.register.tib6 import tib6_table_data
from tib.data.register.tib7 import tib7_table_data
from tib.data.register.tib8 import tib8_table_data
from tib.data.register.tib9 import tib9_table_data

from flask_babel import lazy_gettext as _l

toponym_register = tib1_table_data + tib2_table_data + tib3_table_data + \
                   tib4_table_data + tib5_table_data + tib6_table_data + \
                   tib7_table_data + tib8_table_data + tib9_table_data + \
                   tib10_table_data + tib12_table_data + tib13_table_data + \
                   tib11_table_data

register_volume = {
    'all': {
        'title': _l('Complete Register of TIB 1-13'),
        'register': toponym_register,
        'published': True,
    },
    'tib1': {
        'title': _l('TIB 1 Hellas and Thessaly'),
        'register': tib1_table_data,
        'published': True,
    },
    'tib2': {
        'title': _l('TIB 2 Cappadocia (Kappadokia, Charsianon, Sebasteia and Lykandos)'),
        'register': tib2_table_data,
        'published': True,
    },
    'tib3': {
        'title': _l('TIB 3 Nicopolis and Cephalonia'),
        'register': tib3_table_data,
        'published': True,
    },
    'tib4': {
        'title': _l('TIB 4 Galatia and Lycaonia'),
        'register': tib4_table_data,
        'published': True,
    },
    'tib5': {
        'title': _l('TIB 5 Cilicia and Isauria'),
        'register': tib5_table_data,
        'published': True,
    },
    'tib6': {
        'title': _l('TIB 6 Thrace (Thrakē, Rodopē and Haimimontos)'),
        'register': tib6_table_data,
        'published': True,
    },
    'tib7': {
        'title': _l('TIB 7 Phrygia and Pisidia'),
        'register': tib7_table_data,
        'published': True,
    },
    'tib8': {
        'title': _l('TIB 8 Lycia and Pamphylia'),
        'register': tib8_table_data,
        'published': True,
    },
    'tib9': {
        'title': _l('TIB 9 Paphlagonia and Honorias'),
        'register': tib9_table_data,
        'published': True,
    },
    'tib10': {
        'title': _l('TIB 10 Nothern Aegean'),
        'register': tib10_table_data,
        'published': True,
    },
    'tib11': {
        'title': _l('TIB 11 Macedonia, Southern Part'),
        'register': tib11_table_data,
        'published': True,
    },
    'tib12': {
        'title': _l('TIB 12 Eastern Thrace (Eurōpē)'),
        'register': tib12_table_data,
        'published': True,
    },
    'tib13': {
        'title': _l('TIB 13 Bithynia and Hellespont'),
        'register': tib13_table_data,
        'published': True,
    },
    'tib14': {
        'title': _l('TIB 14 Western Asia Minor: Lydia and Asia'),
        'register': '',
        'published': False,
    },
    'tib15': {
        'title': _l('TIB 15 Syria (Syria Prōtē, Syria Deutera, Syria Euphratēsia)'),
        'register': tib15_table_data,
        'published': True,
    },
    'tib16': {
        'title': _l('TIB 16 Macedonia, Northern Part'),
        'register': '',
        'published': False,
    },
    'tib17': {
        'title': _l('TIB 17 Nea Epeiros and Praevalis'),
        'register': '',
        'published': False,
    },
    'tib18': {
        'title': _l('TIB 18 Caria'),
        'register': '',
        'published': False,
    },
}
