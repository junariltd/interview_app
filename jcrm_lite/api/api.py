
from ..db.models import Contact
from ..auth import login_required
from flask import jsonify, request, session
import time

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

        updated_date = time.strftime("%Y-%m-%d %H:%M:%S")
        updated_user_id = session.get("user_id")

        db = get_db()
        db.execute("""
            UPDATE contacts
            SET company_name = ?, first_name = ?, last_name = ?,
            updated_date = ?, updated_user_id = ?
            WHERE id = ?
        """, (company_name, first_name, last_name,
              updated_date, updated_user_id, contact_id))
        db.commit()

        return jsonify({'success': True})
