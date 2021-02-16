"""The views and CLI commands for the helloworld app."""

import os

import click
from flask.cli import with_appcontext

from flask import Flask, flash, render_template, redirect, abort, request, session, url_for, g

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from helloworld import create_app
from helloworld import database
from helloworld.models import Person, get_person_by_id, person_id_exists


app = create_app()


#
# Set up the Admin interface for managing Person objects.
#

class PersonModelView(ModelView):
    """Customized ModelView for Person in the Admin app."""

    # Also show the ID, in case we have people with the same name.
    column_list = ("id", "firstname", "lastname")
    can_view_details = True
    
    # To make columns searchable, or to use them for filtering:
    column_searchable_list = ["firstname", "lastname", "id"]


admin = Admin(app, name="helloworld", template_mode="bootstrap3")

# Add administrative views
admin.add_view(PersonModelView(Person, database.db.session))


#
# Views
#

# TODO: Maybe the home page should show some basic instruction how to use the app, if there is anything to explain.
@app.route("/")
def home():
    """The view for the home page"""
    return render_template("home.html")


@app.route("/hello-world/<int:id>")
def hello(id):
    """The view for the Hello <name> greeting

    :parameter id: the ID of the person in the database.

    """

    if person_id_exists(id):
        person = get_person_by_id(id)
        return render_template("hello.html", greeting=get_greeting(person))

    else:
        flash(f"Could not find a person with this ID: {id}")
        return redirect(url_for("listpersons"))


def get_greeting(person: Person):
    return f"Hello, {person.firstname} {person.lastname or ''}"


@app.route("/listpersons")
def listpersons():
    """View that shows a short list of persons, with a link to click to their greeting page.
    
    This makes it easier to start testing the application, by giving you some
    links you can click in order to check the hello view for a few persons.
    """

    persons = Person.query.limit(10).all()
    return render_template('listpersons.html', persons=persons)


@click.command(help="Show the greeting for the specified person ID.")
@click.argument("person_id", type=click.INT)
@with_appcontext
def helloworldcli(person_id):
    """The command on the CLI that shows the 'hello <name>" message for the specified ID.
    """

    if person_id is None:
        print(
            "ERROR: No ID specified. " + 
            "Please try again and specify a numerical ID.\n"
        )
        return 1

    elif person_id < 0:
        return 2

    elif not person_id_exists(person_id):
        print(f"There is no person with this ID: {person_id}")
        return 3
    
    else:
        person = get_person_by_id(person_id)
        print(get_greeting(person))
        
    return 0

# Make it available as a subcommand of `flask`
app.cli.add_command(helloworldcli)


@click.command(
    "add-demo-persons", 
    help="Add two users to start the demo: Bob and Alice."
)
@with_appcontext
def add_demo_persons():
    """Add two demo persons to get started, Bob and Alice.

    If they already exist we will skip creating the persons that already exist.
    """

    session = database.db.session
    bob = Person(firstname="Demo user Bob", lastname="Smith")
    
    existing_bob = Person.query.filter_by(firstname="Demo user Bob").first()
    if existing_bob:
        print(f"{bob.firstname} already exists as: {existing_bob}")
    else:
        print(f"Creating {bob.firstname} in the database")
        session.add(bob)
        session.commit()

    # lastname is not mandatory:
    alice = Person(firstname="Demo user Alice")
    existing_alice = Person.query.filter_by(firstname="Demo user Alice").first()
    if existing_alice:
        print(f"{alice.firstname} already exists as: {existing_alice}")
    else:
        print(f"Creating {alice.firstname} in the database")
        session.add(alice)
        session.commit()


# Make it available as a subcommand of `flask`
app.cli.add_command(add_demo_persons)


@click.command(
    "gen-secret-key", 
    help="generate a random value for the SECRET_KEY configuration variable."
)
@with_appcontext
def generate_secret_key():
    """Generate a new key suitable for the SECRET_KEY configuration variable."""
    print(os.urandom(16))


# Make it available as a subcommand of `flask`
app.cli.add_command(generate_secret_key)
