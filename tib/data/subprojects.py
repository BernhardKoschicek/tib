from tib.data.institutes import institutes
from tib.data.tib.team import tib_team_data
from tib.util.util import get_dates_formatted

from flask_babel import lazy_gettext as _l

path = 'images/icons/'

project_descriptions = {
    'mesmy': [
        _l('Smyrna/Izmir, nowadays the third most populated city and a bustling economic center in modern Turkey, is situated in one of the Mediterranean’s most exciting crossroads of cultures littered with remains of ancient sites and monuments of different periods. There is a long tradition of archaeological research on classical, Hellenistic, and early Christian sites of the region; and Smyrna’s significance as an international hub of trade in the late Ottoman Empire have attracted the interest of numerous scholars. Since 2008, the Tabula Imperii Byzantini (TIB) project at the Austrian Academy of Sciences has been focusing on the historical geography of Western Asia Minor in Late Antiquity and Byzantine times and has been gathering the surviving written and material evidence.'),
        _l('The project “Medieval Smyrna/Izmir” probes the question as to how the city of Smyrna and its hinterland developed from its last heydays under Byzantine rule in the 13th century to the Ottoman conquest in the 15th century. During this period, the western coastland of Asia Minor underwent not only substantial environmental change but also profound political, cultural, and religious transformations, in the course of which Byzantine-Christian institutions, structures, and elites were gradually superseded by Muslim-Turkish entities and eventually absorbed into the nascent Ottoman Empire. The project examines this multilayered process through an interdisciplinary approach combining historical geography with methods of social and economic history and archaeology. It combines key components of Byzantine-Turkish transformation with broader archaeological questions concerning long-term patterns of settlement and human agency shaping the region’s entire medieval period. These axes of investigation will revolve around five thematic subunits, namely (a) environment, land use, economic practices, (b) political ideology, government, institutions, (c) urban life, (d) suburban and rural life; (e) religious spaces and practices. In this way, the project aspires to achieve a comprehensive reconstruction of transformative processes, which includes both material aspects of living conditions and the symbolic universe of different population groups.'),
        _l('The archaeological research will document currently existing material evidence of historical habitation, thus promoting future collaborations in the field of Byzantine archaeology in Anatolia. The historical research aims to produce a transposable case study of socio-cultural transformation, which will help elucidate similar processes in other parts and periods of the Mediterranean up to modern times.'), ],
    'holdura': [
        _l('In the current discourse on the integration of the Western Balkans into the European Union the ongoing and envisaged negotiations with the Republics of Montenegro, Serbia and Albania seem to be of remarkable importance in the contemporary media coverage. They comprise a region, which – in a long ago past – played, under the name of Illyricum (Illyrikon), a vital role in the strategic and administrative considerations of the Byzantine Empire.'),
        _l('The project builds upon a scholarly cooperation among the academic fields of Byzantine Studies, Medieval History, Historical Geography, Art History, Geography and Geocommunication (GIScience and Cartography) and focuses on two historic regions of “Duklja” and “Raška” being part of the Illyricum. The research hypothesis is that both historic regions constituted a “Sacred Landscape”, which we intend to decipher and to communicate to academia as well as to the interested public with the joint means of Historical Geography, Art History and Geocommunication.'),
        _l('Therefore, the project aims at approaching and researching systematically the following three major questions:'),
        _l('(1) In which way did the local rulers and the Churches of Rome and Constantinople interact in the regions of “Duklja” and “Raška” from the 11th to the 14th centuries and how is this very interaction mirrored in the distribution pattern of monuments (i.e. the churches and monasteries) in this “Sacred Landscape”?'),
        _l('(2) Did the volatile religious affiliation of the local rulers have an impact on the “Sacred Landscape” and where were Latin or Byzantine places of worship transformed or superimposed in the course of time?'),
        _l('(3) Can the religious and cultural influence of the Latin and Byzantine (Orthodox) faith be traced through small Latin (i.e. “Western”) as well as Byzantine and Slavic (i.e. “Eastern”) objects of art, not only in the coastal area, but also in its hinterland and in Italy? Both historic regions could prove to be constituting a zone “Beyond East and West”, subject to remarkable processes of transformation from the 11th to the 14th centuries, and have the huge potential to offer data suitable for visualisations as well as formalisation by GIScience. The integration and presentation of the research data (i.e. on the written sources, monuments and objects of art) of the project will be achieved through an already existing database and an online <a hrf="https://data1.geo.univie.ac.at/projects/tibapp">map application</a>.'),
        _l('The project is exclusively feasible through a multidisciplinary approach and cooperation between three project partners from Austria (Austrian Academy of Sciences, here Priv.-Doz. Mag. Dr. Mihailo Popović; University of Vienna, here Professor Dr. Karel Kriz) and Germany (Hochschule für Technik, Wirtschaft und Kultur Leipzig, here Professor Dr. Johannes Tripps).Moreover, it is closely connected to the ongoing scholarly work of Mihailo Popović on <a href="/current_status/TIB_17">TIB volume 17 “Nea Epeiros and Praevalis”</a> and on the TIB Sub Project <a href="sub_projects/montenegro">“Cultural Heritage in Times of World War I: The Case of the Austro-Hungarian Relief Map of Montenegro (1916-1918)”</a>.'), ],
    'inventory': [
        _l('The project aims to investigate the historical use of the Bulgarian coastline within the wider port networks and maritime connectivity of the Black Sea and the Mediterranean. A systematic archaeological study of the topographic evolution of the coast in association to the functionality of port sites and other coastal facilities during Late Antiquity and the Middle Ages shall provide new data on the development of coastal life and especially the nature of agricultural and industrial exploitation in context of maritime commerce. Particularly the continuously alternating relationship between the coast and river landscapes are to be emphasized. Based on written sources, historical accounts and already existing archaeological data, a comprehensive catalogue and database of harbor sites, anchorages and natural environments such as bays or river courses and their estuaries will be created. Building upon this database, the research project emphasizes on the analysis of the paleo geographic environment linked to sea-level changes in areas of pre-selected archaeological sites. By using Orthophotography and 3D shooting, the research project therefore complements the existing information. Latter will eventually be used for the study of network patterns and comparative studies of port hierarchies and interrelated functionalities of coastal infrastructures. This shall provide a new platform for a better understanding of maritime economy as well as social and cultural connectivity throughout the Black Sea region.'), ],
    'montenegro': [
        _l('A famous example of a relief map of the Balkan Peninsula in the former Yugoslavia is the map of Montenegro and adjacent territories, which was made in 1916/17 by order of the Austro-Hungarian military administration and is now located in the courtyard of the former royal residence "Biljarda" (now the National Museum of Montenegro) in Cetinje in the Republic of Montenegro. The National Museum of Montenegro in Cetinje reports about the relief map on its homepage on the Internet as follows: "After the Austro-Hungarian army made the breakthrough of the Lovćen front and occupied Cetinje in 1916, a glazed object with a relief map of Montenegro at a scale of 1:10,000 was erected on two levels in the south wing of the "Biljarda" residence, where the headquarters of the occupation troops was also located. The relief, which shows parts of Bosnia and Herzegovina, Croatia, Albania and Serbia, among others, consists of a concrete mass on a stone base and was prepared on the basis of precise Austrian topographic maps and land surveys, which in turn had been prepared using the most modern means. To determine the elevations on the map, a network of thin metal rods was used, around which the space in between was filled manually to match the landscape characteristics. The surface was then painted in detail so that it contained all the relevant information about the road network of that time, water areas, forests and populated places. For a better overview of the map, a bridge was built over its central part, from which every single detail was visible. In addition to Austro-Hungarian military cartographers, Montenegrin prisoners of war were also involved in the production of the relief map, including our famous sculptor Marko Brežanin. The old protective superstructure was demolished in the early 1980s and replaced by a glazed metal structure, which is still in use now. The relief map of Montenegro was declared a cultural monument (cultural property) by Decision No. 1794/1 of September 14, 1948. Apart from the undoubtedly military-strategic purposes it had during the war years, this unique object has gained importance over time due to its aesthetic and historical value, so that it now forms an inevitable tourist attraction." (Translation by M. Popović)'),
        _l('In the description of the National Museum of Montenegro, the statement "In addition to Austro-Hungarian military cartographers, Montenegrin prisoners of war were also involved in the production of the relief map, including our famous sculptor Marko Brežanin" is of particular interest. Surprisingly, the relief map is not mentioned in Austrian scientific literature, but only finds brief mention as a tourist attraction in modern Austrian or German travel guides about Montenegro.'),
        _l('The aim of the project is to investigate the circumstances and general conditions of the production of the relief map by the Austro-Hungarian army and to search for the Austro-Hungarian artists who worked on the relief map of Montenegro in 1916. Among the participants were the Austrian sergeant and sculptor Schugar, the sculptor Brežanin and the painter Grabwinkler.'),],
       'digtib': [
        _l('The devastating impact of wars on world cultural heritage has been widely discussed after 1945. Scholarly projects at the Austrian Academy of Sciences (ÖAW) have a long tradition of contributing to the study of the world\'s cultural heritage. Among them is the Long-Term Project "Tabula Imperii Byzantini" (TIB) of the Austrian Academy of Sciences, which is publishing a historical atlas of the Byzantine Empire with special attention to the Balkan Peninsula and Asia Minor. Since 1966 (until now), monuments and their (then) current state have been documented by means of slides during field trips. This unique collection of Byzantine monuments (around 52,000 slides) is a rich cultural asset and a pivotal point of the present project "The Digital Tabula Imperii Byzantini (Dig-TIB) as Contribution to the World’s Cultural Heritage" as well as future research work.'),
        _l('The initiatives in the field of Digital Humanities and Byzantine Studies in recent years have prompted the scholarly team of the TIB at the ÖAW to intensify the efforts not only to scan and preserve slides of the rich TIB archive, but also to enable a platform for the adequate presentation and sustainable use of the data.'),
        _l('The aim of the project is not to limit itself to digitisation / preservation in general, but to specifically embed the respective monuments and their subsequent fates in the past decades into the world cultural heritage in three different case studies. These case studies - "Cilicia and Isauria" (TIB 5, Friedrich Hild), "Eastern Thrace (Eurōpē)" (TIB 12, Andreas Külzer) and "Macedonia, Northern Part" (TIB 16, Mihailo Popovic) - were chosen because of the complex politico-military situation in the Middle East with its impact on the monuments in situ (TIB 5) and because they include areas whose infrastructures are developing rapidly with lasting consequences for the landscapes of the past and for the respective monuments (TIB 12 and TIB 16).'), ],
    'borderzones': [
        _l('The European continent as a whole and the European Union in particular are facing a period of increasing dynamics of internal migration as well as external immigration at the moment. Migration in all of its various aspects has always been a part of the history of the European continent. In medieval societies the question of migration is closely connected with the definition as well as the representation of medieval borders. Maps in historical atlases are designed to provide clear-cut lines of political formations and empires, which does not reflect the reality of civilizations neither in Antiquity, nor in the Middle Ages, nor in Early Modern Times. The dynamics of borders simultaneously shapes the dynamics of settlement patterns as well as of transportation networks.'),
        _l('The respective stand-alone project focuses on the borders of the Byzantine (Eastern Roman) Empire in medieval South-East Europe, namely in pre-Ottoman (i.e. Byzantine) Macedonia. Far-reaching political changes occurred in the Southern Balkan Peninsula from the end of the 13th until the middle of the 14th century, when the Serbian medieval kingdom expanded to the South under the king Stefan Uroš II Milutin at the expense of the Byzantine Empire, which lasted until the death of tsar Stefan Uroš IV Dušan (1355). This again had a severe impact on the border zones and cross-border societies between both realms in pre-Ottoman (i.e. Byzantine) Macedonia in the same period, especially in five selected target areas (the Strumica Valley, Lesnovo, Skopje, Ohrid, Prilep).'),
        _l('Although substantial publications exist on the population of as well as on the migration in Byzantine Macedonia, there is still an urgent need for this kind of research based on written sources and toponyms. Two interrelated research questions will be addressed in two distinct work packages: "Rivalling Political Concepts – Byzantium and the Medieval Serbian Oecumene” and "Cross-Border Societies and Elite Change in Byzantine Macedonia”.'),
        _l('The initial point form the medieval written sources, i.e. Serbian and Byzantine charters as main corpus, as well as other selected written sources from the medieval Serbian kingdom. The sources will be analysed from the viewpoint of the aforesaid research questions and strongly based on the methods deriving from Historical Geography. Special attention will be given to the analysis of formulations with regard to the Serbian expansion in the area of research, the acquisition of new territories and their administrative incorporation on the macro-level and to the localisation of conquered settlements with related settlement typologies as well as on the change of local elites on a micro-level. Moreover, tools from Digital Humanities in mapping and visualisation will be applied in order to communicate the achieved results to the interested public.'), ]}

