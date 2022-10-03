from tib.data.tib.team import tib_team_data as team
from tib.util.util import format_link, format_link_text, get_dates_formatted, \
    youtube_iframe
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
    'id': 'tib11_release',
    'type': types['book_release'],
    'date': get_dates_formatted(2022, 7, 26),
    'who': [team['psoustal'], team['mpopovic']],
    'title': _l('TIB volume 11, Macedonia, Southern Part') + _l('published'),
    'description': [
        _l('tib_11_release'),
        _l('Cf. in detail:'),
        format_link(
            'https://verlag.oeaw.ac.at/en/product/makedonien-suedlicher-teil'
            '/99200596')
    ],
    # f"""<p>
    # It is with great pleasure that we may announce the publication of the
    # TIB Volume 11 ("Macedonia, Southern Part") written by Peter Soustal
    # (with Andreas Pülz and Mihailo St. Popović as co-authors).
    # </p>
    # <p>: <a
    # href="https://verlag.oeaw.ac.at/en/product/makedonien
    # -suedlicher-teil/99200596" target="_blank">https://verlag.oeaw.ac.at/
    # en/product/makedonien-suedlicher-teil/99200596</a>
    # </p>
    # """,
    'category': ['tib', 'balkan'],
    'attachment': [{
        'path': f'{attach_path}TIB_11_macedonia_southern_part.pdf',
        'type': 'pdf'}]
}, {
    'id': 'seminar_series_april',
    'type': types['online_presentation'],
    'date': get_dates_formatted(2022, 4, 1),
    'who': [team['mpopovic']],
    'title': _l(
        'On the Use and Usefulness of Digital Humanities in the Historical '
        'Geography of Byzantium'),
    'description': _l('seminar_series_april'),
    # f"""<p>
    # Mihailo Popović gave an online paper entitled “On the Use and
    # Usefulness of Digital Humanities in the Historical Geography of
    # Byzantium” on 1 April 2022 in front of students and colleagues of the
    # Aristotle University in Thessalonica and the Ibn Haldun University in
    # Istanbul. This paper is part of a seminar series with the title “The
    # Balkans Between Empires”. After the paper the audience asked manifold
    # questions on the Historical Geography of the Byzantine Empire and
    # Digital Humanities.
    # </p>
    # """,
    'category': ['tib', 'balkan'],
    'attachment': [{
        'path': f'{attach_path}Seminar-Poster-Popovic.pdf',
        'type': 'pdf'}]
}, {
    'id': 'global_eurasia_5_12_22',
    'type': types['presentation'],
    'date': get_dates_formatted(2022, 5, 12),
    'who': [team['mpopovic']],
    'title': _l('presentation at') +
             "Global Eurasia – Comparison and "
             "Connectivity II: Agency, Networks and Transregional Contexts",
    'description': _l('global_eurasia_5_12_22'),
    #     f"""<p>
    #     Mihailo Popović  presented a
    # paper on the TIB at the conference <a href="https://www.oeaw.ac.at/en/
    # global-eurasia/detail/news-detail/handlungsspielraeume-netzwerke-und-
    # transregionale-kontexte" target="_blank">“Global Eurasia – Comparison and
    # Connectivity II: Agency, Networks and Transregional Contexts”</a> at the
    # IMAFO (ÖAW).
    #     </p>
    #     """,
    'category': ['tib', 'balkan'],
    'attachment': []
}, {
    'id': 'lange_nacht_22',
    'type': types['science_fair'],
    'date': get_dates_formatted(2022, 5, 20),
    'who': [team['dvargova']],
    'title': _l('TIB at the "Lange Nacht der Forschung" in Vienna'),
    'description': _l('lange_nacht_22'),
    # """<p>
    # Dorota Vargová represents the Long Term Project TIB at the <a
    # href='https://www.oeaw.ac.at/lange-nacht-der-forschung'>
    # "Lange Nacht der Forschung"</a> in Vienna. in Vienna. She will welcome
    # the interested public, present insights in our current research and
    # stage a quiz for children.
    # </p>
    # """,
    'category': ['tib', 'balkan'],
    'attachment': []
}, {
    'id': 'seminar_koeln',
    'type': types['online_presentation'],
    'date': get_dates_formatted(2022, 6, 23),
    'who': [team['bkoschicek'], team['mpopovic']],
    'title': _l('presentation at') + _l('university of cologne') + ', ' + _l(
        'germany'),
    'description': [
        _l('seminar_koeln') + format_link_text(
            'https://dhc.hypotheses.org/programm-2022',
            _l('Digital Humanities colloquium')),
        youtube_iframe('https://www.youtube.com/embed/cmJo9N05WY4')],
    #     f"""<p>
    #    Bernhard Koschiček-Krombholz and Mihailo St. Popović
    #     present a paper on “OpenAtlas und historische Geographie: Die Tabula
    # Imperii Byzantini (Balkan) im digitalen Zeitalter” at the University of
    # Cologne, Germany at an <a
    # href="https://dhc.hypotheses.org/programm-2022"
    # target=_blank">Digital Humanities colloquium</a>.</p>
    #
    # <iframe width="560" height="315"
    # src="https://www.youtube.com/embed/cmJo9N05WY4" title="YouTube video
    # player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
    # encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    #     """,
    'category': ['tib', 'balkan'],
    'attachment': []
}, {
    'id': 'imc2022',
    'type': types['online_presentation'],
    'date': get_dates_formatted(2022, 7, 6),
    'who': [team['mhernandez'], team['bkoschicek'], team['vpolloczek'],
            team['mpopovic'], team['dvargova'], team['vzervan']],
    'title': _l('presentation at')
             + 'International Medieval Congress (IMC) in Leeds',
    'description': [
        _l('imc2022'),
        _l('Cf. in detail'),
        format_link('https://www.imc.leeds.ac.uk/imc-2022/programme/')],
    # During the International Medieval Congress (IMC) in Leeds from 4 to 7
    # July 2022 the team of the TIB Balkans will present its research in the
    #
    # sessions No. 1034, 1134, 1234 and 1334 on Wednesday, 6 July.
    # </p>
    'category': ['tib', 'balkan'],
    'attachment': []
}, {
    'id': 'aieb_roundtable',
    'type': types['online_presentation'],
    'date': f"{get_dates_formatted(2022, 8, 22)}-"
            f"{get_dates_formatted(2022, 8, 27)}",
    'who': [team['mpopovic']],
    'title': _l('24th International Congress of Byzantine Studies in Venice '
                'and Padua'),
    'description': [
        _l('aieb_roundtable'),
        _l('For further information and the programme please cf.'),
        format_link('https://byzcongress2022.org/')],

    #  The “Commission for the Historical Geography and Spatial Analysis of
    #  Byzantium” of the AIEB is organising a Round Table entitled
    #  “Historical Geography of Byzantium in a Digital Age: Chances and
    #  Risks” at the 24th International Congress of Byzantine Studies in
    #  Venice and Padua (22 to 27 August 2022). It will take place on 23
    #  August in Venice. On Thursday, 25 August, Mihailo St. Popović will
    #  give a Plenary Paper entitled “A Race against Time: The Impact of
    #  Contemporary Environmental and Demographic Change on the Research of
    #  the Historical Geography of Byzantium” within the Plenary Session
    #  “Bridging Interdisciplinary Gaps: New Ways of Making Connections” in
    #  Padua, which will be chaired by Professor Judith Herrin.
    #    </p><p>
    #  {_l('For further information and the programme please cf.')}
    #  <a href="https://byzcongress2022.org/" target=_blank>
    #  https://byzcongress2022.org/</a>
    # </p>""",
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
    #  """<p>
    #  The paper “OpenAtlas und historische Geographie: Die Tabula Imperii
    #   Byzantini (Balkan) im digitalen Zeitalter” by Bernhard
    #   Koschiček-Krombholz and Mihailo St. Popović is presented and
    #   commented in a blogpost by a student of the University of Cologne:
    #    </p><p>
    #  <a href="https://dhc.hypotheses.org/2053" target=_blank>
    #  https://dhc.hypotheses.org/2053</a>
    # </p>
    #  """,
    'category': ['tib', 'balkan'],
    'attachment': []
},
]
