FROM postgres:13.2

LABEL author="Johan Schreurs"

COPY scripts/postgres/1-init-user-db.sh  /docker-entrypoint-initdb.d/1-init-user-db.sh
COPY scripts/postgres/data/*  /docker-entrypoint-initdb.d/data/

RUN apt update && apt-get install -y dos2unix && dos2unix /docker-entrypoint-initdb.d/1-init-user-db.sh

