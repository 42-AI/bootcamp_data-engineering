###################
#   Ex00: Setup   #
###################

import psycopg2
import os
import getpass
from utils.utils import run_sql, run_task

if os.uname()[0] == "Linux":
    USER = "postgres"
else:
    USER = getpass.getuser()

#################
#   FUNCTIONS   #
#################


@run_task("'{0}' database creation")
def create_database(db: str):
    run_sql("CREATE DATABASE {}".format(db),
            user=USER, db="postgres", commit=True)


@run_task("'{0}' database deletion")
def drop_database(db: str):
    run_sql("DROP DATABASE IF EXISTS {}".format(db),
            user=USER, db="postgres", commit=True)


@run_task("Password change for user '{0}'")   
def change_passwd(user="dd", passwd:str="dd"):
    run_sql("ALTER USER {} PASSWORD '{}';".format(user, passwd),
            user=USER, db="postgres", commit=True)


@run_task("'{0}' user creation")
def create_user(user: str, password: str):
    run_sql("CREATE USER {} LOGIN PASSWORD '{}'".format(user, password),
            user=USER, db="postgres", commit=True)


@run_task("'{0}' user deletion")
def drop_user(user: str):
    run_sql("DROP USER IF EXISTS {}".format(user),
            user=USER, db="postgres", commit=True)


@run_task("'{0}' database owner change to '{1}'")
def alter_database(db: str, user: str):
    run_sql("ALTER DATABASE {} OWNER TO {}".format(db, user),
            user=USER, db="postgres", commit=True)


def main():
    change_passwd(USER, "12345")
    drop_database("appstore_games")
    create_database("appstore_games")
    drop_user("postgres_user")
    create_user("postgres_user", "12345")
    alter_database("appstore_games", "postgres_user")


if __name__ == "__main__":
    main()
