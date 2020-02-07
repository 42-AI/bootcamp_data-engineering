#######################
#   Ex12: Worldwide   #
#######################

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


def get_worldwide():
    conn = get_connection()
    curr = conn.cursor()
    curr.execute("""
                SELECT Genre, COUNT(appstore_games_genres.Game_Id)
                FROM appstore_games_genres
                INNER JOIN (
                    SELECT Game_Id, COUNT(Language)
                    FROM appstore_games_languages
                    GROUP BY Game_Id
                    HAVING COUNT(Language) >= 3
                ) Game_lang_freq
                ON appstore_games_genres.Game_Id = Game_lang_freq.Game_Id
                GROUP BY Genre
                ORDER BY COUNT(appstore_games_genres.Game_Id) DESC
                LIMIT 5
                """)

    response = curr.fetchall()
    for e in response:
        print(e[0])
    conn.close()


def main():
    get_worldwide()


if __name__ == "__main__":
    main()
