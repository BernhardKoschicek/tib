from datetime import datetime

from tib.data.institutes import institutes
from tib.data.tib.team import tib_team_data

path = 'images/team'


descriptions = {
    'mesmy': """
    <p>
    Smyrna/Izmir, nowadays the third most populated city and a bustling economic center in modern Turkey, is situated in one of the Mediterranean’s most exciting crossroads of cultures littered with remains of ancient sites and monuments of different periods. There is a long tradition of archaeological research on classical, Hellenistic, and early Christian sites of the region; and Smyrna’s significance as an international hub of trade in the late Ottoman Empire have attracted the interest of numerous scholars. Since 2008, the Tabula Imperii Byzantini (TIB) project at the Austrian Academy of Sciences has been focusing on the historical geography of Western Asia Minor in Late Antiquity and Byzantine times and has been gathering the surviving written and material evidence.
    </p>
    <p>
   The project “Medieval Smyrna/Izmir” probes the question as to how the city of Smyrna and its hinterland developed from its last heydays under Byzantine rule in the 13th century to the Ottoman conquest in the 15th century. During this period, the western coastland of Asia Minor underwent not only substantial environmental change but also profound political, cultural, and religious transformations, in the course of which Byzantine-Christian institutions, structures, and elites were gradually superseded by Muslim-Turkish entities and eventually absorbed into the nascent Ottoman Empire. The project examines this multilayered process through an interdisciplinary approach combining historical geography with methods of social and economic history and archaeology. It combines key components of Byzantine-Turkish transformation with broader archaeological questions concerning long-term patterns of settlement and human agency shaping the region’s entire medieval period. These axes of investigation will revolve around five thematic subunits, namely (a) environment, land use, economic practices, (b) political ideology, government, institutions, (c) urban life, (d) suburban and rural life; (e) religious spaces and practices. In this way, the project aspires to achieve a comprehensive reconstruction of transformative processes, which includes both material aspects of living conditions and the symbolic universe of different population groups.
    </p>
    <p>
   The archaeological research will document currently existing material evidence of historical habitation, thus promoting future collaborations in the field of Byzantine archaeology in Anatolia. The historical research aims to produce a transposable case study of socio-cultural transformation, which will help elucidate similar processes in other parts and periods of the Mediterranean up to modern times.</p>"""
}

subprojects = {
    'mesmy': {
        'title': 'Medieval Smyrna / İzmir: The Transformation of a City and its Hinterland from Byzantine to Ottoman Times (MESMY)',
        'funded_by': [institutes['fwf']],
        'project_number': 'P 33829-G',
        'pi': [tib_team_data['akulzer']],
        'cooperation': [
            'Univ. Prof. Dr. Alexander Beihammer, University of Notre Dame',
            'Dr. Myrto Veikou, Uppsala University'],
        'employees': [tib_team_data['dariantzi']],
        'begin': datetime(2021, 1, 15).strftime('%d %B %Y'),
        'end': datetime(2025, 1, 14).strftime('%d %B %Y'),
        'description': descriptions['mesmy'],
        'icon': f'{path}/mesmy/mesmy_icon.jpg',
        'images': [],
        'presentations': [],
        'publications': [],
        'outreach': [],
    },
    'holdura': {
        'title': 'Medieval Smyrna / İzmir: The Transformation of a City and its Hinterland from Byzantine to Ottoman Times (MESMY)',
        'funded_by': [institutes['fwf'], institutes['dfg']],
        'project_number': 'I 4330-G',
        'pi': [tib_team_data['mpopovic']],
        'cooperation': [
            'Mag. Markus Breier', 'Lukas Neugebauer, BSc MSc',
            'Florian Korn, BSc MSc', 'Dipl.-Ing. Leonhard Kreil-Brunauer',
            'Ass. Prof. Dr. Branka Vranešević'],
        'employees': [tib_team_data['dvargova'], tib_team_data['bkoschicek'],
                      tib_team_data['dschmid']],
        'duration': datetime(2020, 3, 1).strftime('%d %B %Y'),
        'end': datetime(2023, 2, 28).strftime('%d %B %Y'),
        'icon': f'{path}/holdura/holdura_icon.jpg',
        'images': [],
        'presentations': [],
        'publications': [],
        'outreach': [],
    }
}
