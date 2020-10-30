import click
from . import db
from .demodata import create_demo_data

from flask import current_app
from flask.cli import with_appcontext


@click.command('initdb')
@with_appcontext
def initdb():
    db.drop_all()
    db.create_all()
    create_demo_data(db)
    click.echo('Initialized the database.')


def register_command(app):
    app.cli.add_command(initdb)
