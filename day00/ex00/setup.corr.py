###################
#   Ex00: Setup   #
###################

import getpass
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def get_default_connection():
    conn = psycopg2.connect(
        dbname='postgres',
        user=getpass.getuser(),
        host='',
        password="12345"
    )
    return (conn)


def create_database(db: str):
    conn = get_default_connection()
    # AUTOCOMMIT allows database changes in python
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    curr = conn.cursor()
    curr.execute("CREATE DATABASE {}".format(db, db))
    conn.commit()
    conn.close()


def drop_database(db: str):
    conn = get_default_connection()
    # AUTOCOMMIT allows database changes in python
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    curr = conn.cursor()
    curr.execute("DROP DATABASE IF EXISTS {}".format(db))
    conn.commit()
    conn.close()


def create_pg_user(user: str, password: str):
    conn = get_default_connection()
    # AUTOCOMMIT allows database changes in python
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    curr = conn.cursor()
    curr.execute("CREATE USER {} LOGIN PASSWORD '{}'".format(user, password))
    conn.commit()
    conn.close()


def drop_pg_user(user: str):
    conn = get_default_connection()
    # AUTOCOMMIT allows database changes in python
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    curr = conn.cursor()
    curr.execute("DROP USER IF EXISTS {}".format(user))
    conn.commit()
    conn.close()


def alter_database(db: str, user: str):
    conn = get_default_connection()
    # AUTOCOMMIT allows database changes in python
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    curr = conn.cursor()
    curr.execute("ALTER DATABASE {} OWNER TO {}".format(db, user))
    conn.commit()
    conn.close()


def main():
    print("Drop 'appstore_games' database")
    drop_database("appstore_games")
    print("Create 'appstore_games' database")
    create_database("appstore_games")
    print("Drop user '{}'".format("postgres_user"))
    drop_pg_user("postgres_user")
    print("Create user '{}'".format("postgres_user"))
    create_pg_user("postgres_user", "12345")
    print("Give '{}' database ownership to '{}'".format(
        "appstore_games", "postgres_user"))
    alter_database("appstore_games", "postgres_user")


if __name__ == "__main__":
    main()
