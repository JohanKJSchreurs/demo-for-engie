from flask import Flask, flash, render_template, redirect, abort, request, session, url_for, g

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from helloworld import create_app
from helloworld import database
from helloworld.models import Person, get_full_name_for_id, get_person_by_id, person_id_exists


app = create_app()


#
# Set up the Admin interface for managing Person objects.
#

class PersonModelView(ModelView):
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
    return render_template("hello.html", name="world")


@app.route("/hello-world/<int:id>")
def hello(id):

    if person_id_exists(id):
        name = get_full_name_for_id(id)
        return render_template("hello.html", name=name)
        
    else:
        # Is a person_not_found page better, or should we redirect to something more useful?
        # return render_template("person_not_found.html", person_id=id)

        flash(f"Could not find a person with this ID: {id}")
        return redirect(url_for("listpersons"))


@app.route("/listpersons")
def listpersons():
    """Shows a short list of persons with a link to click to their greeting page.
    
    This makes it easy to get started, and check the hello-world view above
    """

    persons = Person.query.limit(10).all()
    return render_template('listpersons.html', persons=persons)
