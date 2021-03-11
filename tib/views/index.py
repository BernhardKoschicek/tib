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

    news = OrderedDict([
        ('1', {
            'header': 'New publication',
            'content': 'New publication by the TIB in the fields of Historical Geography and History'
                       ' of Science entitled <a href="https://akademskaknjiga.com/en/katalog/raum-und-geschichte-der-historische-atlas-tabula-imperii-byzantini-an-der-osterreichischen-akademie-der-wissenschaften/" target="_blank">'
                       '"Raum und Geschichte: der Historische Atlas \"Tabula Imperii Byzantini\" an'
                       ' der Österreichischen Akademie der Wissenschaften"</a>'
        }),
        ('2', {
            'header': 'Report on Relief Map',
            'content': 'Report in the blog of the Austrian Newspaper "Der Standard" on our Sub-Project "Cultural Heritage in Times of World War I": <br/>'
                       '<a href="https://www.derstandard.at/story/2000117505690/montenegro-im-relief-terra-incognita-auf-dem-balkan" target="_blank">'
                       'https://www.derstandard.at/story/2000117505690/montenegro-im-relief-terra-incognita-auf-dem-balkan</a>'
        }),
        ('3', {
            'header': 'TIB 13 Published',
            'content': 'It is our great pleasure to announce the publication of the TIB volume 13 on "Bithynien und Hellespont" by our colleague Klaus Belke. For further details please cf.'
                       ' <a href="https://verlag.oeaw.ac.at/Bithynien-und-Hellespont" target="_blank">'
                       'https://verlag.oeaw.ac.at/Bithynien-und-Hellespont</a>'
        })
    ])

    return render_template('home.html', front_menu=front_menu, news=news)


@app.errorhandler(404)
def page_not_found(e: Exception) -> tuple:
    return render_template('404.html', e=e), 404
