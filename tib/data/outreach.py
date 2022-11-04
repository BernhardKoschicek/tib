from tib.data.tib.team import tib_team_data as team
from tib.util.util import get_dates_formatted

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
    'book_release': {
        'name': 'Publikation',
        'bs_icon': 'bi-book'
    },
    'blog_post': {
        'name': 'Blog Post',
        'bs_icon': 'bi-blockquote-right'
    },

}

outreach_ger = [{
    'id': 'tib11_release',
    'type': types['online_presentation'],
    'date': get_dates_formatted(2022, 4, 1),
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
}, {
    'id': 'hypotheses_post',
    'type': types['blog_post'],
    'date': f"{get_dates_formatted(2022, 8, 15)}-"
            f"{get_dates_formatted(2022, 8, 15)}",
    'who': [team['mpopovic'], team['bkoschicek']],
    'title': 'Blogpost on the Paper “OpenAtlas und historische Geographie”',
    'description': """<p>
        The paper “OpenAtlas und historische Geographie: Die Tabula Imperii
         Byzantini (Balkan) im digitalen Zeitalter” by Bernhard 
         Koschiček-Krombholz and Mihailo St. Popović is presented and 
         commented in a blogpost by a student of the University of Cologne:
          </p><p>
        <a href="https://dhc.hypotheses.org/2053" target=_blank>
        https://dhc.hypotheses.org/2053</a>
       </p>
        """,
    'category': ['tib', 'balkan'],
    'attachment': []
}, {
    'id': 'tib11_release',
    'type': types['book_release'],
    'date': get_dates_formatted(2022, 7, 26),
    'who': [team['psoustal'], team['mpopovic']],
    'title': 'TIB Volume 11 ("Macedonia, Southern Part") published',
    'description': """<p>
        It is with great pleasure that we may announce the publication of the 
        TIB Volume 11 ("Macedonia, Southern Part") written by Peter Soustal 
        (with Andreas Pülz and Mihailo St. Popović as co-authors).
        </p>
        <p>
        Cf. in detail: <a href="https://verlag.oeaw.ac.at/en/product/makedonien
        -suedlicher-teil/99200596" target="_blank">https://verlag.oeaw.ac.at/
        en/product/makedonien-suedlicher-teil/99200596</a>
        </p>
        """,
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
    'id': 'seminar_koeln',
    'type': types['online_presentation'],
    'date': get_dates_formatted(2022, 6, 23),
    'who': [team['bkoschicek'], team['mpopovic']],
    'title': 'Presentation at the University of Cologne, Germany',
    'description': """<p>
       Bernhard Koschiček-Krombholz and Mihailo St. Popović
        present a paper on “OpenAtlas und historische Geographie: Die Tabula 
    Imperii Byzantini (Balkan) im digitalen Zeitalter” at the University of 
    Cologne, Germany at an <a href="https://dhc.hypotheses.org/programm-2022" 
    target=_blank">Digital Humanities colloquium</a>.</p>
 <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/cmJo9N05WY4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> """,
    'category': ['tib', 'balkan'],
    'attachment': []
}, {
    'id': 'lange_nacht_22',
    'type': types['science_fair'],
    'date': get_dates_formatted(2022, 5, 20),
    'who': [team['dvargova']],
    'title': 'TIB at the "Lange Nacht der Forschung" in Vienna',
    'description': """<p>
        In May 2022, the Austrian Academy of Sciences co-hosted and 
        participated in the Austrian nationwide event "Lange Nacht der 
        Forschung 2022" (Science Night 2022). This provided another excellent 
        opportunity for the Long-Term Project Tabula Imperii Byzantini (TIB) 
        to communicate its newest research output to the public. At the stand 
        of the academy's Institute for Medieval Research, the TIB-team 
        organized fun discovery activities such as the Historical Geographer's 
        Quiz for all ages and presented the everyday work of a TIB researcher 
        in a custom-made short film, here based on the sub-project <a href="/subprojects/holdura">"Beyond 
        East and West: Geocommunicating the Sacred Landscapes of “Duklja” and 
        “Raška” through Space and Time (11th-14th Cent.)</a>. 
        </p>
        <div class="col align-self-center text-center">
            <video loop muted autoplay controls>
              <source
                src="/static/video/BEW_Lange_Nacht_der_Forschung_2022.mp4"
                type="video/mp4">
              Your browser does not support the video tag.
            </video>
        </div>
        """,
    'category': ['tib', 'balkan'],
    'attachment': []
}, {
    'id': 'global_eurasia_5_12_22',
    'type': types['presentation'],
    'date': get_dates_formatted(2022, 5, 12),
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
    'id': 'seminar_series_april',
    'type': types['online_presentation'],
    'date': get_dates_formatted(2022, 4, 1),
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
},
]
