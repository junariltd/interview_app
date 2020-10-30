import sqlite3
import click
from .demodata import create_demo_data

from flask import current_app, g
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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
