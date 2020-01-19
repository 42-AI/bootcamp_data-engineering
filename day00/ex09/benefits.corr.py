######################
#   Ex09: Benefits   #
######################

import psycopg2
from psycopg2.extensions import AsIs

def get_benefits():
    conn = psycopg2.connect(
        database="appstore_games",
        host="localhost",
        user="postgres_user",
        password="12345"
    )
    curr = conn.cursor()
    curr.execute(""" SELECT Name, User_rating_count, Price
                     FROM appstore_games;
                 """)
    response = curr.fetchall()
    tmp = {}
    for row in response:
        tmp [row[0]] = round(row[1] * row[2], 2)
        
    tmp = {k: v for k, v in sorted(tmp.items(), key=lambda item: item[1], reverse=True)}
    count = 0
    for k, v in tmp.items():
        print(k)
        count += 1
        if count == 10:
            break
    conn.close()
get_benefits()