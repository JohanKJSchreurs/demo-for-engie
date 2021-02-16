# Demo Flask application for Engie GEM

This is a simple hello-world app implemented in Flask for a demo.

## Quick Start

[Quick Start](quick-start.md)

## How to launch the Command Line Application

See:  [Command Line Interface for Hello World](helloworld-cli.md)

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

## Docker deployment

For deployment we use Docker Docker compose.
This gives us a decent basis to deploy the app somewhere in the cloud (AWS, GCP, Heroko ...)

But for the moment I don't have the knowledge to deploy it on those platforms (yet). 
So I will leave that out for now. Perhaps if I have time at the end I will try to deploy the demo after all.

## Documentation: Markdown and MkDocs

Markdown documentation is converted to HTML with [MkDocs](https://www.mkdocs.org/).

## How to install the app in a virtualenv for development

(i.e. without a Docker container)

[How to create a local development environment (i.e. without Docker)](docs\local-installation.md)
