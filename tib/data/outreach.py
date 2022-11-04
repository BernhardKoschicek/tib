from tib.data.tib.team import tib_team_data as team
from tib.util.util import format_link, format_video_tag, \
    get_dates_formatted, youtube_iframe
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
    'id': 'tib11_promotion',
    'type': types['award'],
    'date': f"{get_dates_formatted(2022, 11, 14)}",
    'who': [team['psoustal'], team['jkoder'], team['mpopovic']],
    'title': 'Promotion Event for TIB 11',
    'description': """<p>
        On Monday, 14 November 2022, the TIB volume “Macedonia, Southern Part” (TIB 11) will be officially promoted at the 
Department of Byzantine Research of the Institute for Medieval Research (IMAFO).
          </p>
          <ul class="list-unstyled">
          <li>Date: 24.11.2022</li>
          <li>Begin: 17:00</li>
          <li>Venue: Hollandstrasse 11-13, 1st Floor, 1020 Vienna</li>
          <li>Registration: <a href="mailto:ekaterini.mitsiou@oeaw.ac.at">Ekaterini.Mitsiou@oeaw.ac.at</a></li>
        </ul>
        """,
    'category': ['tib', 'balkan'],
    'attachment': [{
        'path': f'{attach_path}ABF_Buchpraesentation_TIB_11.pdf',
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
        youtube_iframe('https://www.youtube.com/embed/cmJo9N05WY4')],
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
        format_video_tag('EW_Lange_Nacht_der_Forschung_2022.mp4')],
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
