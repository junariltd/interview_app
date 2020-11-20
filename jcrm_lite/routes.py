
from flask import render_template
from .auth import login_required
from .api import bp as api_bp
from .auth import bp as auth_bp


def register_routes(app):

    @app.route('/')
    @app.route('/<path:path>')
    @login_required
    def index(path='/'):
        return render_template('app.html')

    app.register_blueprint(auth_bp)
    app.register_blueprint(api_bp)
