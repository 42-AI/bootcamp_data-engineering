######################
#   Ex09: Benefits   #
######################

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


def get_benefits():
    conn = get_connection()
    curr = conn.cursor()
    curr.execute(""" SELECT Name
                     FROM appstore_games
                     ORDER BY (User_rating_count * Price) DESC
                     LIMIT 10;
                 """)
    response = curr.fetchall()
    for row in response:
        print(row[0])
    conn.close()


def main():
    get_benefits()


if __name__ == "__main__":
    main()
