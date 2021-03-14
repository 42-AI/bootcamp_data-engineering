FROM postgres:12.2-alpine

# run init.sql
ADD init.sql /docker-entrypoint-initdb.d
ADD pg_hba.conf /var/lib/postgresql/data