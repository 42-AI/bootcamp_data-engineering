######################
#   Ex03: Populate   #
######################

import pandas as pd
import psycopg2


#############
#   UTILS   #
#############

def get_connection():
    conn = psycopg2.connect(
        database="appstore_games",
        host="localhost",
        user="postgres_user",
        password="12345"
    )
    return (conn)


def run_sql(query: str,
            db="appstore_games",
            passwd="12345",
            fetch=False,
            commit=False):
    res = ""

    # Connection to the database
    try:
        conn = psycopg2.connect(
            database=db,
            host="localhost",
            user="postgres_user",
            password=passwd
        )
    except Exception as e:
        print("Connection Error :: {}".format(str(e).strip()))
        return (res)
    curr = conn.cursor()

    # Run sql query
    try:
        curr.execute("{}".format(query))
    except Exception as e:
        print("Query Error :: {}".format(str(e).strip()))

    # Fetch results
    if fetch:
        res = curr.fetchall()
    if commit:
        conn.commit()
    conn.close()
    return (res)


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
                     Game_Id bigint,
                     Language varchar
                 );""")


def create_table_appstore_games_genres():
    create_table("appstore_games_genres",
                 """
                 CREATE TABLE IF NOT EXISTS {} (
                     Id bigint PRIMARY KEY,
                     Game_Id bigint,
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
