from flask_babel import lazy_gettext as _l

PATH = 'images/team'

tib_team_data = {
    'akulzer': {
        'name': 'Andreas Külzer',
        'team': _l('asia_minor'),
        'category': _l('project_leader'),
        'titles': ['Univ.-Prof.', 'Dr. phil.', 'Mag.', 'Dr. phil.'],
        'description':  _l('Univ.-Prof. Mag. Dr. phil. 1990: Magister Artium, 1993: Dr. phil. (summa cum laude), 1999: professorial qualification (Habilitation), 2007: adjunct Professor (apl. Univ.-Professor) of Byzantine History and Literature at the University of Cologne. Board member of the Austrian Byzantine Society, Vienna; Member of the Austrian National Committee of the Association Internationale des Études Byzantines. Research Interests: Western Anatolia from Early Roman times to the Ottoman period – Harbors and maritime networks in the Eastern Mediterranean – Historical Geography of Asia Minor and the Balkans – Late Antique and Medieval Pilgrimages – Late Antiquity – Ephesus.'),
        'email': 'andreas.kuelzer@oeaw.ac.at',
        'image': f'{PATH}/andreas.jpg',
        'academia': 'https://oeaw.academia.edu/AndreasKuelzer'
    },
    'dariantzi': {
        'name': 'Despoina Ariantzi',
        'team': _l('asia_minor'),
        'category': _l('scientific_employee'),
        'titles': ['Dr. phil.', 'Mag.a phil.'],
        'description':  _l('Mag. phil. with distinction (University of Ioannina 2001); Dr. phil. with distinction (University of Vienna, 2009), lecturer in Byzantine History at the University of Nicosia/Cyprus (2010-2011); at the University of Vienna (SS 2015); at the National and Kapodistrian University of Athen (SS 2018); PostDoc (scientific_employee) 2011-14; (University of Vienna); project_leader at the RGZM Mainz/Germany (2015-2016); PostDoc (scientific_employee) 2016-2020 (Univeristy of Vienna). Research Interests: Social and cultural history of the Byzantine Empire – History of Childhood – Coming of Age; History of Family – Hagiography and monasticism – Pilgrimage – Marginalization and subculture groups (Prostitutes, actors and tavern- keepers) – Gender Studies.'),
        'email': 'despoina.ariantzi@oeaw.ac.at',
        'image': f'{PATH}/ariantzi.png',
        'academia': 'https://independent.academia.edu/DAriantzi'
    },
    'gtheochari': {
        'name': 'Georgia Theochari',
        'team': _l('asia_minor'),
        'category': _l('spatial_analyst'),
        'titles': ['BSc', 'MSc'],
        'description':  _l('BSc in Mathematics, Aristotle University of Thessaloniki; MSc in Informatics (Computer Science), Aristotle University of Thessaloniki; Research Interests: Mathematics, Mathematical Modeling, Computational Methods, Information and Communication Technology in Education, Graphs Theory and Spatial Analysis, GIS'),
        'email': 'gtheocha@csd.auth.gr',
        'image': f'{PATH}/gtheochari.jpg',
        'academia': 'https://www.researchgate.net/profile/Georgia-Theochari'
    },
    'mpopovic': {
        'name': 'Mihailo Popović',
        'team': _l('balkans'),
        'category': _l('project_leader'),
        'titles': ['Priv.-Doz.', 'Dr. phil.', 'Mag.'],
        'description':  _l('Priv.-Doz. Mag. Dr. phil.; 2000: Mag. phil. with highest distinction (University of Vienna, 2000); Dr. phil. with highest distinction (University of Vienna, 2005); Unanimous decision to be granted a licence to teach "History of South-East Europe and Byzantine Studies" (University of Vienna, 2011); 2017-2022: Chair of the "Commission for the Historical Geography and Spatial Analysis of Byzantium" at the International Association of Byzantine Studies (AIEB). Research Interests: History and Culture of South Eastern Europe (7th-16th Centuries), Late Byzantine History (1204-1453), Gender Studies, Historical Geography and Cartography of the Mediterranean, Digital Humanities and Historical Geographic Information Systems (HGIS)'),
        'email': 'Mihailo.Popovic@oeaw.ac.at',
        'image': f'{PATH}/mpopovic.png',
        'academia': 'https://oeaw.academia.edu/MihailoPopovic'
    },
    'bkoschicek': {
        'name': 'Bernhard Koschiček-Krombholz',
        'team': _l('balkans'),
        'category': _l('software_developer'),
        'titles': ['BA', 'Bsc'],
        'description':  _l('BSc in Computer Sciences, BA in History, student of Computer Sciences at the University of Applied Sciences Technikum Wien and currently student of history at the University of Vienna. Research interests include computer security, python, Linked Open Data, API, digital reservation, historical geographie, GIS, medieval and military history.'),
        'email': 'bernhard.koschicek-krombholz@oeaw.ac.at',
        'image': f'{PATH}/bernhard.jpg',
        'academia': 'https://oeaw.academia.edu/BernhardKoschicek'
    },
    'dvargova': {
        'name': 'Dorota Vargová',
        'team': _l('former_employee'),
        'category': _l('former_employee'),
        'titles': ['MA'],
        'description':  _l('2016 BA in History (University of Vienna); 2016-2021 MA in History (University of Vienna); Research interest: european history, early-modern history, history of the european identity, history of the middle ages and late antiquity.'),
        'email': 'Dorota.Vargova@oeaw.ac.at',
        'image': f'{PATH}/dorota.jpg',
        'academia': 'https://independent.academia.edu/DorotaVargov%C3%A1'
    },
    'vzervan': {
        'name': 'Vratislav Zervan',
        'team': _l('associated_scholars'),
        'category': _l('scientific_employee'),
        'titles': ['PhD', 'MA'],
        'description':  _l('MA, PhD; 2006: Master Degree in Archaeology and History; 2010: Master Degree in Classical Philology (Faculty of Arts, Comenius University, Bratislava); 2014: PhD in General History (Faculty of Arts, Comenius University, Bratislava); Research Interests: Byzantine History; Byzantine and Slavonic Literature; Archaeology; Historical Geography; Lexicography'),
        'email': 'Vratislav.Zervan@oeaw.ac.at',
        'image': f'{PATH}/vrato.png',
        'academia': 'https://oeaw.academia.edu/vratislavzervan'
    },
    'jkoder': {
        'name': 'Johannes Koder',
        'team': _l('tib_editor'),
        'category': _l('editor_of_tib'),
        'titles': ['w.M.', 'Prof.', 'Dr. phil.'],
        'description':  _l('w.M., Prof. Dr.; 1960-1965 Byzantine, Arab and Classical Studies in Vienna University; 1965 Dr. phil. (Herbert Hunger); postdoctoral studies in Athens and in Munich (Alexander von Humboldt-Scholarship, 1970/71 and 1974, Hans-Georg Beck), 1973 "Habilitation". 1977 assoc. Professor (University of Vienna); 1978-1985 Professor and director of the department for Byzantine Studies, Johannes Gutenberg Universität, Mainz, Germany; 1985-2010 Professor and 1987-1989/1991-1993/1995-2010 Director of the Institute for Byzantine and Neohellenic Studies, University of Vienna. Austrian Archaeological Institute, interim director, 2007-2009; director of excavations, Ephesos, 2008-2009. Austrian Academy of Sciences: corresponding member 1989, 2000 full member, director of the research units "Tabula Imperii Byzantini" (until 2005) and "Balkan-Kommission" (until 2007), chair Advisory Board Institut für Byzanzforschung (2006-2008); Austrian Federal Board of Professors of Universities, member 1991, president 1993-2003; Austrian Association for Byzantine Studies, member 1963, president 1996-2014; Association Internationale des Études Byzantines, vice-president 1986, president 2012-2016; Dumbarton Oaks Research Library and Collection (Washington). senior fellow Byzantine studies, 2002-2008 (chair 2005-2008); Academy of Athens, foreign member 2007; Academia Europaea, member (2012); Dr. h. c. University of Athens (2006), University of Ioannina (2011), University of Thrake (2016); Full member, Austrian Archaeological Institute (2010); Distinctions: "Commander of the Order of the Phoenix" of the Hellenic Republic (1996), „Distinguished Decoration in Gold for Service to the Republic of Austria" (2004), "Cross of Merit for Science and Art", 1st class, Republic of Austria (2010).'),
        'email': 'Johannes.Koder@oeaw.ac.at',
        'image': f'{PATH}/johannes.png',
        'academia': 'https://independent.academia.edu/JohannesKoder'
    },
    'vpolloczek': {
        'name': 'Veronika Polloczek',
        'team': _l('associated_scholars'),
        'category': _l('scientific_employee'),
        'titles': ['Mag.a phil.', 'MA'],
        'description':  _l('Mag.a in Classics, Student of MA Program in Historical Research, Auxiliary Sciences and Archival Studies at the University of Vienna. Research interests Medieval Sources, Middle and Neo Latin, Palaeography, Digitalization of Sources, Heraldry.'),
        'email': 'Veronika.Polloczek@oeaw.ac.at',
        'image': f'{PATH}/veronika.png',
        'academia': 'https://oeaw.academia.edu/VeronikaPolloczek'
    },
    'mhernandez': {
        'name': 'Moisés Hernández Cordero',
        'team': 'balkans',
        'category': _l('spatial_analyst'),
        'titles': ['MA', 'MSc'],
        'description':  _l('Degree History 2007 Universidad Autonónoma de Madrid (UAM) MSc, 2011: Master Degree in GIS and Spatial Analysis in Archaeology (Institute of Archaeology, University College London, London) Research Interests: GIS and Spatial Analysis, Geomatics applications in Archaeology, Structure from Motion, UV IR and Multispectral imagery, Deep Learning and Machine Learning for Cultural research.'),
        'email': 'moises.hernandez.cordero@oeaw.ac.at',
        'image': f'{PATH}/moises.jpg',
        'academia': 'https://oeaw.academia.edu/MoisesHernandez'
    },
    'ebeer': {
        'name': 'Elisabeth Charlotte Beer',
        'team': 'cartographer',
        'category': _l('spatial_analyst'),
        'titles': ['Mag.rer.nat'],
        'description':  _l('Mag.rer.nat with distinction in cartography (University of Vienna 1991). Focus in research was the visualization of signatures in maps. espacially economical maps. 1995 Project for evaluation of map- generalizing software on different official maps of different countries. 1996 licence for entrepreneurship. Since 2020 working as self-employed cartographer (CARTOCONSULT BEER). Collaborating since then with the Austrian Academy of Sciences (ÖAW) in Vienna as free cartographer for the Long-Term-Project "Tabula Imperii Byzantini (TIB)".'),
        'email': 'office@beer16.at',
        'image': f'{PATH}/elisabeth.jpg',
        'academia': ''
    },
    'dschmid': {
        'name': 'David Schmid',
        'team': _l('former_employee'),
        'category': _l('scientific_employee'),
        'titles': ['BA'],
        'description':  _l('BA in History, student of medieval history at the University of Vienna. Research interests include historical geography, GIS, late antique and medieval and military history.'),
        'email': 'david.schmid@oeaw.ac.at',
        'image': f'{PATH}/david.jpg',
        'academia': 'https://univie.academia.edu/DavidSchmid'
    },
    'kbelke': {
        'name': 'Klaus Belke',
        'team': _l('emeritus_scholar'),
        'category': _l('scientific_employee'),
        'titles': ['Dr. phil.'],
        'description':  _l('Dr. phil. (University of Vienna and Munich, 1976); 1976–2012 Academic collaborator at the Austrian Academy of Sciences; at the Commission for the Tabula Imperii Byzantini; from 2006 Institute for Byzantine Studies; from 2012 Division of Byzantine Studies of the Institute for Medieval Studies). 1999 Habilitation at the Institute for Byzantine and Neoellenic Studies of the University of Vienna. Teaching at the University of Vienna; 1999, 2001 teaching at the Central European University at Budapest. 2012 retirement after reaching the legal age of retirement. Continuing voluntarily work for the Tabula Imperii Byzantine project. Research Interests: Historical Geography of the Byzantine Empire, esp. Asia Minor Road, means of traffic in the Roman and Byzantine periods.'),
        'email': 'Klaus.Belke@oeaw.ac.at',
        'image': f'{PATH}/klaus.jpg',
        'academia': 'https://oeaw.academia.edu/KlausBelke'
    },
    'fhild': {
        'name': 'Friedrich Hild',
        'team': _l('emeritus_scholar'),
        'category': _l('scientific_employee'),
        'titles': ['Dr. phil.'],
        'description':  _l('Dr. phil.; Studies of Classical Philology, Ancient History, Ancient Numismatics and Byzantine Studies (1960–1968) at the University of Vienna; Dr. phil. in Ancient History. From 1969 scholarly co-worker in the "Kommission für die Tabula Imperii Byzantini / Commission of the Tabula Imperii Byzantini"; 1977-1987: deputy chairman of the TIB. From 1976 until 1986 secretary and treasurer and from 1987 until 1996 treasurer of the "Austrian Byzantine Society / Österreichische Byzantinische Gesellschaft". After his retirement in 2007 he is working as honorary (emeritus) scholar for the TIB. Research Interests: Ancient and Byzantine History, Archaeology, Historical Geography and Cartography of the Mediterranean'),
        'email': 'Friedrich.Hild@oeaw.ac.at',
        'image': f'{PATH}/friedrich.jpg',
        'academia': 'https://oeaw.academia.edu/friedrichhild'
    },
    'psoustal': {
        'name': 'Peter Soustal',
        'team': _l('emeritus_scholar'),
        'category': _l('scientific_employee'),
        'titles': ['Dr. phil.', 'Mag. phil.'],
        'description':  _l('Mag. Dr. phil.; Mag. phil. (University of Vienna, 1969); Dr. phil. (University of Vienna, 1975); employed at the Austrian Academy of Sciences since 1969, from 1973 at the department of Tabula Imperii Byzantini; from 2006 until 2012 director of the former Institute for Byzantine Research of the Austrian Academy of Sciences; since the retirement in 2012 voluntary collaborator at the Institute for Medieval Research, Division of Byzantine Research. Research Interests: Historical Geography of the Southern part of the Balkan peninsula (Albania, Northern Greece, Bulgaria), historical Studies in Place names.'),
        'email': 'Peter.Soustal@oeaw.ac.at',
        'image': f'{PATH}/peter.jpg',
        'academia': 'https://oeaw.academia.edu/PeterSoustal'
    }
}

team_categories = {
    'Heads_of_the_TIB': [
        tib_team_data['akulzer'],
        tib_team_data['mpopovic']],
    'Scientific_Employees': [
        tib_team_data['dariantzi']],
    'Associated_Scholars': [
        tib_team_data['vzervan'],
        tib_team_data['vpolloczek']],
    'Technical_Specialists': [
        tib_team_data['ebeer'],
        tib_team_data['mhernandez'],
        tib_team_data['bkoschicek'],
        tib_team_data['gtheochari']],
    'Former_Employees': [
        tib_team_data['jkoder'],
        tib_team_data['fhild'],
        tib_team_data['kbelke'],
        tib_team_data['psoustal'],
        tib_team_data['dschmid'],
        tib_team_data['dvargova']]
}
