
from ..db import db
from ..db.models import Contact
from ..db.model_utils import jsonify_one, jsonify_list
from ..auth import login_required
from flask import Blueprint, jsonify, request, session
from datetime import datetime

bp = Blueprint('api', __name__, url_prefix='/api/v1')


@bp.route('/contacts', methods=['GET'])
@login_required
def get_contacts():
    contacts = Contact.query.all()
    return jsonify_list(contacts)


@bp.route('/contact/<int:contact_id>', methods=['GET'])
@login_required
def get_contact(contact_id):
    contact = Contact.query.filter_by(id=contact_id).one()
    return jsonify_one(contact)


@bp.route('/contact/<int:contact_id>', methods=['PUT'])
@login_required
def update_contact(contact_id):

    data = request.get_json()

    contact = Contact.query.filter_by(id=contact_id).one()

    contact.company_name = data['company_name']
    contact.first_name = data['first_name']
    contact.last_name = data['last_name']

    contact.updated_date = datetime.utcnow()
    contact.updated_user_id = session.get('user_id')

    db.session.commit()

    return jsonify({'success': True})
