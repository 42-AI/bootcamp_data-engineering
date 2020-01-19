####################
#   Ex04: Top100   #
####################

import psycopg2
from psycopg2.extensions import AsIs
import re

def get_top_100():
    conn = psycopg2.connect(
        database="appstore_games",
        host="localhost",
        user="postgres_user",
        password="12345"
    )
    curr = conn.cursor()
    curr.execute(""" SELECT Name, Avg_user_rating
                     FROM appstore_games 
                     ORDER BY Avg_user_rating DESC, Name
                 """)
    response = curr.fetchall()
    count = 0
    for row in response:
        if not re.match(r'^[0-9]*', row[0])[0]:
            count += 1
            print(row[0])
        if count == 100:
            break
    conn.close()
get_top_100()