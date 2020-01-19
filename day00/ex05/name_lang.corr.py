#######################
#   Ex05: Name_lang   #
#######################

import psycopg2
from psycopg2.extensions import AsIs

def get_name_lang():
    conn = psycopg2.connect(
        database="appstore_games",
        host="localhost",
        user="postgres_user",
        password="12345"
    )
    curr = conn.cursor()
    curr.execute(""" SELECT Name, Language
                     FROM appstore_games
                     INNER JOIN appstore_games_languages
                     ON appstore_games.Game_Id = appstore_games_languages.Game_Id
                     WHERE appstore_games.Price > 5.0
                     AND appstore_games.Price < 10.0
                 """)
    response = curr.fetchall()
    for row in response:
        print(row)
    conn.close()
get_name_lang()