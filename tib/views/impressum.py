from flask import render_template

from tib import app


@app.route('/impressum')
def impressum():
    return render_template('impressum.html')
