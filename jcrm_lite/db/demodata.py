import time
from werkzeug.security import generate_password_hash
from .models import User, Contact


def create_demo_data(db):

    # Create user1 / letmein user
    user1 = User(
        username='user1',
        password=generate_password_hash('letmein')
    )
    db.session.add(user1)
    db.session.commit()

    uid = user1.id

    # Create demo contacts
    contacts = [
        Contact(company_name='ABC Customer Ltd', first_name='Mark',
                last_name='Otto', created_user_id=uid, updated_user_id=uid),
        Contact(company_name='Dom\'s Doughnuts', first_name='Jacob',
                last_name='Thornton', created_user_id=uid, updated_user_id=uid),
        Contact(company_name='Ed\'s Kebabs', first_name='Larry',
                last_name='the Bird', created_user_id=uid, updated_user_id=uid)
    ]

    for contact in contacts:
        db.session.add(contact)
    db.session.commit()
