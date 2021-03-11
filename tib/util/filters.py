from typing import Any, Iterator

import flask
import jinja2
from flask import url_for

from tib.views import subprojects

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
        'member': 'Österreichische Akademie der Wissenschaften (ÖAW) <br> Institut für Mittelalterforschung (IMAFO)',
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


@jinja2.contextfilter
@blueprint.app_template_filter()
def display_menu(self: Any, route: str) -> str:
    html = ''
    items = ['longterm', 'subprojects', 'digital_tools', 'team', 'kontakt']
    for item in items:
        active = ''
        if route.startswith('/' + item):
            active = 'active'
        html += '<li class="nav-item {active}">' \
                '<a class="nav-link" href="{url}">{label}</a>' \
                '</li>'.format(active=active, url=url_for(item), label=item.title().replace('_', ' '))
    return html


@jinja2.contextfilter
@blueprint.app_template_filter()
def display_institutes(self: Any, institutes: Iterator) -> str:
    html = ''
    for short_name in institutes:
        institute = INSTITUTES[short_name]
        html += '''
            <a href="{url}" target="_blank">
                <img src="/static/images/institutes/{logo}" alt="{name}" title="{name}"  style="display: unset;">
            </a>'''.format(url=institute['url'], logo=institute['logo'], name=institute['name'])
    return html


@jinja2.contextfilter
@blueprint.app_template_filter()
def display_sponsors(self: Any, institutes: Iterator) -> str:
    html = '<div>'
    for short_name in institutes:
        institute = INSTITUTES[short_name]
        html += '''
                <div class="row">
                    <div class="col-sm-4">
                        <h6>{name}</h6>
                        <p>{member}</p>
                        <p>{address}</p>
                        <p><a href="{url}" target="_blank">{url}</a></p>
                    </div>
                    <div class="col-sm-4">
                        <a href="{url}" target="_blank">
                            <img src="/static/images/institutes/{logo}" alt="{name}" title="{name}" style="max-height: 200px">
                        </a>
                    </div>
                </div>
                '''.format(url=institute['url'], logo=institute['logo'], name=institute['name'],
                           member=institute['member'], address=institute['address'])
    return html + '</div>'
