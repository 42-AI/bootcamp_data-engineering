###################
#   Ex11: Price   #
###################

import psycopg2
from psycopg2.extensions import AsIs

import numpy as np
import matplotlib.pyplot as plt


def get_connection():
    conn = psycopg2.connect(
        database="appstore_games",
        host="localhost",
        user="postgres_user",
        password="12345"
    )
    return (conn)


def get_price():
    conn = get_connection()
    curr = conn.cursor()
    curr.execute(""" SELECT Price, COUNT(Price)
                     FROM appstore_games
                     GROUP BY Price
                     ORDER BY Price
                 """)
    response = curr.fetchall()
    response = sorted(response)
    data = []
    for e in response:
        for _ in range(e[1]):
            data.append(e[0])
    print("mean price : ", np.mean(data))
    print("std price : ", np.std(data))
    data = [e for e in data if e > 0]
    bins = []
    for i in range(0, 200, 3):
        bins.append(i)
    plt.hist(data, bins)
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    plt.title("Appstore games price")
    plt.savefig("price.png")
    plt.show()
    conn.close()


def main():
    get_price()


if __name__ == "__main__":
    main()
