from flask import render_template

from tib import app


@app.route('/digtib')
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
