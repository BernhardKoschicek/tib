from datetime import datetime
from tib.data.tib.team import tib_team_data as team

news = [{
    'date': datetime(2022, 5, 12).strftime('%d %B %Y'),
    'who': [team['mpopovic']],
    'title': 'will present a paper at the  IMAFO (ÖAW) in Vienna',
    'text': """
    will present a 
    paper on the TIB at the conference “Global Eurasia – Comparison and 
    Connectivity II: Agency, Networks and Transregional Contexts” at the 
    IMAFO (ÖAW).
    """
}, {
    'date': datetime(2022, 5, 20).strftime('%d %B %Y'),
    'who': [team['dvargova']],
    'title': 'will represent the Long Term Project TIB will at the "Lange '
             'Nacht der Forschung" in Vienna',
    'text': """
    will represent the Long Term Project TIB will at the <a href="
    https://www.oeaw.ac.at/175-jahre/events/lange-nacht-der-forschung"
    "Lange Nacht der Forschung" in Vienna. Dorota Vargová will 
    welcome the interested public and present insights in our current research.
    """
}, {
    'date': datetime(2022, 5, 20).strftime('%d %B %Y'),
    'who': [team['bkoschicek'], team['mpopovic']],
    'title': 'will present a pape at the University of Cologne, Germany',
    'text': """
    will present a paper on “OpenAtlas und historische Geographie: Die Tabula 
    Imperii Byzantini (Balkan) im digitalen Zeitalter” at the University of 
    Cologne, Germany.
    """
},
]
