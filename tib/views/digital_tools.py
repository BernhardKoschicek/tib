from flask import render_template

from tib import app


@app.route('/digital_tools')
def digital_tools():
    return render_template('digital_tools.html')