subprojects = {
    'mesmy': {
        'title': _l(
            'Medieval Smyrna / İzmir: The Transformation of a City and its Hinterland from Byzantine to Ottoman Times'),
        'funded_by': [institutes['fwf']],
        'project_number': 'P 33829-G',
        'pi': [tib_team_data['akulzer']],
        'cooperation': [
            _l('Univ. Prof. Dr. Alexander Beihammer, University of Notre Dame'),
            _l('Dr. Myrto Veikou, Uppsala University')],
        'employees': [tib_team_data['dariantzi']],
        'begin': get_dates_formatted(2021, 1, 15),
        'end': get_dates_formatted(2025, 1, 14),
        'description': project_descriptions['mesmy'],
        'question': '',
        'icon': f'{path}mesmy_icon.jpg',
        'presentations': [],
        'publications': [],
        'outreach': [],
        'part': 'asia',
    },
    'holdura': {
        'title': _l(
            'Beyond East and West: Geocommunicating the Sacred Landscapes of “Duklja” and “Raška” through Space and Time (11th-14th Cent.)'),
        'funded_by': [institutes['fwf'], institutes['dfg']],
        'project_number': 'I 4330-G',
        'pi': [tib_team_data['mpopovic']],
        'cooperation': [
            'Mag. Markus Breier', 'Lukas Neugebauer, BSc MSc',
            'Florian Korn, BSc MSc', 'Dipl.-Ing. Leonhard Kreil-Brunauer',
            'Ass. Prof. Dr. Branka Vranešević'],
        'employees': [tib_team_data['dvargova'], tib_team_data['bkoschicek'],
                      tib_team_data['dschmid']],
        'begin': get_dates_formatted(2020, 3, 1),
        'end': get_dates_formatted(2023, 8, 31),
        'description': project_descriptions['holdura'],
        'question':
            _l('Läßt sich im jetzigen Montenegro eine „heilige Landschaft“ aus mittelalterlichen Kirchen und Klöstern rekonstruieren?'),
        'icon': f'{path}holdura_icon.jpg',
        'presentations': [],
        'publications': [],
        'outreach': [],
        'part': 'balkan',
    },
    'inventory': {
        'title': _l(
            'Inventory of Late Antique and Medieval Ports along the Western Black Sea'),
        'funded_by': [],
        'project_number': '',
        'pi': [tib_team_data['akulzer']],
        'cooperation': [
            'Mag. Dr. Alkiviadis Ginalis (Curator for Late Antique and Byzantine Archaeology at the German Archaeological Institute, Department Istanbul)'],
        'employees': [],
        'begin': get_dates_formatted(2019, 8, 29),
        'end': get_dates_formatted(2021, 8, 28),
        'description': project_descriptions['inventory'],
        'question': '',
        'icon': f'{path}inventory_icon.jpg',
        'presentations': [],
        'publications': [],
        'outreach': [],
        'part': 'asia',
    },
    'montenegro': {
        'title': _l(
            'Cultural Heritage in Times of World War I: The Case of the Austro-Hungarian Relief Map of Montenegro (1916-1918)'),
        'funded_by': [institutes['oead']],
        'project_number': 'ME 07/2019',
        'pi': [tib_team_data['mpopovic']],
        'cooperation': [
            'Jelena Nikić, BA',
            _l('University of Donja Gorica (Faculty for Culture and Tourism, Podgorica, Montenegro)'),
            _l('Austrian Archaeological Institute (ÖAI) of the Austrian Academy of Sciences (Director Priv.-Doz. MMag. Dr. A. Pülz, w.M.)'),
            _l('National Museum of Montenegro (Narodni muzej Crne Gore, Cetinje, Montenegro)')
        ],
        'employees': [tib_team_data['vpolloczek'], tib_team_data['bkoschicek'],
                      tib_team_data['mhernandez']],
        'begin': get_dates_formatted(2019, 1, 1),
        'end': get_dates_formatted(2021, 12, 31),
        'description': project_descriptions['montenegro'],
        'question': _l(
            'Was blieb von der österreichisch-ungarischen Besetzung Montenegros im Ersten Weltkrieg?'),
        'icon': f'{path}montenegro_icon.jpg',
        'presentations': [],
        'publications': [],
        'outreach': [],
        'part': 'balkan',
    },
    'digtib': {
        'title': _l(
            'The Digital Tabula Imperii Byzantini (Dig-TIB) as Contribution to the World’s Cultural Heritage'),
        'funded_by': [institutes['oenb']],
        'project_number': '17771',
        'pi': [tib_team_data['mpopovic']],
        'cooperation': ['Alexander Watzinger, IT Experte'],
        'employees': [tib_team_data['vpolloczek'], tib_team_data['bkoschicek'],
                      tib_team_data['mhernandez']],
        'begin': get_dates_formatted(2018, 3, 1),
        'end': get_dates_formatted(2020, 5, 31),
        'description': project_descriptions['digtib'],
        'question': _l(
            'Welchen Beitrag leistet die TIB Balkan zur Dokumentation und Erhaltung von Kulturdenkmälern auf der Balkanhalbinsel?'),
        'icon': f'{path}digtib_icon.jpg',
        'presentations': [],
        'publications': [],
        'outreach': [],
        'part': 'balkan',
    },
    'borderzones': {
        'title': _l(
            'Byzantino-Serbian Border Zones in Transition: Migration and Elite Change in pre-Ottoman Macedonia (1282–1355)'),
        'funded_by': [institutes['fwf']],
        'project_number': 'P 30384-G28',
        'pi': [tib_team_data['mpopovic']],
        'cooperation': '',
        'employees': [tib_team_data['vzervan'], tib_team_data['bkoschicek']],
        'begin': get_dates_formatted(2017, 10, 1),
        'end': get_dates_formatted(2022, 3, 31),
        'description': project_descriptions['borderzones'],
        'question': _l(
            'Wo und wie lebten die Menschen in der historischen Landschaft Makedonien während des byzantinisch-serbischen Konflikts im 14. Jahrhundert?'),
        'icon': f'{path}borderzones_icon.jpg',
        'presentations': [],
        'publications': [],
        'outreach': [],
        'part': 'balkan',
    }
}