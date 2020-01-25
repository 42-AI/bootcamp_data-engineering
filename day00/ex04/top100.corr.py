####################
#   Ex04: Top100   #
####################

import psycopg2
from psycopg2.extensions import AsIs
import re


def get_connection():
    conn = psycopg2.connect(
        database="appstore_games",
        host="localhost",
        user="postgres_user",
        password="12345"
    )
    return (conn)


def get_top_100():
    conn = get_connection()
    curr = conn.cursor()
    curr.execute(""" SELECT Name, Avg_user_rating
                     FROM appstore_games
                     WHERE Name !~ '^[0-9]'
                     ORDER BY Avg_user_rating DESC, Name
                     LIMIT 100
                 """)
    response = curr.fetchall()
    for row in response:
        print(row[0])
    conn.close()


def main():
    get_top_100()


if __name__ == "__main__":
    main()
