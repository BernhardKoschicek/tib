import flask
from flask import url_for
from markupsafe import Markup

from tib.data.balkan.subprojects_ger import subprojects_ger
from tib.data.tib.digtib import digtib_bar

blueprint: flask.Blueprint = flask.Blueprint('filters', __name__)
MENU_NAMES = {
    'balkan_tib': 'TIB Balkan',
    'balkan_long_term': 'Langzeitprojekt',
    'balkan_historical_geographie': 'Historische Geographie',
    'balkan_outreach': 'Öffentlichkeitsarbeit',
    'balkan_team': 'Team',
    'balkan_volumes': 'Bänder der TIB Balkan',
    'balkan_subprojects': 'Projekte',
    'balkan_digital': 'Digitale Ära',
    '3dobjects': '3D Objekte',
    'discover': 'Datenbank durchstöbern',
    'holdura': 'HOLDURA',
    'digtib': 'DigTIB',
    'borderzones': 'Borderzones',
    'montenegro': 'Montenegro',
}


@blueprint.app_template_filter()
def display_menu(route: str) -> str:
    menu = {
        'balkan_tib': [
            'balkan_long_term',
            'balkan_historical_geographie',
            'balkan_outreach',
            'balkan_team',
            'balkan_volumes'],
        'balkan_subprojects': [i for i in subprojects_ger],
        'balkan_digital': ['3dobjects', 'discover']}
    html = ''
    for key, sub in menu.items():
        html += '<div class="col-lg-3 col-md-6 mb-4 mb-md-0">'
        html += f'<a href="{url_for(key)}" ' \
                f'class="nav-link text-center display-6">' \
                f'{MENU_NAMES[key]}</a><hr>' \
                f'<ul class="">'
        for item in sub:
            if key == 'balkan_subprojects':
                url = url_for(key, project=item)
            elif key == 'balkan_digital':
                url = url_for(key, category=item)
            else:
                url = url_for(item)
            html += f'<li class="nav-item">' \
                    f'<a class="nav-link" href="{url}">' \
                    f'{MENU_NAMES[item]}</a></li>'
        html += '</ul></div>'
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
              data-bs-toggle="dropdown" > DigTIB
          </a>
          {digtib_submenu(item)}
          </li>
            """
        elif item == 'aieb':
            html += f"""
            <li class="nav-item">
                <a class="nav-link {active}" href="{url_for(f'tib_{item}')}"
                    >{item.upper().replace("_", " ")}</a>
            </li>"""
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
        title = f"{item['title']} <i class='bi bi-box-arrow-up-right'></i>" \
            if item['link_type'] == 'ext' else item['title']
        html += f"""
                <li><a class="dropdown-item" 
                    href="{item['link']}">
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
