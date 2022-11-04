from typing import Any

from flask import render_template

from tib import app
from tib.data.outreach import outreach
from tib.data.balkan.project_results import result_links, project_results
from tib.data.balkan.subprojects_ger import subprojects_ger
from tib.data.digital import objects3d
from tib.data.image_descriptions import home_images
from tib.data.images.hist_geo import balkan_hist_geo
from tib.data.images.long_term import tib_balkan_long_term
from tib.data.images.util import IMAGES_SUB, IMAGES_TIB
from tib.data.images.outreach import gallery_outreach, icons_outreach
from tib.data.navigation import balkan_jumbotron
from tib.data.openatlas.oa_access import view_classes
from tib.data.openatlas.subprojects import subprojects_ger_discover
from tib.data.balkan.team import team_members
from tib.data.tib.presentations import presentations
from tib.data.tib.project_publications import project_publications
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
        subprojects=subprojects_ger,
        team=team_members,
        outreach=outreach,
        images=gallery_outreach,
        outreach_icons=icons_outreach)


@app.route('/balkan/team')
def balkan_team() -> str:
    return render_template(
        'balkan/team/team.html',
        team=team_members)


@app.route('/balkan/bände')
@app.route('/balkan/bände/<band>')
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
def balkan_subprojects(project: str = None) -> str:
    if project:
        return render_template(
            'balkan/subprojects/project.html',
            project=subprojects_ger[project],
            presentations=get_dict_entries_by_category(
                project,
                presentations),
            publications=get_dict_entries_by_category(
                project,
                project_publications),
            images=get_dict_entries_by_category(project, IMAGES_SUB),
            results=project_results[project],
            result_links=result_links[project])
    return render_template(
        'balkan/subprojects/subproject_overview.html',
        subprojects=subprojects_ger)


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
            subprojects_dict=subprojects_ger_discover,
            view_classes=view_classes)
    return render_template(
        'balkan/digital/digital.html',
        objects3d=objects3d,
        subprojects_dict=subprojects_ger_discover,
        view_classes=view_classes)


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


@app.route('/balkan/historische-geographie')
def balkan_historical_geographie():
    return render_template(
        'balkan/geography/historically_geography.html',
        images=balkan_hist_geo)


@app.errorhandler(404)
def page_not_found(e: Exception) -> Any:
    return render_template('404.html', e=e), 404
