######################
#   Ex03: Populate   #
######################

import pandas as pd
import psycopg2
from correction.utils.utils import run_sql, get_connection

#############
#   UTILS   #
#############


def delete_table(table: str):
    print("\tDeleting table '{}'".format(table), end='')
    run_sql("DROP TABLE IF EXISTS {};".format(table), commit=True)
    print(' Done !')


def display_table(table: str):
    res = run_sql("SELECT * FROM {} LIMIT 10".format(table), fetch=True)
    for row in res:
        print(row)


def import_csv(file):
    print("\tImporting '{}'".format(file), end='')
    df = pd.read_csv(file)
    print(" Done !")
    return (df)


##############################
#   CREATE TABLE FUNCTIONS   #
##############################

def create_table(table, query):
    print("\tCreating table '{}' ...".format(table), end='')
    run_sql(query.format(table), commit=True)
    print(' Done !')


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


def populate_table(table, query, df, index=False):
    print("\tPopulating table '{}' ...".format(table), end='')
    conn = get_connection()
    curr = conn.cursor()
    df_rows = list(df.itertuples(index=index))
    args_str = b",".join(curr.mogrify("%s", (row,)) for row in df_rows)
    curr.execute(query.format(table) + args_str.decode())
    conn.commit()
    conn.close()
    print(' Done !')


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
    print("IMPORTING CSVS ...")

    df = import_csv("appstore_games.normalized.csv")
    df_genres = import_csv("appstore_games_genres.normalized.csv")
    df_languages = import_csv("appstore_games_languages.normalized.csv")

    print("DELETING TABLES ...")

    delete_table("appstore_games_genres")
    delete_table("appstore_games_languages")
    delete_table("appstore_games")

    print("CREATING TABLES ...")

    create_table_appstore_games()
    create_table_appstore_games_genres()
    create_table_appstore_games_languages()

    print("POPULATING TABLES ...")

    populate_appstore_games(df)
    populate_appstore_games_genres(df_genres)
    populate_appstore_games_languages(df_languages)

    print('ALL DONE !')


if __name__ == "__main__":
    main()
