# from flask_sqlalchemy import SQLAlchemy
from helloworld.database import db

from typing import Union


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    
    # Maybe we don't really need the last name for the demo. 
    # So I'm keeping it nullable.
    lastname = db.Column(db.String(80), nullable=True)
    
    def __repr__(self):
        return f"Person(id={self.id}, firstname='{self.firstname}', lastname={self.lastname})"

# TODO: do we realy need a special exception or will a 404 do, or just check for returning None? Keep it simple
class PersonDoesNotExist(Exception):
    pass


def get_full_name_for_id(person_id: int) -> Union[str, None]:
        """Get the full name of the Person if it exists.

        :parameter person_id: the person ID to find in the database

        :returns Person, or None if the ID does not exist.

        """
        person = get_person_by_id(person_id)
        if not person:
            # TODO: Is it better to raise the "PersonDoesNotExist" exception?
            return None

        return f"{person.firstname} {person.lastname}"


def get_person_by_id(person_id: int) -> Union[Person, None]:
    """Get a person with the specified ID from the database.

    If the ID does not exists it returns None.

    :parameter person_id: the person ID to find in the database

    :returns Person, or None if the ID does not exist.
    
    """
    
    # TODO: decide: use get_or_404() instead or is it better to handle None when person does not exist?
    return Person.query.get(person_id)


def person_id_exists(person_id: int) -> bool:
    """Returns True of the ID exists in the database, False otherwise."""

    return get_person_by_id(person_id) is not None



