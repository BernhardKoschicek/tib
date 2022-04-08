from flask import render_template

from tib import app
from tib.data.tib.counter import counter
from tib.data.tib.jumbotron import front_jumbotron
from tib.data.tib.tib_volumen import tib_volumes_dict


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
@app.route('/current_status/tib-volumen/<volume>')
def tib_current_status(volume: str = None) -> str:
    if volume:
        return render_template(
            'tib/current_status/volume.html',
            tib_volume=tib_volumes_dict[volume])
    return render_template(
        'tib/current_status/current_status.html',
        tib_volumen=tib_volumes_dict)


@app.route('/sub_projects')
def tib_sub_projects() -> str:
    return render_template('tib/current_status/current_status.html')


@app.route('/publications')
def tib_publications() -> str:
    return render_template('tib/current_status/current_status.html')


@app.route('/digtib')
def tib_digtib() -> str:
    return render_template('tib/current_status/current_status.html')


@app.route('/aieb')
def tib_aieb() -> str:
    return render_template('tib/current_status/current_status.html')


@app.route('/team')
def tib_team() -> str:
    return render_template('tib/current_status/current_status.html')


@app.route('/contact')
def tib_contact() -> str:
    return render_template('tib/current_status/current_status.html')
