from pathlib import Path

from flask_babel import Babel
from flask import Flask, Response, g, request, session
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__, instance_relative_config=True)
csrf = CSRFProtect(app)
babel = Babel(app)
app.config.from_object('config')  # type: ignore
if (Path(app.root_path).parent / 'instance' / 'production.py').is_file():
    app.config.from_pyfile('production.py')

# pylint: disable=wrong-import-position, import-outside-toplevel
from tib.util import filters, util
from tib import views_balkan
from tib.model import team


@babel.localeselector
def get_locale() -> str:
    if 'language' in session:
        return session['language']
    best_match = request.accept_languages.best_match(app.config['LANGUAGES'])
    return best_match if best_match else g.settings['default_language']


@app.before_request
def before_request():
    if request.path.startswith('/static'):
        return  # Only needed if not running with apache and static alias


@app.after_request
def apply_caching(response: Response) -> Response:
    response.headers['Strict-Transport-Security'] = \
        'max-age=31536000; includeSubDomains'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response


app.register_blueprint(filters.blueprint)

if __name__ == "__main__":  # pragma: no cover
    app.run()
