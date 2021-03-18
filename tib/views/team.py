from collections import defaultdict

import requests
from flask import render_template

from tib import app
from tib.models.team import Team
from tib.models.util import Util


@app.route('/team')
def team() -> str:
    data = requests.get('http://meta.sarfstation.de/api/0.2/system_class/person').json()['result']
    entity = []
    for i in data:
        entity.append(Team.get_entity(i['features'][0]))
    team = defaultdict(list)
    for e in entity:
        team[e['current_employment'][0]].append(e)
    print(dict(team))
    return render_template('team.html', team=dict(team))
