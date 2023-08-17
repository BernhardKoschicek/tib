import flask
from flask import url_for
from flask_babel import gettext as _

from tib.data.navigation import \
    balkan_nav_items, tib_digtib_submenu_items, balkan_nav_translations, \
    tib_nav_items

blueprint: flask.Blueprint = flask.Blueprint('filters', __name__)


@blueprint.app_template_filter()
def balkan_nav(route: str) -> str:
    html = ''
    for url, text in balkan_nav_items.items():
        html += '<div class="col-lg-3 col-md-6 mb-4 mb-md-0">'
        html += f'<a href="{url_for(url)}" ' \
                f'class="nav-link text-center display-6">' \
                f'{balkan_nav_translations[url]}</a><hr>' \
                f'<ul class="">'
        for suburl in text:
            if url == 'balkan_subprojects':
                url_ = url_for(url, project=suburl)
            elif url == 'balkan_digital':
                url_ = url_for(url, category=suburl)
            else:
                url_ = url_for(suburl)
            html += f'<li class="nav-item">' \
                    f'<a class="nav-link" href="{url_}">' \
                    f'{balkan_nav_translations[suburl]}</a></li>'
        html += '</ul></div>'
    return html


@blueprint.app_template_filter()
def tib_nav(route: str) -> str:
    html = ''
    for url, text in tib_nav_items.items():
        active = 'active' if route.startswith('/' + url) else ''
        if url == 'digtib':
            html += f"""
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" 
              href="{url_for(f'tib_{url}')}" 
              id="navbarDropdown" role="button" 
              data-bs-toggle="dropdown" > DigTIB
          </a>
          {tib_digtib_submenu(url)}
          </li>
            """
        elif url == 'aieb':
            html += f"""
            <li class="nav-item">
                <a class="nav-link {active}" href="{url_for(f'tib_{url}')}"
                    >{text}</a>
            </li>"""
        else:
            html += f"""
            <li class="nav-item">
                <a class="nav-link {active}" href="{url_for(f'tib_{url}')}"
                    >{text}</a>
            </li>"""
    return html


def tib_digtib_submenu(item: str) -> str:
    html = f'''
    <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
         <li class="nav-item">
                <a class="nav-link " href="{url_for(f'tib_{item}')}">
                {_('Digital Tabula Imperii Byzantini')}</a>
            </li>
    <li><hr class="dropdown-divider"></li>
    '''
    for item in tib_digtib_submenu_items:
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
    for style in ['style', 'burger', 'navbar', 'parallax', 'footer', 'fonts',
                  'image_hover_effect', 'boxes_background', 'responsive_grid',
                  'datatables']:
        css += f'<link rel="stylesheet" type="text/css"' \
               f' href="/static/styles/{style}.css">'
    return css
