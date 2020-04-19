######################
#   Ex03: Populate   #
######################

import pandas as pd
import psycopg2
from utils.utils import run_sql, get_connection

#############
#   UTILS   #
#############


@run_task("Deleting table '{0}'")
def delete_table(table: str):
    run_sql("DROP TABLE IF EXISTS {};".format(table), commit=True)


def display_table(table: str):
    res = run_sql("SELECT * FROM {} LIMIT 10".format(table), fetch=True)
    for row in res:
        print(row)


@run_task("Importing csv '{0}'")
def import_csv(file):
    df = pd.read_csv(file)
    return (df)


##############################
#   CREATE TABLE FUNCTIONS   #
##############################


@run_task("Creating table '{0}'")
def create_table(table, query):
    run_sql(query.format(table), commit=True)


def create_table_appstore_games():
    create_table("appstore_games",
                 """
                 CREATE TABLE IF NOT EXISTS {} (
                     Game_Id bigint PRIMARY KEY,
                     Name varchar,
                     Avg_user_rating float,
                     User_rating_count int,
                     Price float,
                     Description varchar,
                     Developer varchar,
                     Age_rating int,
                     Size bigint,
                     Release_date date,
                     Last_update date
                 );""")


def create_table_appstore_games_languages():
    create_table("appstore_games_languages",
                 """
                 CREATE TABLE IF NOT EXISTS {} (
                     Id bigint PRIMARY KEY,
                     Game_Id bigint REFERENCES appstore_games(Game_Id),
                     Language varchar
                 );""")


def create_table_appstore_games_genres():
    create_table("appstore_games_genres",
                 """
                 CREATE TABLE IF NOT EXISTS {} (
                     Id bigint PRIMARY KEY,
                     Game_Id bigint REFERENCES appstore_games(Game_Id),
                     Primary_genre varchar,
                     Genre varchar
                 );""")


##########################
#   POPULATE FUNCTIONS   #
##########################


@run_task("Populating table '{0}'", oneline=False)
def populate_table(table, query, df, index=False):
    conn = get_connection()
    curr = conn.cursor()
    df_rows = list(df.itertuples(index=index))
    args_str = b",".join(curr.mogrify("%s", (row,)) for row in df_rows)
    curr.execute(query.format(table) + args_str.decode())
    conn.commit()
    conn.close()


def populate_appstore_games(df):
    populate_table("appstore_games",
                   """
                   INSERT INTO {}
                       (Game_Id,
                       Name,
                       Avg_user_rating,
                       User_rating_count,
                       Price,
                       Description,
                       Developer,
                       Age_rating,
                       Size,
                       Release_date,
                       Last_update) VALUES """, df)


def populate_appstore_games_genres(df_genres):
    populate_table("appstore_games_genres",
                   """
                   INSERT INTO {}
                       (Id,
                       Game_Id,
                       Primary_genre,
                       Genre) VALUES """, df_genres, index=True)


def populate_appstore_games_languages(df_languages):
    populate_table("appstore_games_languages",
                   """
                   INSERT INTO {}
                       (Id,
                       Game_Id,
                       Language) VALUES """, df_languages, index=True)


############
#   MAIN   #
############


def main():
    df = import_csv("appstore_games.normalized.csv")
    df_genres = import_csv("appstore_games_genres.normalized.csv")
    df_languages = import_csv("appstore_games_languages.normalized.csv")

    delete_table("appstore_games_genres")
    delete_table("appstore_games_languages")
    delete_table("appstore_games")

    create_table_appstore_games()
    create_table_appstore_games_genres()
    create_table_appstore_games_languages()

    populate_appstore_games(df)
    populate_appstore_games_genres(df_genres)
    populate_appstore_games_languages(df_languages)


if __name__ == "__main__":
    main()
