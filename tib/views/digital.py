from flask import render_template

from tib import app


@app.route('/digital')
def digital():
    return render_template('digital.html')
