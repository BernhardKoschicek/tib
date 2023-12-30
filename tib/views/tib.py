from flask import Response, redirect, render_template, session, request

from tib import app
from tib.data.images.history import tib_history_images
from tib.data.images.util import IMAGES_SUB, IMAGES_TIB
from tib.data.images.outreach import gallery_outreach, icons_outreach
from tib.data.openatlas.oa_access import view_classes
from tib.data.outreach import outreach
from tib.data.tib.counter import counter
from tib.data.navigation import tib_digtib_submenu_items
from tib.data.tib.jumbotron import front_jumbotron
from tib.data.presentations import presentations
from tib.data.project_publications import project_publications
from tib.data.publications import tib_publications_data
from tib.data.subprojects import subprojects, project_results
from tib.data.team import team_categories
from tib.data.tib_volumes import tib_volumes_dict
from tib.data.toponym_register import register_volume
from tib.util.util import get_dict_entries_by_category, \
    get_prev_and_next_item_of_dict


@app.route('/')
def tib_home() -> str:
    return render_template(
        'tib/frontpage/frontpage.html',
        jumbotron=front_jumbotron,
        counter=counter,
        outreach=get_dict_entries_by_category('tib', outreach),
        outreach_icons=icons_outreach,
        outreach_gallery=gallery_outreach)


@app.route('/history')
def tib_history() -> str:
    return render_template(
        'tib/history/history.html',
        images=tib_history_images)


@app.route('/current_status')
@app.route('/current_status/<volume>')
@app.route('/current-status')
@app.route('/current-status/<volume>')
@app.route('/current-status/<volume>')
def tib_current_status(volume: str = None) -> str:
    if volume:
        return render_template(
            'tib/current_status/volume.html',
            navigation=get_prev_and_next_item_of_dict(
                volume,
                tib_volumes_dict),
            tib_volume=tib_volumes_dict[volume],
            code=volume,
            images=get_dict_entries_by_category(
                tib_volumes_dict[volume]['images'],
                IMAGES_TIB))
    return render_template(
        'tib/current_status/current_status.html',
        tib_volumes=tib_volumes_dict)


@app.route('/sub_projects')
@app.route('/sub_projects/<project>')
@app.route('/subprojects')
@app.route('/subprojects/<project>')
def tib_sub_projects(project: str = None) -> str:
    if project:
        return render_template(
            'tib/subprojects/project.html',
            project=subprojects[project],
            presentations=get_dict_entries_by_category(
                project,
                presentations),
            publications=get_dict_entries_by_category(
                project,
                project_publications),
            results=project_results[project],
            images=get_dict_entries_by_category(project, IMAGES_SUB),
            layout='tib')
    return render_template(
        'tib/subprojects/subprojects.html',
        projects=subprojects)


@app.route('/publications')
def tib_publications() -> str:
    return render_template(
        'tib/publications/publications.html',
        publications=tib_publications_data)


@app.route('/digtib')
def tib_digtib() -> str:
    return render_template(
        'tib/digtib/digtib.html',
        bar=tib_digtib_submenu_items)


@app.route('/tib-register')
@app.route('/tib-register/<volume>')
def tib_register(volume: str = None) -> str:
    if volume:
        return render_template(
            'tib/digtib/register.html',
            register=register_volume[volume]['register'])
    return render_template(
        'tib/digtib/register_overview.html',
        register=register_volume)


@app.route('/aieb')
def tib_aieb() -> str:
    return render_template('tib/aieb/aieb.html')


@app.route('/team')
def tib_team() -> str:
    return render_template(
        'tib/team/team.html',
        categories=team_categories)


@app.route('/imprint')
def tib_imprint() -> str:
    return render_template('tib/imprint.html')


@app.route('/contact')
def tib_contact() -> str:
    return render_template('tib/current_status/current_status.html')


@app.route('/atlas')
def tib_atlas() -> Response:
    return redirect('https://maps-of-power.oeaw.ac.at/frontend')


@app.route('/balkan/explore')
def tib_discover() -> str:
    return render_template(
        'openatlas/explore.html',
        subprojects_dict=subprojects,
        view_classes=view_classes)


@app.route('/language=<language>')
def set_language(language=None):
    session['language'] = language
    return redirect(request.referrer)
