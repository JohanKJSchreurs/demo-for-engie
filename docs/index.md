# Demo Flask application for Engie

This is a simple hello-world app implemented in Flask for a demo.

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

So the unit tests and the application are kept in a separate folders. 
There are other ways you could organize this, but this way has the benefit that you can import/use the application without the need to also load the dependencies for unit testing or for any development tools.


## Utilities for launching and configuring the application

You find these tools in the folder `scripts`

> // Comment: To Be Decided: this folder structure is perhaps more cumbersome. Find a better way to organize the scripts folder.

If they are Windows-specific, they will be stored in `scripts\windows`.
If they are Linux-specific, they will be stored in `scripts/linux`.



Generate a random key for the SECRET_KEY in the Flask configuration


python scripts\generate_random_key.py


