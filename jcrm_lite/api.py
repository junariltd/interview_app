
from .db import get_db, dictfetchall
from .auth import login_required
from flask import jsonify, request

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

    @app.route(API_PREFIX + '/contact/<int:contact_id>', methods=['GET'])
    @login_required
    def get_contact(contact_id):
        db = get_db()
        contacts = dictfetchall(
            db, "SELECT * FROM contacts WHERE id = ?",
            (contact_id,)
        )
        return jsonify(contacts[0])

    @app.route(API_PREFIX + '/contact/<int:contact_id>', methods=['PUT'])
    @login_required
    def update_contact(contact_id):

        update = request.get_json()
        company_name = update['company_name'].strip()
        first_name = update['first_name'].strip()
        last_name = update['last_name'].strip()
        if not company_name or not first_name or not last_name:
            return jsonify({'success': False, 'message': 'Required field(s) not set'})

        db = get_db()
        db.execute("""
            UPDATE contacts
            SET company_name = ?, first_name = ?, last_name = ?
            WHERE id = ?
        """, (company_name, first_name, last_name, contact_id))
        db.commit()
        return jsonify({'success': True})
