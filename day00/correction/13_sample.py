####################
#   Ex13: Sample   #
####################

import math
from utils.utils import run_sql


def get_sample_size(
        population,
        confidence=.95,
        error_margin=.05,
        std=0.5):
    conf_zscore = {
        .80 : 1.28,
        .85 : 1.44,
        .90 : 1.65,
        .95 : 1.96,
        .99 : 2.58
    }
    z = conf_zscore[confidence]
    p = std
    num = ((z ** 2) * (p * (1 - p))) / (error_margin ** 2)
    den = 1 + (((z ** 2) * (p * (1 - p))) / ((error_margin ** 2) * population))
    return(math.ceil(num / den))


def sample():
    res = run_sql("""
                SELECT *
                FROM appstore_games
                """, fetch=True)
    sample_size = get_sample_size(len(res))
    conn = get_connection()
    df = pd.read_sql_query("""
                SELECT *
                FROM appstore_games
                ORDER BY random()
                LIMIT {}
                """.format(sample_size), conn)
    df.to_csv("appstore_games.sample.csv", index=False)


def main():
    sample()


if __name__ == "__main__":
    main()

