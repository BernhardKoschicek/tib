from flask import render_template

from tib import app
from tib.models.index import front_menu
from tib.models.subprojects import get_subprojects
from tib.models.team import get_team


@app.route('/')
def home() -> str:
    return render_template('home.html', front_menu=front_menu)


@app.route('/team')
def team() -> str:
    return render_template('team/team.html', team=dict(get_team()))


@app.route('/subprojects')
@app.route('/subprojects/<projekt>')
def subprojects(projekt=None):
    if projekt:
        return render_template('projekt_details.html')
    else:
        return render_template(
            'subprojects.html',
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
