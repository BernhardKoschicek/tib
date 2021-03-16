import requests
from flask import render_template

from tib import app
from tib.models.entity import Entity


@app.route('/team')
def team() -> str:
    data = Entity.get_entity(
        requests.get('http://meta.sarfstation.de/api/0.2/system_class/person').json()['result'])

    return render_template('team.html', )
