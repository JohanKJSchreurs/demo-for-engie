FROM postgres:13.2

LABEL author="Johan Schreurs"

COPY scripts/postgres/1-init-user-db.sh  /docker-entrypoint-initdb.d/1-init-user-db.sh
COPY scripts/postgres/data/*  /docker-entrypoint-initdb.d/data/

VOLUME /code
