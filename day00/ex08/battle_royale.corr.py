###########################
#   Ex08: Battle_royale   #
###########################

import psycopg2
from psycopg2.extensions import AsIs

def get_battle_royale():
    conn = psycopg2.connect(
        database="appstore_games",
        host="localhost",
        user="postgres_user",
        password="12345"
    )
    curr = conn.cursor()
    curr.execute(""" SELECT Name, Description
                     FROM appstore_games
                     WHERE Description
                     ILIKE '%battle_royale%';
                 """)
    response = curr.fetchall()
    count = 0
    for row in response:
        if re.match(r'.*http.{1,10}(facebook|fb).*', row[1]):
            print(row)
            count += 1
    print(count)
    conn.close()
get_battle_royale()