from typing import Iterator

import flask
from flask import url_for
from markupsafe import Markup

from tib.data.tib.digtib import digtib_bar

blueprint: flask.Blueprint = flask.Blueprint('filters', __name__)



@blueprint.app_template_filter()
def display_menu(route: str, category: str) -> str:
    menu = {
        'tib': ['balkan_long_term', 'team', 'tib', 'publications', 'youth', 'outreach'],
        'sub': ['balkan_long_term'],
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


# @blueprint.app_template_filter()
# def display_institutes(institutes: Iterator) -> str:
#     html = ''
#     for short_name in institutes:
#         institute = INSTITUTES[short_name]
#         html += f'''<a href="{institute['url']}" target="_blank">
#                 <img src="/static/images/institutes/{institute['logo']}"
#                 alt="{institute['name']}" title="{institute['name']}"
#                 style="display: unset;">
#             </a>'''
#     return Markup(html)


# @blueprint.app_template_filter()
# def display_sponsors(institutes: Iterator) -> str:
#     html = '<div>'
#     for short_name in institutes:
#         institute = INSTITUTES[short_name]
#         html += f'''
#                 <div class="row">
#                     <div class="col-sm-4">
#                         <h6>{institute['name']}</h6>
#                         <p>{institute['member']}</p>
#                         <p>{institute['address']}</p>
#                         <p><a href="{institute['url']}"
#                         target="_blank">{institute['url']}</a></p>
#                     </div>
#                     <div class="col-sm-4">
#                         <a href="{institute['url']}" target="_blank">
#                         <img src="/static/images/institutes/{institute['logo']}"
#                         alt="{institute['name']}"
#                         title="{institute['name']}" style="max-height: 200px">
#                         </a>
#                     </div>
#                 </div>
#                 '''
#     return Markup(html + '</div>')
