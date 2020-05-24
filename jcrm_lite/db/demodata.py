import time
from werkzeug.security import generate_password_hash


def create_demo_data(db):
    # Create user1 / letmein user
    cr = db.cursor()
    cr.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        ('user1', generate_password_hash('letmein')),
    )
    user_id = cr.lastrowid
    # Create demo contacts
    contacts = [
        ('ABC Customer Ltd', 'Mark', 'Otto'),
        ('Dom\'s Doughnuts', 'Jacob', 'Thornton'),
        ('Ed\'s Kebabs', 'Larry', 'the Bird')
    ]
    insert_stmt = """INSERT INTO contacts (company_name, first_name, last_name,
        created_date, created_user_id, updated_date, updated_user_id)
        VALUES (?,?,?,?,?,?,?)"""
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    meta = (now, user_id, now, user_id)
    for contact in contacts:
        cr.execute(insert_stmt, contact + meta)
    cr.close()
    db.commit()
