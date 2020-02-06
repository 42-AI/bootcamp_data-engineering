###################
#   Ex00: Setup   #
###################

import getpass
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

###################
#   BOILERPLATE   #
###################


def run_sql(query: str,
            db="postgres",
            passwd="12345",
            fetch=False,
            commit=False):
    res = ""

    # Connection to the database
    try:
        conn = psycopg2.connect(
            dbname=db,
            user="postgres",
            host="localhost",
            password=passwd
        )
    except Exception as e:
        print("Connection Error :: {}".format(str(e).strip()))
        return(res)
    if commit:
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    curr = conn.cursor()

    # Run sql query
    try:
        curr.execute("{}".format(query))
    except Exception as e:
        print("Query Error :: {}".format(str(e).strip()))

    # Fetch results
    if fetch:
        res = curr.fetchall()
    if commit:
        conn.commit()

    conn.close()
    return (res)


#################
#   FUNCTIONS   #
#################


def create_database(db: str):
    print("Creating '{}' database ... ".format(db), end="")
    run_sql("CREATE DATABASE {}".format(db), commit=True)
    print("Done !")


def drop_database(db: str):
    print("Dropping '{}' database ... ".format(db), end="")
    run_sql("DROP DATABASE IF EXISTS {}".format(db), commit=True)
    print("Done !")


def change_passwd(user: str, passwd: str):
    print("Changing password for '{}' ... ".format(user), end="")
    run_sql("ALTER USER {} PASSWORD '{}';".format(user, passwd), commit=True)
    print("Done !")


def create_user(user: str, password: str):
    print("Creating '{}' user ... ".format(user), end="")
    run_sql("CREATE USER {} LOGIN PASSWORD '{}'".format(user, password),
            commit=True)
    print("Done !")


def drop_user(user: str):
    print("Dropping '{}' user ... ".format(user), end="")
    run_sql("DROP USER IF EXISTS {}".format(user), commit=True)
    print("Done !")


def alter_database(db: str, user: str):
    print("Altering '{}' database, owner is '{}' ... ".format(db, user),
          end="")
    run_sql("ALTER DATABASE {} OWNER TO {}".format(db, user), commit=True)
    print("Done !")


def main():
    change_passwd("postgres", "12345")
    drop_database("appstore_games")
    create_database("appstore_games")
    drop_user("postgres_user")
    create_user("postgres_user", "12345")
    alter_database("appstore_games", "postgres_user")


if __name__ == "__main__":
    main()
