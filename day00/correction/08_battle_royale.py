###########################
#   Ex08: Battle_royale   #
###########################

from utils.utils import run_sql


@run_task("Ex08 Battle_royale", oneline=False)
def get_battle_royale():
    res = run_sql("""
                    SELECT Name, Description
                    FROM appstore_games
                    WHERE Description ILIKE '%battle_royale%'
                    AND Description ~
                    '.*https?://(www.)?(facebook|fb).(com).*';
                 """, fetch=True)
    for row in res:
        print(row[0])


def main():
    get_battle_royale()


if __name__ == "__main__":
    main()
