from flask import render_template

from tib import app
from tib.data.index import front_menu
from tib.models.sponsors import Sponsors
from tib.models.subprojects import Subprojects
from tib.models.team import Team
from tib.data.image_descriptions import home_images


@app.route('/')
def home() -> str:
    return render_template(
        'home/home.html',
        front_menu=front_menu,
        img_description=home_images)


@app.route('/team')
def team() -> str:
    return render_template('team/team.html',
                           team=dict(Team.get_team_categorized()))


@app.route('/subprojects')
@app.route('/subprojects/<project>')
def subprojects(project=None):
    if project:
        project = next((item for item in
                  Subprojects.get_subprojects(app.config['PROJECTS_ID']) if
                  item.project[0] == project), None)
        sidebar = render_template(
            'projects/sidebar.html',
            projects=project,
            team=project.project_team,
            sponsors=Sponsors.get_sponsors(app.config['FINANCIER_ID']))
        return render_template(
            'projects/project_details.html',
            projects=project,
            sidebar=sidebar)
    else:
        return render_template(
            'projects/subprojects.html',
            projects=Subprojects.get_subprojects(app.config['PROJECTS_ID']))


@app.route('/longterm')
def longterm():
    return render_template('longterm/longterm.html')


@app.route('/tib')
def tib():
    return render_template('longterm/longterm.html')


@app.route('/publications')
def publications():
    return render_template('longterm/longterm.html')


@app.route('/youth')
def youth():
    return render_template('longterm/longterm.html')


@app.route('/digtib')
def catalouge():
    return render_template('longterm/longterm.html')


@app.route('/dig-tib')
def dig_tib():
    return render_template('longterm/longterm.html')


@app.route('/maps')
def maps():
    return render_template('longterm/longterm.html')


@app.route('/relief')
def relief():
    return render_template('longterm/longterm.html')


@app.route('/model')
def model():
    return render_template('longterm/longterm.html')


@app.errorhandler(404)
def page_not_found(e: Exception) -> tuple:
    return render_template('404.html', e=e), 404
