"""Database setup and tear down"""

import click
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

# The database connection. 
# It still has to be initialized, but that must be done when the app starts, 
# for which the app calls init_app() below.
db = SQLAlchemy()


def init_db():
    """Create the database tables."""
    db.create_all()


def close_db(errorhandler):
    """Close the database session
    :parameter errorhandler: this is dummy argument required by  app.teardown_appcontext()

    """
    db.session.remove()


@click.command("init-db")
@with_appcontext
def init_db_command():
    """CLI command to clear the existing data and create new tables."""
    init_db()
    click.echo("Initialized the database")


def init_app(app):
    """Initialize the database using the app's cofiguration.""" 

    print(app.config["SQLALCHEMY_DATABASE_URI"])
    db.init_app(app)
    
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
