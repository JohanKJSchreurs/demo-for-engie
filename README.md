# Demo Flask application for Engie GEM

This is a simple hello-world app implemented in Flask for a demo.

## Quick Start

Get the web application up and running with docker-compose:

```bash
docker-compose up
```

Then open the following URL in your web browser: [http://localhost:5000](http://localhost:5000)

At startup there are two demo users in the database to make it easier to start testing.

The navigation menu at the top has no style to make it look nice but it contains 

- a link to the [Admin application](http://localhost:5000/Admin)
- a link to the home page
- a link to a page that shows the first 10 users and the link to the page for their "greeting".

The person objects have the following fields:

- a numerical ID which is a database sequence,
- a firstname which is a mandatory column/field,
- an optional lastname field.

## Command line tool to display "hello <name>" message

```bash
flask helloworldcli
```

There is a command line tool to display the greeting message for a specified 
person ID. This tools is integrate as a Flask CLI command

If the web application is up and running with Docker then the simplest way
to run the flask command is like so

To list all flask CLI commands:

```bash
docker exec -ti demo-for-engie_web_1 flask
```

## Commands to initialize a database (not needed for PostgreSQL)

There are two other commands to help set up a database, but the PostgreSQL 
database is initialized with some scripts in its Docker container
You only need those commands if you would choose another database, 
for example if you use sqlite for some local testing. 

## Containers: Flask, Postgres and Adminer

- The Flask app is reachable on localhost on port 5000
- The PostgreSQL is reachable on localhost on port 5432
- We have Adminer as a web GUI for postgres, on port 8080

## Documentation: Markdown and MkDocs

Markdown documentation is converted to HTML with [MkDocs](https://www.mkdocs.org/).


## Documentation

See [docs/index.md](docs/index.md)
