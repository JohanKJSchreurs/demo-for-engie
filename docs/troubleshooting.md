# Troubleshooting Guide

I have discovered there may be an issue with the database initialization script `scripts\postgres\1-init-user-db.sh`.

This issue is probably caused by the fact that git converts its End-of-Line characters and then the script fails in the postgres container, which does not handle the carriage return characters for some reason.

Below is a description of the error you may encounter and how to fix it.

## Error: sqlalchemy.exc.OperationalError: password authentication failed for user "helloworld"

When the helloworld database is not present, then you may encounter the following error when you start the app for the first time.
This would happen when you open the page `http://localhost:5000/listpersons` because that needs to retrieve data from the `person` table.

```
sqlalchemy.exc.OperationalError
sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) FATAL:  password authentication failed for user "helloworld"

(Background on this error at: http://sqlalche.me/e/13/e3q8)
```

![sqlalchemy.exc.OperationalError](images\sqlalchemy-operationalerror.png)

This most likely means that the helloworld user and its database failed to be created.

It is the DB initialization script `scripts\postgres\1-init-user-db.sh`. that creates the user `helloworld` and the database with the same name. 

After that it will proceed to run 2 SQL scripts, one to create the table `person`, and a second script to add two demo users.


### Probable cause of the problem

I have discovered there may be an issue with the database initialization script `scripts\postgres\1-init-user-db.sh`.

When you clone the git repository git may convert Unix's End of Line character `\n`, to the Windows convention of having two characters: `\n\r`.
This trips up the script in the Docker container for the postgres service.

The script runs in a Linux container. But git may convert the linux EOL characters which are a single \n into the Windows convention of having two characters for a newline and carriage return \n\r.

### Quick fix: convert the EoL character, then docker-compose down & up again

A quick fix is to open the following file in a text editor that can convert the EOL characters, such as Notepad++.

`demo-for-engie\scripts\postgres\1-init-user-db.sh`

Then make sure to save `1-init-user-db.sh` with the Unix EOL: \n.


Now to tear down the docker containers so you get a fresh start:

```
# removing all images and volumes as well just to be sure.
docker-compose down --rmi all --volumes
```

And bring them up again, this will rebuild the images as well.

```
docker-compose up
```

### If that does not help, create user and database with psql

You can also create the user and database, but there are a few commands to run which is a bit cumbersome. That's why we wanted this to be done automatically in the first place.


1. Create the user helloworld

```
docker exec -ti demo-for-engie_postgres_1 psql -U postgres -c "CREATE USER helloworld WITH PASSWORD 'example'"
```

Expected output

```
CREATE ROLE
```

2. Create the database helloworld:

```
docker exec -ti demo-for-engie_postgres_1 psql -U postgres -c "CREATE DATABASE helloworld;"
```

Expected output

```
CREATE DATABASE
```

3. Grant all privileges to the user

```
docker exec -ti demo-for-engie_postgres_1 psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE helloworld TO helloworld;"
```

Expected output

```
GRANT
```

4. Next, use the `flask init-db` command on the web container to create the database table `person`.

This command is just easier than using psql to create the table.

```
docker exec -ti demo-for-engie_web_1 flask init-db
```

Expected output

```
Initialized the database
```

**Optional:** If you also want to have the demo persons do the same for the command `flask add-demo-persons`

```
docker exec -ti demo-for-engie_web_1 flask add-demo-persons
```
