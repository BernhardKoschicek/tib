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

outreach = [{
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
}, {
    'id': 'global_eurasia_5_12_22',
    'type': types['presentation'],
    'date': datetime(2022, 5, 12).strftime('%d.%m.%Y'),
    'who': [team['mpopovic']],
    'title': 'Presentation at “Global Eurasia – Comparison and Connectivity '
             'II: Agency, Networks and Transregional Contexts”',
    'icon': '',
    'description': """<p>
        Mihailo Popović  presented a 
    paper on the TIB at the conference “Global Eurasia – Comparison and 
    Connectivity II: Agency, Networks and Transregional Contexts” at the 
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
    'icon': '',
    'description': """<p>
        Dorota Vargová represents the Long Term Project TIB will at the <a 
        href='https://www.oeaw.ac.at/175-jahre/events/lange-nacht-der-
        forschung'>
        "Lange Nacht der Forschung"</a> in Vienna. Dorota Vargová will 
        welcome the interested public and present insights in our current 
        research.
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
    'icon': '',
    'description': """<p>
       Bernhard Koschiček-Krombholz and Mihailo St. Popović
        present a paper on “OpenAtlas und historische Geographie: Die Tabula 
    Imperii Byzantini (Balkan) im digitalen Zeitalter” at the University of 
    Cologne, Germany.</p>
        """,
    'category': ['tib', 'balkan'],
    'attachment': []},
]
