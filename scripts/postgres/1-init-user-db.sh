#!/bin/bash
set -e

# TODO: can we also use an environment variable for the helloworld password?
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER helloworld WITH PASSWORD 'example';
    CREATE DATABASE helloworld;
    GRANT ALL PRIVILEGES ON DATABASE helloworld TO helloworld;
EOSQL

psql -v ON_ERROR_STOP=1 --username "helloworld" --dbname "helloworld" -f /docker-entrypoint-initdb.d/data/2-schema-helloworld.sql

psql -v ON_ERROR_STOP=1 --username "helloworld" --dbname "helloworld" -f /docker-entrypoint-initdb.d/data/3-person-data.sql
