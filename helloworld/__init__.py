"""The application factory is in here."""
import os

from flask import Flask, render_template, redirect, abort, request, session, url_for, g


def create_app():
    """Flask application factory: creates and configures the app."""

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

    app.config.from_mapping(
        # This is a default. SECRET_KEY should be configured in config.py
        # with a proper randomly generated value.
        SECRET_KEY="someRandomStuff_for_development!1sdf2s1d4szrf",
    )

    instance_config_path = os.path.join(app.instance_path, "config.py")
    if os.path.exists(instance_config_path):
        app.config.from_pyfile(instance_config_path)
    else:
        # Ensure the instance folder exists
        os.makedirs(instance_config_path)
    
    # Set up the database session using the app's configuration.
    from . import database
    database.init_app(app)

    return app
