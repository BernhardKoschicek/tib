from collections import OrderedDict

from flask import render_template

from tib import app


@app.route('/')
def home() -> str:
    front_menu = OrderedDict([
        ('longterm', {
            'id': '1',
            'image': 'oeffentlich.jpg',
            'title': 'Long-Term-Project',
            'subtitle': 'Langzeitprojekt Stand und Geschichte'
        }),
        ('subprojekte', {
            'id': '2',
            'image': 'projekte.jpg',
            'title': 'Subprojects',
            'subtitle': 'Übersicht über alle Projekte'
        }),
        ('digital', {
            'id': '3',
            'image': 'Österreich-Europa-Karte.png',
            'title': 'Digital Tools',
            'subtitle': 'Digitales Tools der TIB'
        })
    ])

    return render_template('home.html', front_menu=front_menu)


@app.errorhandler(404)
def page_not_found(e: Exception) -> tuple:
    return render_template('404.html', e=e), 404
