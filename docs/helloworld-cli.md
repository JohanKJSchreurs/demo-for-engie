# Command Line Interface for Hello World

## The really short version

1. Make sure that you are in a project environment or in the web (Flask) container 
2. and then run this command

```bash
flask helloworldcli
```

The difficulty is how to get the Flask environment with all the necessary Python packages.

The command line tool to display the greeting message for a specified 
person ID is subcommand of flask, but in order to get that subcommand you
need to be in the environment for the helloworld app.

You can either:

- a) use the running Docker container for Flask.
  - This is the simplest option.
  - In this container the flask command and everything it needs is already set up.

OR

- b) create a Python virtualenv and install the dependencies with pip, like you would do for development.

## Running flask helloworldcli in the docker container

If the docker container is already up and running ( `docker-compose up` ) then this way 
the simplest way to run `flask helloworldcli`

You need to use the `docker exec` command. Note that in the example below the
name of the container is `demo-for-engie_web_1 ` but your name might be different:

```bash
docker exec -ti demo-for-engie_web_1 flask
```

**For example, using ID = 1 :**

```bash
docker exec -ti demo-for-engie_web_1 flask helloworldcli 1
Hello, Demo user Bob Smith
```

> **Note:**
>
> To see what the names of your running containers are, check with `docker ps` and look for the one where the COMMAND is "flask run".

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
[docs/local-installation.md](docs/local-installation.md)

## Commands to initialize a database (not needed for PostgreSQL)

There are two other commands to help set up a database.

For the PostgreSQL database you don't need them, because the postgres container
includes setup scripts for the helloworld database and these scripts run automatically on the
first run.

Nonetheless these setup commands came in handy to get things started with
SQLite, and they should also work with any database the SQLAlchemy supports.

So if you want to test locally with sqlite for example, these two commands will
let you create the person table, and insert two demo persons into it, respectively.

- `flask init-db`: Creates the person table
- `flask add-demo-persons`  Add two users to start the demo: Bob and Alice.

### All commands available in the flask CLI

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
