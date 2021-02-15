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

## Documentation

See [docs/index.md](docs/index.md)
