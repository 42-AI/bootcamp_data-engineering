###################
#   Ex11: Price   #
###################


import numpy as np
import matplotlib.pyplot as plt
from utils.utils import run_sql


@run_task("Ex11 Price", oneline=False)
def get_price():
    res= run_sql("""
                    SELECT Price, COUNT(Price)
                    FROM appstore_games
                    WHERE Price > 1
                    GROUP BY Price
                    ORDER BY Price
                 """, fetch=True)
    d = []
    for k, v in res:
        d += [k] * v
    print("mean price : ", np.mean(d))
    print("std price : ", np.std(d))
    bins = [i for i in range(0, 200, 3)]
    plt.hist([e[1] for e in res], bins)
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    plt.title("Appstore games price")
    plt.savefig("price.png")
    plt.show()


def main():
    get_price()


if __name__ == "__main__":
    main()
