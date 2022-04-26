from flask import render_template

from tib import app
from tib.data.tib.counter import counter
from tib.data.tib.digtib import digtib_bar
from tib.data.tib.jumbotron import front_jumbotron
from tib.data.tib.publications import tib_publications_data
from tib.data.tib.team import team_categories
from tib.data.tib.tib_volumen import tib_volumes_dict
from tib.util.util import  get_prev_and_next_item_of_dict


@app.route('/')
def tib_home() -> str:
    return render_template(
        'tib/frontpage/frontpage.html',
        jumbotron=front_jumbotron,
        counter=counter)


@app.route('/history')
def tib_history() -> str:
    return render_template('tib/history/history.html')


@app.route('/current_status')
@app.route('/current_status/<volume>')
def tib_current_status(volume: str = None) -> str:
    if volume:
        return render_template(
            'tib/current_status/volume.html',
            navigation=get_prev_and_next_item_of_dict(volume, tib_volumes_dict),
            tib_volume=tib_volumes_dict[volume],
            code=volume)
    return render_template(
        'tib/current_status/current_status.html',
        tib_volumen=tib_volumes_dict)


@app.route('/sub_projects')
def tib_sub_projects() -> str:
    return render_template('tib/current_status/current_status.html')


@app.route('/publications')
def tib_publications() -> str:
    return render_template(
        'tib/publications/publications.html',
        publications=tib_publications_data)


@app.route('/digtib')
def tib_digtib() -> str:
    return render_template('tib/digtib/digtib.html', bar=digtib_bar)


@app.route('/tib-register')
def tib_register() -> str:
    return render_template('tib/aieb/aieb.html')


@app.route('/aieb')
def tib_aieb() -> str:
    return render_template('tib/aieb/aieb.html')


@app.route('/team')
def tib_team() -> str:
    return render_template(
        'tib/team/team.html',
        categories=team_categories)


@app.route('/contact')
def tib_contact() -> str:
    return render_template('tib/current_status/current_status.html')
