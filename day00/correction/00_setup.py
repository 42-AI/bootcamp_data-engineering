##################
#   Ex00: Setup   #
###################

import getpass
import os

from utils.utils import run_sql

if os.uname()[0] == "Linux":
    USER = "postgres"
else:
    USER = getpass.getuser()


#################
#   FUNCTIONS   #
#################


def create_database(db: str):
    print("Creating '{}' database ... ".format(db), end="")
    run_sql("CREATE DATABASE {}".format(db),
            user=USER, db="postgres", commit=True)
    print("Done !")


def drop_database(db: str):
    print("Dropping '{}' database ... ".format(db), end="")
    run_sql("DROP DATABASE IF EXISTS {}".format(db),
            user=USER, db="postgres", commit=True)
    print("Done !")


def change_passwd(user: str, passwd: str):
    print("Changing password for '{}' ... ".format(user), end="")
    run_sql("ALTER USER {} PASSWORD '{}';".format(user, passwd),
            user=USER, db="postgres", commit=True)
    print("Done !")


def create_user(user: str, password: str):
    print("Creating '{}' user ... ".format(user), end="")
    run_sql("CREATE USER {} LOGIN PASSWORD '{}'".format(user, password),
            user=USER, db="postgres", commit=True)
    print("Done !")


def drop_user(user: str):
    print("Dropping '{}' user ... ".format(user), end="")
    run_sql("DROP USER IF EXISTS {}".format(user),
            user=USER, db="postgres", commit=True)
    print("Done !")


def alter_database(db: str, user: str):
    print("Altering '{}' database, owner is '{}' ... ".format(db, user),
          end="")
    run_sql("ALTER DATABASE {} OWNER TO {}".format(db, user),
            user=USER, db="postgres", commit=True)
    print("Done !")


def main():
    change_passwd(USER, "12345")
    drop_database("appstore_games")
    create_database("appstore_games")
    drop_user("postgres_user")
    create_user("postgres_user", "12345")
    alter_database("appstore_games", "postgres_user")


if __name__ == "__main__":
    main()
