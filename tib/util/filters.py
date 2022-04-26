from typing import Iterator

import flask
from flask import url_for
from markupsafe import Markup

from tib.data.tib.digtib import digtib_bar

blueprint: flask.Blueprint = flask.Blueprint('filters', __name__)

INSTITUTES = {
    'ZF': {
        'name': 'Zukunftsfonds',
        'url': 'http://www.zukunftsfonds-austria.at/',
        'logo': 'zf_logo.jpg',
        'member': '',
        'address': ''},
    'MT': {
        'name': 'Metropolis von Austria',
        'url': 'http://www.metropolisvonaustria.at/',
        'logo': 'metropolis.png',
        'member': 'S. Em. Metropolit Arsenios von Austria',
        'address': 'Fleischmarkt 13<br>1010 Wien<br>Österreich'},
    'OEAW': {
        'name': 'Austrian Academy of Sciences',
        'url': 'https://www.oeaw.ac.at/',
        'logo': 'oeaw.png',
        'member': '',
        'address': ''},
    'IMAFO': {
        'name': 'Institute for Medieval Research',
        'url': 'https://www.oeaw.ac.at/imafo/',
        'logo': 'imafo.png',
        'member': '',
        'address': ''},
    'ABF': {
        'name': 'Abteilung Byzanzforschung (ABF)',
        'url': 'https://www.oeaw.ac.at/en/byzantine-research/',
        'logo': 'byzantine_research.jpg',
        'member': 'Österreichische Akademie der Wissenschaften (ÖAW) '
                  '<br> Institut für Mittelalterforschung (IMAFO)',
        'address': 'Hollandstraße 11-13<br> 1020 Wien<br> Österreich'},
    'ACDH': {
        'name': 'Austrian Centre for Digital Humanities and Cultural Heritage',
        'url': 'https://www.oeaw.ac.at/acdh/',
        'logo': 'acdh.png',
        'member': '',
        'address': ''},
    'univie': {
        'name': 'University of Vienna',
        'url': 'https://www.univie.ac.at/',
        'logo': 'uni_vienna.jpg',
        'member': '',
        'address': ''},
    'FWF': {
        'name': 'Austrian Science Fund',
        'url': 'https://www.fwf.ac.at/',
        'logo': 'fwf.png',
        'member': '',
        'address': ''},
    'OeAI': {
        'name': 'Austrian Archaeological Institute',
        'url': 'https://www.oeaw.ac.at/oeai/',
        'logo': 'oeai.png',
        'member': '',
        'address': ''},
    'MA7': {
        'name': 'Wien Kultur (MA 7)',
        'url': 'https://www.wien.gv.at/kultur/abteilung/',
        'logo': 'wien-kultur.png',
        'member': '',
        'address': ''},
    'AIT': {
        'name': 'Austrian Institute of Technology',
        'url': 'https://www.ait.ac.at/',
        'logo': 'ait.jpg',
        'member': '',
        'address': ''},
    'BCM': {
        'name': 'Belgrade City Museum',
        'url': 'http://www.mgb.org.rs/en/',
        'logo': 'bcm.png',
        'member': '',
        'address': ''},
    'NLS': {
        'name': 'National Library of Serbia',
        'url': 'https://www.nb.rs',
        'logo': 'nls.jpg',
        'member': '',
        'address': ''},
    'Biblioteka Matice Srpske': {
        'name': 'Biblioteka Matice Srpske',
        'url': 'http://www.bms.ns.ac.rs/bms101.htm',
        'logo': 'biblioteka_matice_srpske.png',
        'member': '',
        'address': ''},
    'TIB': {
        'name': 'Tabula Imperii Byzantini',
        'url': 'https://tib.oeaw.ac.at',
        'logo': 'tib.png',
        'member': '',
        'address': ''},
    'UAI': {
        'name': 'Union Académique Internationale',
        'url': 'http://www.uai-iua.org/en',
        'logo': 'uai.jpg',
        'member': '',
        'address': ''}}


@blueprint.app_template_filter()
def display_menu(route: str, category: str) -> str:
    menu = {
        'tib': ['longterm', 'team', 'tib', 'publications', 'youth', 'outreach'],
        'sub': ['longterm'],
        'digtib': ['dig_tib', 'catalouge', 'maps', 'relief', 'model']}
    html = ''
    for item in menu[category]:
        active = 'active' if route.startswith('/' + item) else ''
        html += f'<li class="nav-item {active}">' \
                f'<a class="nav-link" href="{url_for(item)}">' \
                f'{item.title().replace("_", " ")}</a> </li>'
    return Markup(html)


@blueprint.app_template_filter()
def tib_menu(route: str) -> str:
    menu_items = ['history', 'current_status', 'sub_projects',
                  'publications', 'digtib', 'aieb', 'team']
    html = ''
    for item in menu_items:
        active = 'active' if route.startswith('/' + item) else ''
        if item == 'digtib':
            html += f"""
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" 
              href="{url_for(f'tib_{item}')}" 
              id="navbarDropdown" role="button" 
              data-bs-toggle="dropdown" >
            {item.title().replace("_", " ")}
          </a>
          {digtib_submenu(item)}
          </li>
            """
        else:
            html += f"""
            <li class="nav-item">
                <a class="nav-link {active}" href="{url_for(f'tib_{item}')}"
                    >{item.title().replace("_", " ")}</a>
            </li>"""
    return Markup(html)


def digtib_submenu(item: str) -> str:
    html = f'''
    <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
         <li class="nav-item">
                <a class="nav-link " href="{url_for(f'tib_{item}')}">
                Digital Tabula Imperii Byzntini</a>
            </li>
    <li><hr class="dropdown-divider"></li>
    '''
    for item in digtib_bar:
        link = item['link'] if item['link_type'] == 'ext' \
            else url_for(item['link'])
        title = f"{item['title']} <i class='bi bi-box-arrow-up-right'></i>" \
            if item['link_type'] == 'ext' else item['title']
        html += f"""
                <li><a class="dropdown-item" 
                    href="{link}">
                    {title}
                </a></li>
            """

    return f'{html}</ul>'


@blueprint.app_template_filter()
def include_css(route: str) -> str:
    css = ''
    for style in ['style', 'burger', 'navbar', 'parallax', 'footer',
                  'image_hover_effect', 'boxes_background']:
        css += f'<link rel="stylesheet" type="text/css"' \
               f' href="/static/styles/{style}.css">'
    return css


@blueprint.app_template_filter()
def display_institutes(institutes: Iterator) -> str:
    html = ''
    for short_name in institutes:
        institute = INSTITUTES[short_name]
        html += f'''<a href="{institute['url']}" target="_blank">
                <img src="/static/images/institutes/{institute['logo']}" 
                alt="{institute['name']}" title="{institute['name']}"  
                style="display: unset;">
            </a>'''
    return Markup(html)


@blueprint.app_template_filter()
def display_sponsors(institutes: Iterator) -> str:
    html = '<div>'
    for short_name in institutes:
        institute = INSTITUTES[short_name]
        html += f'''
                <div class="row">
                    <div class="col-sm-4">
                        <h6>{institute['name']}</h6>
                        <p>{institute['member']}</p>
                        <p>{institute['address']}</p>
                        <p><a href="{institute['url']}" 
                        target="_blank">{institute['url']}</a></p>
                    </div>
                    <div class="col-sm-4">
                        <a href="{institute['url']}" target="_blank">
                        <img src="/static/images/institutes/{institute['logo']}" 
                        alt="{institute['name']}" 
                        title="{institute['name']}" style="max-height: 200px">
                        </a>
                    </div>
                </div>
                '''
    return Markup(html + '</div>')
