########################
#   Ex10: Sweet_spot   #
########################

from utils.utils import run_sql


@run_task("Ex10 Sweet_spot", oneline=False)
def get_sweet_spot():
    res = run_sql("""
        SELECT MAX(month)
        FROM (
            SELECT TO_CHAR(Release_date, 'month') AS month, COUNT(*)
            FROM appstore_games
            GROUP BY TO_CHAR(Release_date, 'month')
        ) month_counts
    """, fetch=True)
    for row in res:
        print(row[0])


def main():
    get_sweet_spot()


if __name__ == "__main__":
    main()