#######################
#   Ex12: Worldwide   #
#######################

from utils.utils import run_sql


@run_task("Ex12 Worldwide", oneline=False)
def get_worldwide():
    res = run_sql("""
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
                """, fetch=True)
    for e in res:
        print(e[0])


def main():
    get_worldwide()


if __name__ == "__main__":
    main()
