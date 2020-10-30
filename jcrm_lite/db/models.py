
from . import db
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin


class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)


class Contact(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)

    created_user_id = db.Column(
        db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_date = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    updated_user_id = db.Column(
        db.Integer, db.ForeignKey('user.id'), nullable=False)
    updated_date = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
