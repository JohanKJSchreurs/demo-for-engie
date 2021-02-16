# Demo Flask application for Engie GEM

This is a simple hello-world app implemented in Flask for a demo.

## Quick Start Guide

Also available in the documentation folder `docs`, [here: Quick Start Guide](docs/quick-start.md)

Here is the TL;DR version, but please *do* read the [Quick Start Guide](docs/quick-start.md) because it explains much better how to launch and use the application.

1. Change directory to the root of the project (i.e. this git repository)

2. Run docker-compose up

```bash
docker-compose up
```

The CLI command is integrated in flask.

For instructions see: [docs/helloworld-cli.md](docs/helloworld-cli.md)

## Documentation

See [docs/index.md](docs/index.md)

## Troubleshooting

I have discovered there may be an issue with the database initialization script `scripts\postgres\1-init-user-db.sh`.

When you clone the git repository git may convert Unix's End of Line character `\n`, to the Windows convention of having two characters: `\n\r`.
This trips up the script in the Docker container for the postgres service.

The script runs in a Linux container. But git may convert the linux EOL characters which are a single \n into the Windows convention of having two characters for a newline and carriage return \n\r.

This page describes how to solve it:

[Troublshooting Guide](docs/troubleshooting.md)

## Project structure

- docs: the documentation
- helloworld: the source code of the hello world application itself
- tests: where I would put unit tests, but in the end I did not have time.
- scripts: some tools to help with launching the app, and tools for development.
- Docker:
  - Dockerfile: defines the main container, for the Flask app `helloworld`.
  - postgres.dockerfile: for the Postgres container, so it can include database initialization
  - docker-compose.yml: so you can start the all services with `docker-compose up`
- requirements to install the dependencies with pip:
  - requirements.txt: the main dependencies for the Flask app without developer tools
  - dev-requirements.txt: extra tools that are only needed in a development environment: mkdocs, pytest, ...
