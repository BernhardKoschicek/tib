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

    }
}
