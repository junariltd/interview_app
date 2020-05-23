
from .db import get_db, dictfetchall
from .auth import login_required
from flask import jsonify

API_PREFIX = '/api/v1'


def register_api(app):

    @app.route(API_PREFIX + '/contacts', methods=['GET'])
    @login_required
    def get_contacts():
        db = get_db()
        contacts = dictfetchall(
            db, "SELECT * FROM contacts ORDER BY company_name"
        )
        return jsonify(contacts)
