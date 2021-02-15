import os
import pathlib

from flask import Flask, render_template, redirect, abort, request, session, url_for, g


def create_app():

    app = Flask(__name__, instance_relative_config=True)
    
    # Set up some defaults for the config.
    # If the instance folder exists we try to load the config from the instance folder.
    #
    # ALTERNATIVE to using config.py: 
    # Perhaps it is better to use environment variables for configuration, 
    # the way the Twelve-Factor App describes it.
    # See also https://12factor.net/config
    #
    # Example:
    #   app.config.from_envvar('YOURAPPLICATION_SETTINGS')
    # Which is equivalent to:
    #   app.config.from_pyfile(os.environ['YOURAPPLICATION_SETTINGS'])
    #
    
    # # default_db_path = pathlib.Path(app.instance_path) / "helloworld.sqlite"
    # default_db_path = os.path.join(app.instance_path, "helloworld.sqlite")
    # print(f"default_db_path={default_db_path}")

    instance_config_path = os.path.join(app.instance_path, "config.py")
    
    app.config.from_mapping(
        # SECRET_KEY should be configured in config.py with a proper randomly generated value.
        SECRET_KEY="someRandomStuff_for_development!1sdf2s1d4szrf",
    )

    # TODO: Do we really need silent=True?
    app.config.from_pyfile(instance_config_path) # , silent=True)

    # Ensure the instance folder exists
    instance_path = pathlib.Path(app.instance_path)
    if not instance_path.exists():
        instance_path.mkdir()
    
    # Set up the database session using the app's configuration.
    from . import database
    database.init_app(app)

    return app