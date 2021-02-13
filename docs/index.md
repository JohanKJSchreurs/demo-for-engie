# Demo Flask application for Engie

This is a simple hello-world app implemented in Flask.

For deployment we use Docker with Docker compose.
This gives us a decent basis to deploy the app somewhere in the cloud (AWS, GCP, Heroko ...)

But for the moment I don't have the knowledge to deploy it on those platforms (yet). 
So I will leave that out for now. Perhaps if I have time at the end I will try to deploy the demo after all.


What you find in this manual
- Installation instructions.
- How to launch the application

## Project structure

- docs: the documentation
- src: the application's source code
- tests: unit tests  

The unit tests are kept in separate from the application's code. 
There are other ways you could organize this, but the benefit of having a separate folder for tests is that you don't have to import extra dependencies that are only used during testing or development when you run the application.


