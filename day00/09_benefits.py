######################
#   Ex09: Benefits   #
######################

from correction.utils.utils import run_sql


@run_task("Ex09 Benefits", oneline=False)
def get_benefits():
    res = run_sql("""
                    SELECT Name
                    FROM appstore_games
                    ORDER BY (User_rating_count * Price) DESC
                    LIMIT 10;
                 """, fetch=True)
    for row in res:
        print(row[0])


def main():
    get_benefits()


if __name__ == "__main__":
    main()
