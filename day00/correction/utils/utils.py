###################
#   Ex00: Setup   #
###################

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def get_connection(
				user="postgres_user",
				db="appstore_games",
				passwd="12345"
				):
    conn = psycopg2.connect(
        database=db,
        host="localhost",
        user=user,
        password=passwd
    )
    return (conn)

def run_sql(query: str,
			user="postgres_user",
            db="appstore_games",
            passwd="12345",
            fetch=False,
            commit=False):
    res = ""

    # Connection to the database
    try:
        conn = psycopg2.connect(
            dbname=db,
            user=user,
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
