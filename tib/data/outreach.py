from datetime import datetime

from tib.data.tib.team import tib_team_data as team

img_path = '/images/icons/outreach/'
attach_path = '/repository/outreach/'
types = {
    'presentation': {
        'name': 'Präsentation',
        'bs_icon': 'bi-chat-text-fill'
    },
    'online_presentation': {
        'name': 'Präsentation',
        'bs_icon': 'bi-chat-right-text-fill'
    },
    'award': {
        'name': '',
        'bs_icon': 'bi-award'
    },
    'science_fair': {
        'name': 'Präsentation',
        'bs_icon': 'bi-mortarboard-fill'
    },
}

outreach_ger = [{
    'id': 'seminar_series_april',
    'type': types['online_presentation'],
    'date': datetime(2022, 4, 1).strftime('%d.%m.%Y'),
    'who': [team['mpopovic']],
    'title': 'On the Use and Usefulness of Digital Humanities in the '
             'Historical Geography of Byzantium ',
    'icon': f'{img_path}seminar_series_icon.jpg',
    'description': """<p>
        Mihailo Popović hat am 1. April 2022 einen Online-Vortrag mit dem 
        Titel <i>On the Use and Usefulness of Digital Humanities in the 
        Historical Geography of Byzantium</i> vor Studierenden der Aristoteles 
        Universität in Thessaloniki und der Ibn Haldun Universität in 
        Istanbul gehalten. Dieser Vortrag war Teil der Seminarreihe The 
        Balkans Between Empires. Nach einem einstündigen Vortrag haben die 
        ZuhörerInnen zahlreiche Fragen gestellt, sodaß in weiteren 45 Minuten 
        spannende Fragen zur Historischen Geographie des Byzantinischen 
        Reiches und zu den digitalen Geisteswissenschaften erörtert werden 
        konnte.
        </p>
        """,
    'category': ['balkan'],
    'attachment': [{
        'path': f'{attach_path}Seminar-Poster-Popovic.pdf',
        'type': 'pdf'}]
}]

outreach = [{
    'id': 'seminar_series_april',
    'type': types['online_presentation'],
    'date': datetime(2022, 4, 1).strftime('%d.%m.%Y'),
    'who': [team['mpopovic']],
    'title': 'On the Use and Usefulness of Digital Humanities in the '
             'Historical Geography of Byzantium ',
    'description': """<p>
        Mihailo Popović gave an online paper entitled “On the Use and 
        Usefulness of Digital Humanities in the Historical Geography of 
        Byzantium” on 1 April 2022 in front of students and colleagues of the 
        Aristotle University in Thessalonica and the Ibn Haldun University in 
        Istanbul. This paper is part of a seminar series with the title “The 
        Balkans Between Empires”. After the paper the audience asked manifold 
        questions on the Historical Geography of the Byzantine Empire and 
        Digital Humanities.
        </p>
        """,
    'category': ['tib', 'balkan'],
    'attachment': [{
        'path': f'{attach_path}Seminar-Poster-Popovic.pdf',
        'type': 'pdf'}]
}, {
    'id': 'global_eurasia_5_12_22',
    'type': types['presentation'],
    'date': datetime(2022, 5, 12).strftime('%d.%m.%Y'),
    'who': [team['mpopovic']],
    'title': 'Presentation at “Global Eurasia – Comparison and Connectivity '
             'II: Agency, Networks and Transregional Contexts”',
    'description': """<p>
        Mihailo Popović  presented a 
    paper on the TIB at the conference <a href="https://www.oeaw.ac.at/en/
    global-eurasia/detail/news-detail/handlungsspielraeume-netzwerke-und-
    transregionale-kontexte" target="_blank">“Global Eurasia – Comparison and 
    Connectivity II: Agency, Networks and Transregional Contexts”</a> at the 
    IMAFO (ÖAW).
        </p>
        """,
    'category': ['tib', 'balkan'],
    'attachment': []
}, {
    'id': 'lange_nacht_22',
    'type': types['science_fair'],
    'date': datetime(2022, 5, 20).strftime('%d.%m.%Y'),
    'who': [team['dvargova']],
    'title': 'TIB at the "Lange Nacht der Forschung" in Vienna',
    'description': """<p>
        Dorota Vargová represents the Long Term Project TIB at the <a 
        href='https://www.oeaw.ac.at/lange-nacht-der-forschung'>
        "Lange Nacht der Forschung"</a> in Vienna. in Vienna. She will welcome 
        the interested public, present insights in our current research and 
        stage a quiz for children.
        </p>
        """,
    'category': ['tib', 'balkan'],
    'attachment': []
}, {
    'id': 'seminar_koeln',
    'type': types['online_presentation'],
    'date': datetime(2022, 6, 23).strftime('%d.%m.%Y'),
    'who': [team['bkoschicek'], team['mpopovic']],
    'title': 'Presentation at the University of Cologne, Germany',
    'description': """<p>
       Bernhard Koschiček-Krombholz and Mihailo St. Popović
        present a paper on “OpenAtlas und historische Geographie: Die Tabula 
    Imperii Byzantini (Balkan) im digitalen Zeitalter” at the University of 
    Cologne, Germany at an <a href="https://dhc.hypotheses.org/programm-2022" 
    target=_blank">Digital Humanities colloquium</a>.</p>
        """,
    'category': ['tib', 'balkan'],
    'attachment': []
}, {
    'id': 'imc2022',
    'type': types['online_presentation'],
    'date': datetime(2022, 7, 6).strftime('%d.%m.%Y'),
    'who': [team['mhernandez'], team['bkoschicek'], team['vpolloczek'],
            team['mpopovic'], team['dvargova'], team['vzervan']],
    'title': 'Presentation at the International Medieval Congress (IMC) in '
             'Leeds',
    'description': """<p>
       During the International Medieval Congress (IMC) in Leeds from 4 to 7 
       July 2022 the team of the TIB Balkans will present its research in the 
       <a href="https://www.imc.leeds.ac.uk/imc-2022/programme/" target=_blank>
       sessions No. 1034, 1134, 1234 and 1334 on Wednesday, 6 July</a>.
       </p>
        """,
    'category': ['tib', 'balkan'],
    'attachment': []
}, {
    'id': 'aieb_roundtable',
    'type': types['online_presentation'],
    'date': f"{datetime(2022, 8, 22).strftime('%d.%m.%Y')}-"
            f"{datetime(2022, 8, 27).strftime('%d.%m.%Y')}",
    'who': [team['mpopovic']],
    'title': '24th International Congress of Byzantine Studies in Venice and '
             'Padua',
    'description': """<p>
        The “Commission for the Historical Geography and Spatial Analysis of 
        Byzantium” of the AIEB is organising a Round Table entitled 
        “Historical Geography of Byzantium in a Digital Age: Chances and 
        Risks” at the 24th International Congress of Byzantine Studies in 
        Venice and Padua (22 to 27 August 2022). It will take place on 23 
        August in Venice. On Thursday, 25 August, Mihailo St. Popović will 
        give a Plenary Paper entitled “A Race against Time: The Impact of 
        Contemporary Environmental and Demographic Change on the Research of 
        the Historical Geography of Byzantium” within the Plenary Session 
        “Bridging Interdisciplinary Gaps: New Ways of Making Connections” in 
        Padua, which will be chaired by Professor Judith Herrin. 
          </p><p>
        For further information and the programme please cf. 
        <a href="https://byzcongress2022.org/" target=_blank>
        https://byzcongress2022.org/</a>
       </p>
        """,
    'category': ['tib', 'balkan'],
    'attachment': []
},
]
