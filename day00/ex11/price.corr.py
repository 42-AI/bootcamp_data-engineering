###################
#   Ex11: Price   #
###################

import psycopg2
from psycopg2.extensions import AsIs

import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline


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
    curr.execute(""" SELECT Price
                     FROM appstore_games
                 """)
    response = curr.fetchall()
    uniq = sorted(set(response))
    data = []
    for e in uniq:
        if int(e[0]) == 0:
            continue
        for _ in range(response.count(e)):
            data.append(e[0])
    bins = []
    for i in range(0, 200, 3):
        bins.append(i)
    plt.hist(data, bins)
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    plt.title("Appstore games price")
    plt.savefig("price.png")
    plt.show()
    print("mean price : ", np.mean(response))
    print("std price : ", np.std(response))
    conn.close()


def main():
    get_price()


if __name__ == "__main__":
    main()
