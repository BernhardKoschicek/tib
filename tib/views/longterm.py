from flask import render_template

from tib import app


@app.route('/longterm')
def longterm():
    return render_template('longterm.html')
