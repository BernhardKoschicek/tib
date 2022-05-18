from datetime import datetime

img_path = '/images/icons/outreach/'
attach_path = '/repository/outreach/'
types = {
    'presentation': {
        'name': 'Präsentation',
        'bt_icon': ''
    },
    'online_presentation': {
        'name': 'Präsentation',
        'bt_icon': ''
    },
}

outreach = [{
    'id': 'seminar_series_april',
    'type': types['online_presentation'],
    'date': datetime(2022, 4, 1).strftime('%d %B %Y'),
    'title': 'On the Use and Usefulness of Digital Humanities in the Historical Geography of Byzantium ',
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
    'attachment': [{
        'path': f'{attach_path}Seminar-Poster-Popovic.pdf',
        'type': 'pdf'
    }]
},
]
