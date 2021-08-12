from flask import render_template

from tib import app
from tib.models.index import front_menu
from tib.models.subprojects import get_subprojects
from tib.models.sponsors import get_sponsors
from tib.models.team import get_team_categorized, get_team_members


@app.route('/')
def home() -> str:
    return render_template('home.html', front_menu=front_menu)


@app.route('/team')
def team() -> str:
    return render_template('team/team.html', team=dict(get_team_categorized()))


@app.route('/subprojects')
@app.route('/subprojects/<project>')
def subprojects(project=None):
    if project:
        p = next((item for item in get_subprojects(app.config['PROJECTS_ID']) if
              item['project'][0] == project), None)
        team = [member for member in get_team_members() if p['project'][0] in member['projects']]
        sponsors = get_sponsors(app.config['FINANCIER_ID'])



        print(p)
        print(team)
        print(sponsors)



        return render_template(
            'projects/project_details.html',
            projects=p)
    else:
        return render_template(
            'projects/subprojects.html',
            projects=get_subprojects(app.config['PROJECTS_ID']))


@app.route('/longterm')
def longterm():
    return render_template('longterm.html')


@app.route('/tib')
def tib():
    return render_template('longterm.html')


@app.route('/publications')
def publications():
    return render_template('longterm.html')


@app.route('/youth')
def youth():
    return render_template('longterm.html')


@app.route('/digtib')
def catalouge():
    return render_template('longterm.html')


@app.route('/dig-tib')
def dig_tib():
    return render_template('longterm.html')


@app.route('/maps')
def maps():
    return render_template('longterm.html')


@app.route('/relief')
def relief():
    return render_template('longterm.html')


@app.route('/model')
def model():
    return render_template('longterm.html')


@app.errorhandler(404)
def page_not_found(e: Exception) -> tuple:
    return render_template('404.html', e=e), 404
