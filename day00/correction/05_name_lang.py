#######################
#   Ex05: Name_lang   #
#######################

from utils.utils import run_sql


@run_task("Ex05 Name_lang", oneline=False)
def get_name_lang():
    res = run_sql("""
            SELECT Name, Language
                FROM appstore_games
                INNER JOIN appstore_games_languages
                ON appstore_games.Game_Id =
                    appstore_games_languages.Game_Id
                WHERE appstore_games.Price > 5.0
                AND appstore_games.Price < 10.0
            """, fetch=True)
    for row in res:
        print(row[0], row[1])


def main():
    get_name_lang()


if __name__ == "__main__":
    main()
