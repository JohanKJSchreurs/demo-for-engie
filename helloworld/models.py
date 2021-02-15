"""Model classes for the app. 

These are objects that are stored in a database.
We only have one model really, but putting it in a separate module keeps things neat.
"""

from typing import Union

from helloworld.database import db


class Person(db.Model):
    """A person with a first and last name."""
    
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    
    # Maybe we don't really need the last name for the demo. 
    # So I'm keeping it nullable.
    lastname = db.Column(db.String(80), nullable=True)
    
    def __repr__(self):
        return f"Person(id={self.id}, firstname='{self.firstname}', lastname={self.lastname})"


def get_person_by_id(person_id: int) -> Union[Person, None]:
    """Get a person with the specified ID from the database.

    When the ID does not exists it returns None.

    :parameter person_id: 
        The person ID to find in the database.

    :returns: 
        Person, or None if the ID does not exist.
    
    """
    
    # TODO: decide: should we use get_or_404() instead of get() or is it better to handle None when person does not exist?
    return Person.query.get(person_id)


def person_id_exists(person_id: int) -> bool:
    """Returns True when the ID exists in the database, False otherwise."""

    return get_person_by_id(person_id) is not None

