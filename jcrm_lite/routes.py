
from flask import render_template
from .db import get_db
from .auth import login_required
from .api import register_api


def register_routes(app):

    @app.route('/')
    @login_required
    def index():
        db = get_db()
        return render_template('app.html')

    register_api(app)
