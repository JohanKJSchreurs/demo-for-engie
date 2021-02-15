# How to create a local development environment (i.e. without Docker)

These are setup instructions for when you want to work on the application outside of a Docker container, directly on your system.

We advise using Docker because that allows to have (almost) the same environment for your development as what you will have in production.
However, if you need to, this is how to set it up. It may come in handy when you need to do some troubleshooting, or as a fall-back should there be some problem with the docker setup.

## References

See also:  The official Flask docs, [Flask Installation.](https://flask.palletsprojects.com/en/1.1.x/installation/)

URL: [https://flask.palletsprojects.com/en/1.1.x/installation/](https://flask.palletsprojects.com/en/1.1.x/installation/)

## Create a python virtual environment

**Windows:**

    py -3 -m venv venv

**Linux:**

    python3 -m venv venv

### Activate the environment

**Windows:**

    venv\Scripts\activate

**Linux:**

    source venv/bin/activate

## Install Flask and all the applications dependencies

Install all dependencies with pip, via the provided pip requirements file, `requirements.txt`.

This file is located at the root folder of the project, in other words at the root of the git repository that you cloned from GitHub.

1. In your terminal, change directory to the root of the project folder.

2. Then run:

    python -m pip install -r requirements.txt


## setup your config file

We have an example file that you can copy to the instance folder.

This is in fact what the Dockerfile for the flask container does.

In the root of your project / your git repo, copy `the file 

    example-config\example_config.py

to:

    instance\config.py

Here are corresponding commands for the command line:

**Windows:**

    copy example-config\example_config.py instance\config.py

**Linux:**

    cp example-config\example_config.py instance\config.py

## create the database tables

I have added a command the Flask CLI to create the database tables easily.

    flask init-db

Optionally, you can also add two demo users to get you started, with this command:

    flask add-demo-persons

This adds the following persons:

- firstname: 'Demo user Bob', lastname: 'Smith'
- firstname: 'Demo user Alice', lastname: null (deliberately, so we can test with a lastname that is null)


It is safe to run `flask add-demo-users` multiple times (which can happen by accident). 
The users will only be created if it does not exist yet (The check is based on their first name)

As usual, you can see all the available flask commands by running

    flask

Or

    flask --help
