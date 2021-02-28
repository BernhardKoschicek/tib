from flask import render_template

from tib import app


@app.route('/download')
def download():
    return render_template('download.html')
