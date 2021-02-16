# Troubleshooting Guide

## Error: password authentication failed for user "helloworld"

This most likely means that the helloworld user and its database failed to be created.

```
sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) FATAL:  password authentication failed for user "helloworld"
```

I have discovered there may be an issue with the database initialization script `scripts\postgres\1-init-user-db.sh`.

When you clone the git repository git may convert Unix's End of Line character `\n`, to the Windows convention of having two characters: `\n\r`.
This trips up the script in the Docker container for the postgres service.

The script runs in a Linux container. But git may convert the linux EOL characters which are a single \n into the Windows convention of having two characters for a newline and carriage return \n\r.

### Quick fix

A quick fix is to open the following file in a text editor that can convert the EOL characters, such as Notepad++.

`demo-for-engie\scripts\postgres\1-init-user-db.sh`

Then make sure to save `1-init-user-db.sh` with the Unix EOL: \n.

Now tear down the docker containers:

```
# removing all images and volumes as well just to be sure.
docker-compose down --rmi all --volumes
```

And rebuild / bring them up again 

```
docker-compose up
```

### If that does not help, create user and database with psql

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
docker exec -ti demo-for-engie_postgres_1 psql -U postgres -c "CREATE DATABASE helloworld2;"
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

4. Next, use the `flask init-db` command on the web container to create the database

```
docker exec -ti demo-for-engie_web_1 flask init-db
```

Expected output

```
Initialized the database
```

If you also want the demo persons do the same for the command `flask add-demo-persons`

```
docker exec -ti demo-for-engie_web_1 flask add-demo-persons
```

