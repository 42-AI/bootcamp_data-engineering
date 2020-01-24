#####################
#   Ex06: K-first   #
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

def get_k_first():
    conn = get_connection()
    curr = conn.cursor()
    curr.execute(""" SELECT Developer
                     FROM appstore_games
                     INNER JOIN appstore_games_genres
                     ON appstore_games.Game_Id = appstore_games_genres.Game_Id
                     WHERE Developer LIKE 'K%'
                     AND appstore_games_genres.Genre LIKE '%Casual%';
                 """)
    response = curr.fetchall()
    for row in response:
        print(row[0])
    conn.close()
get_k_first()