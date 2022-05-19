from typing import Any

from flask import render_template

from tib import app
from tib.data.balkan.balkan_volumen import tib_volumen_dict
from tib.data.balkan.outreach import outreach
from tib.data.balkan.project_results import project_results
from tib.data.balkan.subprojects_ger import subprojects_ger
from tib.data.digital import objects3d
from tib.data.image_descriptions import home_images
from tib.data.images.images import IMAGES_SUB_GER, IMAGES_TIB, tib_history
from tib.data.images.outreach import img_outreach
from tib.data.index import front_menu
from tib.data.oa_access import get_entity_from_oa, \
    get_oa_by_view_class, view_classes
from tib.data.subprojects import subprojects_dict
from tib.data.balkan.team import team_members
from tib.data.tib.presentations import presentations
from tib.data.tib.project_publications import project_publications
from tib.data.tib.tib_volumen import tib_volumes_dict
from tib.util.util import get_dict_entries_by_category, \
    get_prev_and_next_item_of_dict


@app.route('/balkan')
@app.route('/balkan/')
def home() -> str:
    return render_template(
        'balkan/home/home.html',
        front_menu=front_menu,
        img_description=home_images,
        tib_volumen=tib_volumen_dict,
        subprojects=subprojects_ger,
        team=team_members,
        outreach=outreach,
        images=img_outreach)


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
            'balkan/tib_volumen/volume.html',
            tib_volume=tib_volumen_dict[band],
            navigation=get_prev_and_next_item_of_dict(
                band,
                tib_volumen_dict),
            code=band,
            images=get_dict_entries_by_category(
                tib_volumes_dict[band]['images'],
                IMAGES_TIB))
    return render_template(
        'balkan/tib_volumen/tib_volumes.html',
        tib_volumen=tib_volumen_dict)


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
            images=get_dict_entries_by_category(project, IMAGES_SUB_GER),
            results=project_results[project])
    return render_template(
        'balkan/subprojects/subproject_overview.html',
        subprojects=subprojects_ger)


@app.route('/balkan/öffentlichskeitsarbeit')
def balkan_outreach() -> str:
    return render_template(
        'balkan/outreach/outreach.html',
        outreach=outreach,
        images=img_outreach)


@app.route('/balkan/entity/<id_>')
def entity_view(id_: int) -> str:
    return render_template(
        'balkan/digital/entity_view.html',
        entity=get_entity_from_oa(id_))


@app.route('/balkan/digital/')
def balkan_digital() -> str:
    return render_template(
        'balkan/digital/digital.html',
        objects3d=objects3d,
        subprojects_dict=subprojects_dict,
        view_classes=view_classes)


@app.route('/digital/<project>/<view>')
def digital_oa_access(project: str, view: str) -> str:
    return render_template(
        'balkan/digital/entity_table.html',
        data=get_oa_by_view_class(view, subprojects_dict[project]['oaID']),
        project=subprojects_dict[project],
        view_classes=view_classes[view])


@app.route('/balkan/langzeitprojekt')
def balkan_long_term():
    return render_template('balkan/longterm/longterm.html', images=tib_history)

@app.route('/balkan/langzeitprojekt')
def balkan_tib():
    return render_template('balkan/longterm/longterm.html', images=tib_history)


@app.route('/balkan/historische-geographie')
def balkan_historical_geographie():
    return render_template(
        'balkan/geography/historically_geography.html')



@app.errorhandler(404)
def page_not_found(e: Exception) -> Any:
    return render_template('404.html', e=e), 404
