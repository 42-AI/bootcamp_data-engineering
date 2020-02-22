#####################
#   Ex07: Seniors   #
#####################

from utils.utils import run_sql


@run_task("Ex07 Seniors", oneline=False)
def get_seniors():
    res = run_sql("""
                    SELECT Developer
                    FROM appstore_games
                    WHERE appstore_games.Release_date < '2008-08-01 00:00:00'
                    AND appstore_games.Last_update > '2018-01-01 00:00:00';
                 """, fetch=True)
    for row in res:
        print(row[0])


def main():
    get_seniors()


if __name__ == "__main__":
    main()
