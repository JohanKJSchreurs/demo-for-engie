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


