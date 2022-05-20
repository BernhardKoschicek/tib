from flask import render_template

from tib import app
from tib.data.images.images import IMAGES_TIB
from tib.data.outreach import outreach
from tib.data.tib.counter import counter
from tib.data.tib.digtib import digtib_bar
from tib.data.tib.jumbotron import front_jumbotron
from tib.data.tib.publications import tib_publications_data
from tib.data.tib.subprojects import subprojects
from tib.data.tib.team import team_categories
from tib.data.tib.tib_volumen import tib_volumes_dict
from tib.data.volumes.toponym_register import register_volume
from tib.util.util import get_dict_entries_by_category, \
    get_prev_and_next_item_of_dict


@app.route('/')
def tib_home() -> str:
    return render_template(
        'tib/frontpage/frontpage.html',
        jumbotron=front_jumbotron,
        counter=counter,
        outreach=get_dict_entries_by_category('tib', outreach))


@app.route('/history')
def tib_history() -> str:
    return render_template('tib/history/history.html')


@app.route('/current_status')
@app.route('/current_status/<volume>')
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
        tib_volumen=tib_volumes_dict)


@app.route('/sub_projects')
@app.route('/sub_projects/<project>')
def tib_sub_projects(project: str = None) -> str:
    if project:
        return render_template(
            'tib/subprojects/project.html',
            project=subprojects[project])
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
    return render_template('tib/digtib/digtib.html', bar=digtib_bar)


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
