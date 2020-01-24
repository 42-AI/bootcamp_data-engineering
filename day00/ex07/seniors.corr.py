#####################
#   Ex07: Seniors   #
#####################

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

def get_seniors():
    conn = get_connection()
    curr = conn.cursor()
    curr.execute(""" SELECT Developer
                     FROM appstore_games 
                     WHERE appstore_games.Release_date < '2008-07-30 00:00:00'
                     AND appstore_games.Last_update > '2018-01-01 00:00:00';
                 """)
    response = curr.fetchall()
    for row in response:
        print(row[0])
    conn.close()
get_seniors()