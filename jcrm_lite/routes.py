
from flask import render_template
from .auth import login_required
from .api import register_api


def register_routes(app):

    @app.route('/')
    @app.route('/<path:path>')
    @login_required
    def index(path='/'):
        return render_template('app.html')

    register_api(app)
