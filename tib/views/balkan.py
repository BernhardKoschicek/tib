from typing import Any

from flask import render_template

from tib import app
from tib.data.outreach import outreach
from tib.data.digital import objects3d
from tib.data.images.balkan_home import home_images
from tib.data.images.hist_geo import balkan_hist_geo
from tib.data.images.long_term import tib_balkan_long_term
from tib.data.images.util import IMAGES_SUB, IMAGES_TIB
from tib.data.images.outreach import gallery_outreach, icons_outreach
from tib.data.navigation import balkan_jumbotron
from tib.data.openatlas.oa_access import view_classes
from tib.data.presentations import presentations
from tib.data.project_publications import project_publications
from tib.data.subprojects import subprojects, project_results
from tib.data.team import tib_team_data
from tib.data.tib_volumes import tib_volumes_dict
from tib.util.util import get_dict_entries_by_category, \
    get_prev_and_next_item_of_dict


@app.route('/balkan')
@app.route('/balkan/')
def home() -> str:
    return render_template(
        'balkan/home/home.html',
        front_menu=balkan_jumbotron,
        img_description=home_images,
        tib_volumes=tib_volumes_dict,
        subprojects=subprojects,
        team=tib_team_data,
        outreach=outreach,
        images=gallery_outreach,
        outreach_icons=icons_outreach)


@app.route('/balkan/team')
def balkan_team() -> str:
    return render_template(
        'balkan/team/team.html',
        team=tib_team_data)


@app.route('/balkan/bände')
@app.route('/balkan/bände/<band>')
@app.route('/balkan/volumes')
@app.route('/balkan/volumes/<band>')
def balkan_volumes(band: str = None) -> str:
    if band:
        return render_template(
            'balkan/tib_volumes/volume.html',
            tib_volume=tib_volumes_dict[band],
            navigation=get_prev_and_next_item_of_dict(
                band,
                tib_volumes_dict),
            code=band,
            images=get_dict_entries_by_category(
                tib_volumes_dict[band]['images'],
                IMAGES_TIB))
    return render_template(
        'balkan/tib_volumes/tib_volumes.html',
        tib_volumes=tib_volumes_dict)


@app.route('/balkan/subprojekte')
@app.route('/balkan/subprojekte/<project>')
@app.route('/balkan/subprojects')
@app.route('/balkan/subprojects/<project>')
def balkan_subprojects(project: str = None) -> str:
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
            images=get_dict_entries_by_category(project, IMAGES_SUB),
            results=project_results[project],
            layout='balkan')
    return render_template(
        'balkan/subprojects/subproject_overview.html',
        subprojects=subprojects)


@app.route('/balkan/public-relations')
@app.route('/balkan/öffentlichskeitsarbeit')
def balkan_outreach() -> str:
    return render_template(
        'balkan/outreach/outreach.html',
        outreach=outreach,
        outreach_gallery=gallery_outreach,
        outreach_icons=icons_outreach)


@app.route('/balkan/digital')
@app.route('/balkan/digital/<category>')
def balkan_digital(category: str = None) -> str:
    if category:
        return render_template(
            f'balkan/digital/{category}.html',
            objects3d=objects3d,
            subprojects_dict=subprojects,
            view_classes=view_classes)
    return render_template(
        'balkan/digital/digital.html',
        objects3d=objects3d,
        subprojects_dict=subprojects,
        view_classes=view_classes)


@app.route('/balkan/long-term-project')
@app.route('/balkan/langzeitprojekt')
def balkan_long_term():
    return render_template(
        'balkan/longterm/longterm.html',
        images=tib_balkan_long_term)


@app.route('/balkan/tib')
def balkan_tib():
    return render_template(
        'balkan/tib_balkan/tib_balkan.html',
        tib_volumes=tib_volumes_dict)


@app.route('/balkan/historical-geography')
@app.route('/balkan/historische-geographie')
def balkan_historical_geographie():
    return render_template(
        'balkan/geography/historical_geography.html',
        images=balkan_hist_geo)


@app.errorhandler(404)
def page_not_found(e: Exception) -> Any:
    return render_template('404.html', e=e), 404
