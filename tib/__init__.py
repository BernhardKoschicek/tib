from flask import Flask, request


app = Flask(__name__, instance_relative_config=True)
# app.config.from_object('config.default')  # type: ignore
# app.config.from_pyfile('production.py')  # type: ignore

from tib.util import filters, util
from tib.views import outreach, download, digital_tools, longterm, kontakt, subprojects, team, \
    verein, index
from tib.models import entity

@app.before_request
def before_request():
    if request.path.startswith('/static'):
        return  # Only needed if not running with apache and static alias


@app.after_request
def apply_caching(response):
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response


app.register_blueprint(filters.blueprint)

if __name__ == "__main__":  # pragma: no cover
    app.run()
