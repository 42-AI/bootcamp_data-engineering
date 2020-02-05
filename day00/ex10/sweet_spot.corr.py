########################
#   Ex10: Sweet_spot   #
########################

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


def get_sweet_spot():
    conn = get_connection()
    curr = conn.cursor()
    curr.execute("""
        SELECT date_trunc('month', Release_date)
            AS txn_month,
            COUNT(Release_date) as monthly_sum
        FROM appstore_games
        GROUP BY txn_month
        ORDER BY txn_month
    """)
    response = curr.fetchall()
    m = {
        1: "january",
        2: "february",
        3: "march",
        4: "april",
        5: "may",
        6: "june",
        7: "july",
        8: "august",
        9: "september",
        10: "october",
        11: "november",
        12: "december",
    }
    months = {}
    for row in response:
        if row[0].month not in months:
            months[row[0].month] = 0
        months[row[0].month] += row[1]
    print("sweet_spot : ", m[max(months, key=months.get)])
    conn.close()


def main():
    get_sweet_spot()


if __name__ == "__main__":
    main()
