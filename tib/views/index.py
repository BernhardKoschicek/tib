from collections import OrderedDict

from flask import render_template

from tib import app


@app.route('/')
def home() -> str:
    front_menu = OrderedDict([
        ('longterm', {
            'id': '1',
            'image': 'oeffentlich.jpg',
            'title': 'Long Term Project',
            'subtitle': 'Langzeitprojekt Stand und Geschichte'
        }),
        ('subprojekte', {
            'id': '2',
            'image': 'projekte.jpg',
            'title': 'Subprojekte',
            'subtitle': 'Übersicht über alle Projekte'
        }),
        ('digital', {
            'id': '3',
            'image': 'Österreich-Europa-Karte.png',
            'title': 'Digitale Tools',
            'subtitle': 'Digitales Tools der TIB'
        }),
        ('team', {
            'id': '4',
            'image': 'team.jpg',
            'title': 'Team',
            'subtitle': 'Vorstellung des Teams'
        })
    ])

    home_gallery = {
        'lageplan.jpg': 'Lageplan des Flüchtlingslagers Oberhollabrunn '
                        '(<a href="http://www.ffhollabrunn.at/index.php?option=com_content&view=article&id=1159:kommandantentafel&catid=98:geschichte&Itemid=71" target="_blank">http://www.ffhollabrunn.at/</a>)',
        'lager_oberhollabrunn.jpg': 'Das Eingangstor zum k.k. Flüchtlingslager Oberhollabrunn im Jahre'
                                    ' 1916 Ecke Wienerstraße/Dr. Kutschergasse, 2020 Hollabrunn'
                                    ' (<a href="https://regiowiki.at/wiki/Datei:Stockerau_Fl%C3%BCchtlingslager.jpg" target="_blank">Wikipedia</a>)',
        'totenschaubefund.jpg': 'Beispiel eines Totenbeschaubefundes (Metropolis von Austria,'
                                ' Archiv der griech.-orient. Kirchengemeinde zur Hl. Dreifaltigkeit, 1010 Wien)',
        'sveti_sava.jpg': 'Die serbisch-orthodoxe Kirche zum Heiligen Sava in 1030 Wien (Mihailo St. Popović)',
        'unterschrift_velimirovic.jpg': 'Unterschrift des Hl. Bischofs Nikolaj Velimirović (1881-1956) im Evangelium der Kirche des Hl. Sava (Mihailo St. Popović)',
        'uros_predic.jpg': 'Ölgemälde des ersten serbischen Erzbischofs des Hl. Sava von Uroš Predić (1857-1953) (Mihailo St. Popović)'
    }

    return render_template('home.html', front_menu=front_menu, home_gallery=home_gallery)





@app.errorhandler(404)
def page_not_found(e: Exception) -> tuple:
    return render_template('404.html', e=e), 404
