# Demo Flask application for Engie GEM

This is a simple hello-world app implemented in Flask for a demo.

## Quick Start Guide

Also available in the documentation folder `docs`, [here: Quick Start Guide](docs/quick-start.md)

Here is the TL;DR version, but please *do* read the [Quick Start Guide](docs/quick-start.md) because it explains much better how to launch it and it also explains how to get around in the web application.

1. Change directory to the root of the project (i.e. this git repository)

2. Unfortunately you need to check whether git has converted the End of Line character in a database initialisation script, before you continue to step 3.
    
    This is the script in question: `scripts\postgres\1-init-user-db.sh`.
    See the [Quick Start Guide](docs/quick-start.md) for details.

3. Run docker-compose up

```bash
docker-compose up
```

The CLI command is integrated in flask.

For instructions see: [docs/helloworld-cli.md](docs/helloworld-cli.md)

## Documentation

See [docs/index.md](docs/index.md)

## Troubleshooting

[Troublshooting Guide](docs/troubleshooting.md)

This guide describes one problem in particular.

After cloning / pulling from git, the database initialization script may contain carriage return characters and this causes the script to fail inside the Linux container for PostgreSQL.

I already mentioned this script above:

`scripts\postgres\1-init-user-db.sh`.

The [Quick Start Guide](docs/quick-start.md) explains what error you may encounter, and how to prevent that error. So please don't skip step 2.

If this error happens after all, the [Troublshooting Guide](docs/troubleshooting.md) describes how to solve it.

## Project structure

- docs:
  - The documentation
- helloworld:
  - The source code of the hello world application itself
- tests:
  - This is where I would put unit tests, but in the end I did not have time.
- scripts:
  - Some tools to help with launching the app, and tools for development.
- Docker:
  - Dockerfile: defines the main container, for the Flask app `helloworld`.
  - postgres.dockerfile: for the Postgres container, so it can include database initialization
  - docker-compose.yml: so you can start the all services with `docker-compose up`
- requirements to install the dependencies with pip:
  - requirements.txt:
    - the main dependencies for the Flask app without developer tools
  - dev-requirements.txt:
    - extra tools that are only needed in a development environment: mkdocs, pytest, ...
