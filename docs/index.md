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

## Command line tool to display "hello &lt; name &gt; message

```bash
flask helloworldcli
```

The command line tool to display the greeting message for a specified 
person ID is subcommand of flask, but in order to get that subcommand you
need to be in the environment for the helloworld app.

If the web application is already up and running as a Docker container then 
the simplest way to run flask helloworldcli is through the container, 
with `docker exec`:

The alternative is to set up a python virtualenv with the flask app and  run `flask helloworldcli` in the activated virtualenv

### How to run it with docker exec

```bash
docker exec -ti demo-for-engie_web_1 flask
```

**For example:**

```shell
docker exec -ti demo-for-engie_web_1 flask helloworldcli 1
Hello, Demo user Bob Smith
```

> Note re: Container name `demo-for-engie_web_1`
>
> Note that the name of the docker container here is `demo-for-engie_web_1` which
is the default name `docker-compost up` has generated.
>
>To see what the names of your running containers are, check with `docker ps` and look for the one where the COMMAND is "flask run".

**For example**

```

docker ps
CONTAINER ID   IMAGE                     COMMAND                  CREATED          STATUS          PORTS                    NAMES
2fc70e90d047   adminer                   "entrypoint.sh docke…"   45 minutes ago   Up 45 minutes   0.0.0.0:8080->8080/tcp   demo-for-engie_adminer_1
bfa7dc9f4341   demo-for-engie_web        "flask run"              45 minutes ago   Up 45 minutes   0.0.0.0:5000->5000/tcp   demo-for-engie_web_1
168501c42769   demo-for-engie_postgres   "docker-entrypoint.s…"   45 minutes ago   Up 45 minutes   0.0.0.0:5432->5432/tcp   demo-for-engie_postgres_1

```

### Running helloworldcli with a local virtualenv

This requires a bit more setup.
This page describes how to set up the virtualenv and how to configure the app
outside without Docker, locally:
[local-installation/](local-installation/)



## Commands to initialize a database (not needed for PostgreSQL)

There are two other commands to help set up a database.

For he PostgreSQL database you don't need them, because postgres container
has setup scripts for the helloworld database that run automatically on the
first run.

However they, came in handy in the beginning to get things going, and you
can use them with any database the SQLAlchemy supports.

So if you want to test locally with sqlite for example, these two commands will
let you create the person table, and insert two demo persons into it, respectively.

- `flask init-db`: Creates the person table
- `flask add-demo-persons`  Add two users to start the demo: Bob and Alice.


### all commands available in the flask CLI

```
Commands:
  add-demo-persons  Add two users to start the demo: Bob and Alice.
  gen-secret-key    generate a random value for the SECRET_KEY
                    configuration...

  helloworldcli     Show the greeting for the specified person ID.
  init-db           CLI command to clear the existing data and create new...
  routes            Show the routes for the app.
  run               Run a development server.
  shell             Run a shell in the app context.
```

## Containers: Flask, Postgres and Adminer

- The Flask app is reachable on localhost on port 5000
- The PostgreSQL is reachable on localhost on port 5432
- We have Adminer as a web GUI for postgres, on port 8080

## Documentation: Markdown and MkDocs

Markdown documentation is converted to HTML with [MkDocs](https://www.mkdocs.org/).


## Docker deployment

For deployment we use Docker Docker compose.
This gives us a decent basis to deploy the app somewhere in the cloud (AWS, GCP, Heroko ...)

But for the moment I don't have the knowledge to deploy it on those platforms (yet). 
So I will leave that out for now. Perhaps if I have time at the end I will try to deploy the demo after all.

What you find in this manual

- Installation instructions
- How to launch the application

## Project structure

- docs: the documentation
- helloworld: the source code of the hello world application itself
- tests: unit tests
- scripts: some tools to help with launching the app, and tools for development.
- two dockerfiles and a docker-compose.yml file
- requirements.txt for installing python dependencies with pip

