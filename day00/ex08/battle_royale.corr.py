###########################
#   Ex08: Battle_royale   #
###########################

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

def get_battle_royale():
    conn = get_connection()
    curr = conn.cursor()
    curr.execute(""" SELECT Name, Description
                     FROM appstore_games
                     WHERE Description ILIKE '%battle_royale%'
                     AND Description ~ '.*https?://(www\.)?(facebook|fb)\.(com).*';
                 """)
    response = curr.fetchall()
    for row in response:
        print(row[0])
    conn.close()
get_battle_royale()