##################
#   Ex10: Rank   #
##################

import psycopg2
from psycopg2.extensions import AsIs


def get_connection():
    conn = psycopg2.connect(
        database="appstore_games",
        host="localhost",
        user="postgres_user",
        password="12345"
    )
    return (conn)


def get_rank():
    conn = get_connection()
    curr = conn.cursor()
    curr.execute(""" SELECT Name
                     FROM appstore_games
                     ORDER BY Avg_user_rating DESC, Name
                     LIMIT 100;
                 """)
    response = curr.fetchall()
    tmp = {}
    for row in response:
        print(row[0])
    curr.execute(""" SELECT Name
                     FROM appstore_games
                     ORDER BY Avg_user_rating, Name
                     LIMIT 100;
                 """)
    response = curr.fetchall()
    tmp = {}
    for row in response:
        print(row[0])
    conn.close()


def main():
    get_rank()


if __name__ == "__main__":
    main()
