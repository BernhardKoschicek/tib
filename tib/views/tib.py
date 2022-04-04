from flask import render_template

from tib import app


@app.route('/')
def tib_home() -> str:
    return render_template('tib/frontpage/frontpage.html')

@app.route('/history')
def tib_history() -> str:
    return render_template('tib/history/history.html')

@app.route('/current_status')
def tib_current_status() -> str:
    return render_template('tib/current_status/current_status.html')

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
