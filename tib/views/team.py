import requests
from flask import render_template

from tib import app
from tib.models.entity import Entity


@app.route('/team')
def team() -> str:
    data = requests.get('http://meta.sarfstation.de/api/0.2/system_class/person').json()['result']
    team = []
    for i in data:
        team.append(Entity.get_entity(i['features'][0]))
    for t in team:
        print(t)
    return render_template('team.html', )
