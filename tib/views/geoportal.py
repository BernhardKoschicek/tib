from flask import render_template

from tib import app


@app.route('/geoportal')
def geoportal():
    return render_template('geoportal.html')
