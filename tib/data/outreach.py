from tib.data.team import tib_team_data as team
from tib.util.util import format_link, get_dates_formatted, youtube_iframe
from flask_babel import lazy_gettext as _l

img_path = '/images/icons/outreach/'
attach_path = '/repository/outreach/'
types = {
    'presentation': {
        'name': _l('presentation'),
        'bs_icon': 'bi-chat-text-fill'
    },
    'online_presentation': {
        'name': _l('presentation'),
        'bs_icon': 'bi-chat-right-text-fill'
    },
    'award': {
        'name': _l('award'),
        'bs_icon': 'bi-award'
    },
    'science_fair': {
        'name': _l('science_fair'),
        'bs_icon': 'bi-mortarboard-fill'
    },
    'book_release': {
        'name': _l('book_release'),
        'bs_icon': 'bi-book'
    },
    'blog_post': {
        'name': _l('blogpost'),
        'bs_icon': 'bi-blockquote-right'
    },
}

outreach = [{
    'id': 'imc_leeds_23',
    'type': types['presentation'],
    'date': f"{get_dates_formatted(2023, 7, 6)}",
    'who': [team['mpopovic'], team['dvargova'], team['bkoschicek']],
    'icon': 'imc_leeds_23.jpg',
    'title': _l('TIB Balkans at the IMC Leeds 2023'),
    'description': [_l('imc_leeds_23')],
    'category': ['tib', 'balkan', 'holdura'],
    'attachment': [{
        'path': '',
        'type': ''}]
},{
    'id': 'lead_seals_2022',
    'type': types['presentation'],
    'date': f"{get_dates_formatted(2022, 4, 19)}",
    'who': [
        team['akulzer'], team['mpopovic'], team['psoustal'], team['kbelke']],
    'title': _l('Congress on Byzantine Thrace'),
    'description': [
        _l('The TIB and its retired colleagues took part substantially in the '
           'conference “Lead Seals in Byzantine Thrace” on 19 April 2022 at '
           'the IMAFO of the ÖAW. While Andreas Külzer and Peter Soustal '
           'presented papers, Klaus Belke and Mihailo Popović were chairing '
           'sessions. Finally, Mihailo Popović gave a résumé of the '
           'conference.')
    ],
    'category': ['tib', 'balkan'],
    'attachment': [{
        'path': f'{attach_path}Lead-Seals-in-Byzantine-Thrace.pdf',
        'type': 'pdf'}]
},{
    'id': 'serbian_academy',
    'type': types['presentation'],
    'date': f"{get_dates_formatted(2023, 2, 22)}",
    'who': [team['mpopovic']],
    'title': _l('Presentation at the Serbian Academy of Sciences and Arts'),
    'description': [
        _l('Mihailo Popović was invited by the Institute for Byzantine '
           'Studies of the Serbian Academy of Sciences and Arts to give a paper '
           'entitled “Пројекат Tabula Imperii Byzantini: о будућности (?) '
           'проучавања историјске географије Византије” [“The Project Tabula '
           'Imperii Byzantini: on the Future (?) of the Research in the '
           'Field of the Historical Geography of Byzantium”] on 22 February '
           '2023 in Belgrade.')
    ],
    'category': ['tib', 'balkan'],
    'attachment': [{
        'path': f'{attach_path}MPopovic_SANU Beograd.pdf',
        'type': 'pdf'}]
}, {
    'id': 'les_ciutats_mediterranies',
    'type': types['presentation'],
    'date': f"{get_dates_formatted(2022, 12, 15)}",
    'who': [team['akulzer'], team['mpopovic']],
    'title': _l('Presentation in Barcelona'),
    'description': [
        _l('Andreas Külzer and Mihailo Popović gave a joint paper entitled '
           '"Reality and Mirage in the Eastern Mediterranean. The Long Term '
           'Project Tabula Imperii Byzantini and its Reconstruction Work of '
           'Late Antique and Medieval  Settlements" at the conference “Les '
           'ciutats mediterrànies. Realitat i miratge” in Barcelona, Spain, '
           'on 15 December 2022.')
    ],
    'category': ['tib', 'balkan'],
    'attachment': [{
        'path': f'{attach_path}Prog_Ciutats_Mediterranies_2022.pdf',
        'type': 'pdf'}]
}, {
    'id': 'tib11_promotion',
    'type': types['award'],
    'date': f"{get_dates_formatted(2022, 11, 14)}",
    'who': [team['psoustal'], team['jkoder'], team['mpopovic']],
    'title': _l('Promotion Event for TIB 11'),
    'description': [
        _l('On Monday, 14 November 2022, the TIB volume "Macedonia, '
           'Southern Part" (TIB 11) will be officially promoted '
           'at the Department of Byzantine Research of the Institute for '
           'Medieval Research (IMAFO).'),
        '''<ul class="list-unstyled"><li>'''
        + _l('Date') + ''': 24.11.2022</li><li>''' + _l('Begin') +
        ''': 17:00</li><li>''' + _l('Venue') + ''': Hollandstrasse 11-13, '''
        + _l('1st Floor') + ''', 1020 ''' + _l('Vienna') + '''</li>
          <li>''' + _l('Registration') + ''': <a href="mailto:ekaterini.mitsiou@oeaw.ac.at">
          Ekaterini.Mitsiou@oeaw.ac.at</a></li>
        </ul>'''
    ],
    'category': ['tib', 'balkan'],
    'attachment': [{
        'path': f'{attach_path}ABF_Buchpraesentation_TIB_11.pdf',
        'type': 'pdf'}]
}, {
    'id': 'histgeo_leipzig_22',
    'type': types['presentation'],
    'date': f"{get_dates_formatted(2022, 11, 10)}",
    'who': [team['mpopovic']],
    'title': _l('Presentation in Leipzig'),
    'description': [
        _l('On Thursday, 10 November 2022, Mihailo Popović will present a paper in Leipzig, which is entitled “Die historische Geographie von Byzanz neu gedacht – Über den Wert der digitalen Kartographie und Geokommunikation in der Vermittlung historischer Inhalte am Beispiel des Projektes ‚Jenseits von Ost und West‘” and is based on scholarly results from the project <a href="subprojects/holdura>“Beyond East and West (HOLDURA)”</a>'),
    ],
    'category': ['tib', 'balkan'],
    'attachment': [{
        'path': f'{attach_path}Popovic_11_22.pdf',
        'type': 'pdf'}]
}, {
    'id': 'aieb_roundtable',
    'type': types['online_presentation'],
    'date': f"{get_dates_formatted(2022, 8, 22)}-"
            f"{get_dates_formatted(2022, 8, 27)}",
    'who': [team['mpopovic']],
    'title': _l(
        '24th International Congress of Byzantine Studies in Venice '
        'and Padua'),
    'description': [
        _l('aieb_roundtable'),
        _l('For further information and the programme please cf.'),
        format_link('https://byzcongress2022.org/')],
    'category': ['tib', 'balkan'],
    'attachment': []
}, {
    'id': 'hypotheses_post',
    'type': types['blog_post'],
    'date': f"{get_dates_formatted(2022, 8, 15)}-"
            f"{get_dates_formatted(2022, 8, 15)}",
    'who': [team['mpopovic'], team['bkoschicek']],
    'title': _l(
        'Blogpost on the Paper "OpenAtlas und historische Geographie"'),
    'description': [
        _l('hypotheses_post'),
        format_link('https://dhc.hypotheses.org/2053')],
    'category': ['tib', 'balkan'],
    'attachment': []
}, {
    'id': 'tib11_release',
    'type': types['book_release'],
    'date': get_dates_formatted(2022, 7, 26),
    'who': [team['psoustal'], team['mpopovic']],
    'title': _l('TIB volume 11, Macedonia, Southern Part published'),
    'description': [
        _l('tib_11_release'),
        _l('Cf. in detail:'),
        format_link(
            'https://verlag.oeaw.ac.at/en/product/makedonien-suedlicher-teil'
            '/99200596')],
    'category': ['tib', 'balkan'],
    'attachment': [{
        'path': f'{attach_path}TIB_11_macedonia_southern_part.pdf',
        'type': 'pdf'}]
}, {
    'id': 'imc2022',
    'type': types['online_presentation'],
    'date': get_dates_formatted(2022, 7, 6),
    'who': [team['mhernandez'], team['bkoschicek'], team['vpolloczek'],
            team['mpopovic'], team['dvargova'], team['vzervan']],
    'title': _l(
        'presentation at International Medieval Congress (IMC) in Leeds'),
    'description': [
        _l('imc2022'),
        _l('Cf. in detail'),
        format_link('https://www.imc.leeds.ac.uk/imc-2022/programme/')],
    'category': ['tib', 'balkan'],
    'attachment': []
}, {
    'id': 'seminar_koeln',
    'type': types['online_presentation'],
    'date': get_dates_formatted(2022, 6, 23),
    'who': [team['bkoschicek'], team['mpopovic']],
    'title': _l('presentation at university of cologne, germany'),
    'description': [
        _l('seminar_koeln'),
        youtube_iframe('https://www.youtube-nocookie.com/embed/cmJo9N05WY4')],
    'category': ['tib', 'balkan'],
    'attachment': []
}, {
    'id': 'lange_nacht_22',
    'type': types['science_fair'],
    'date': get_dates_formatted(2022, 5, 20),
    'who': [team['dvargova']],
    'title': _l('TIB at the "Lange Nacht der Forschung" in Vienna'),
    'description': [
        _l('lange_nacht_22_text'),
        youtube_iframe('https://www.youtube-nocookie.com/embed/Nhdx2OeWkN8')],
    'category': ['tib', 'balkan'],
    'attachment': []
}, {
    'id': 'global_eurasia_5_12_22',
    'type': types['presentation'],
    'date': get_dates_formatted(2022, 5, 12),
    'who': [team['mpopovic']],
    'title': _l(
        'presentation at "Global Eurasia – Comparison and Connectivity II: '
        'Agency, Networks and Transregional Contexts"'),
    'description': [_l('global_eurasia_5_12_22')],
    'category': ['tib', 'balkan'],
    'attachment': []
}, {
    'id': 'seminar_series_april',
    'type': types['online_presentation'],
    'date': get_dates_formatted(2022, 4, 1),
    'who': [team['mpopovic']],
    'title': _l(
        'On the Use and Usefulness of Digital Humanities in the Historical '
        'Geography of Byzantium'),
    'description': [_l('seminar_series_april')],
    'category': ['tib', 'balkan'],
    'attachment': [{
        'path': f'{attach_path}Seminar-Poster-Popovic.pdf',
        'type': 'pdf'}]
},
]
