####################
#   Ex04: Top100   #
####################

from utils.utils import run_sql


def get_top_100():
    res = run_sql("""
            SELECT Name, Avg_user_rating
            FROM appstore_games
            WHERE Name ~ '^[A-Za-z]'
            ORDER BY Avg_user_rating DESC, Name
            LIMIT 100
            """, fetch=True)
    for row in res:
        print(row[0])


def main():
    get_top_100()


if __name__ == "__main__":
    main()
