from flask import render_template

from tib import app


@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')
