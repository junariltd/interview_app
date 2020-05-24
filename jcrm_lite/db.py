import sqlite3
import click
import time

from flask import current_app, g
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def dictfetchall(db, sql, args=()):
    cr = db.cursor()
    cr.execute(sql, args)
    cols = [col[0] for col in cr.description]
    results = []
    for row in cr.fetchall():
        results.append(dict(zip(cols, row)))
    return results


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
    return db


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


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    db = init_db()
    create_demo_data(db)
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
