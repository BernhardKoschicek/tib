from flask import render_template

from tib import app


@app.route('/verein')
def verein():
    return render_template('verein.html')
