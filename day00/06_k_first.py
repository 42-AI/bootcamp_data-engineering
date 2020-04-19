#####################
#   Ex06: K-first   #
#####################

from utils.utils import run_sql


@run_task("Ex06 K-first", oneline=False)
def get_k_first():
    res = run_sql("""
                    SELECT Developer
                        FROM appstore_games
                        INNER JOIN appstore_games_genres
                        ON appstore_games.Game_Id = appstore_games_genres.Game_Id
                        WHERE Developer LIKE 'K%'
                        AND appstore_games_genres.Genre LIKE '%Casual%';
                 """, fetch=True)
    for row in res:
        print(row[0])


def main():
    get_k_first()


if __name__ == "__main__":
    main()
