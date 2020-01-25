######################
#   Ex03: Populate   #
######################

import pandas as pd
import psycopg2
from psycopg2.extensions import AsIs


######################
#   SET CONNECTION   #
######################

def get_connection():
    conn = psycopg2.connect(
        database="appstore_games",
        host="localhost",
        user="postgres_user",
        password="12345"
    )
    return (conn)


####################
#   DELETE TABLE   #
####################

def delete_table(table: str):
    print("\tdeleting table '{}'".format(table), end='')
    conn = get_connection()
    curr = conn.cursor()
    curr.execute("DROP TABLE IF EXISTS %(table)s;", {"table": AsIs(table)})
    conn.commit()
    conn.close()
    print(' done !')


#####################
#   DISPLAY TABLE   #
#####################

def display_table(table: str):
    conn = get_connection()
    curr = conn.cursor()
    curr.execute("SELECT * FROM %(table)s LIMIT 10", {"table": AsIs(table)})
    response = curr.fetchall()
    for row in response:
        print(row)
    conn.close()


##############################
#   CREATE TABLE FUNCTIONS   #
##############################

def create_table_appstore_games():
    print("\tcreating table 'appstore_games' ...", end='')
    conn = get_connection()
    curr = conn.cursor()
    curr.execute("""CREATE TABLE IF NOT EXISTS appstore_games(
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
    conn.commit()
    conn.close()
    print(' done !')


def create_table_appstore_games_languages():
    print("\tcreating table 'appstore_games_languages' ...", end='')
    conn = get_connection()
    curr = conn.cursor()
    curr.execute("""CREATE TABLE IF NOT EXISTS appstore_games_languages(
             Id bigint PRIMARY KEY,
             Game_Id bigint REFERENCES appstore_games(Game_id),
             Language varchar
             );""")
    conn.commit()
    conn.close()
    print(' done !')


def create_table_appstore_games_genres():
    print("\tcreating table 'appstore_games_genres' ...", end='')
    conn = get_connection()
    curr = conn.cursor()
    curr.execute("""CREATE TABLE IF NOT EXISTS appstore_games_genres(
             Id bigint PRIMARY KEY,
             Game_Id bigint REFERENCES appstore_games(Game_id),
             Primary_genre varchar,
             Genre varchar
             );""")
    conn.commit()
    conn.close()
    print(' done !')


##########################
#   POPULATE FUNCTIONS   #
##########################

def populate_appstore_games(df):
    print("\tpopulating table 'appstore_games' ...", end='')
    conn = get_connection()
    curr = conn.cursor()
    for idx in range(df.shape[0]):
        tmp = df.iloc[idx]
        curr.execute("""INSERT INTO appstore_games
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
            Last_update) VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                     (int(tmp["ID"]),
                      tmp["Name"],
                      tmp["Average User Rating"],
                      int(tmp["User Rating Count"]),
                      tmp["Price"],
                      tmp["Description"],
                      tmp["Developer"],
                      int(tmp["Age Rating"]),
                      int(tmp["Size"]),
                      tmp["Original Release Date"],
                      tmp["Current Version Release Date"]
                      ))
    conn.commit()
    conn.close()
    print(' done !')


def populate_appstore_games_genres(df):
    print("\tpopulating table 'appstore_games_genres' ...", end='')
    conn = get_connection()
    curr = conn.cursor()
    for idx in range(df.shape[0]):
        tmp = df.iloc[idx]
        curr.execute("""INSERT INTO appstore_games_genres
            (Id,
            Game_Id,
            Primary_genre,
            Genre) VALUES
            (%s, %s, %s, %s)""",
                     (idx,
                      int(tmp["ID"]),
                      tmp["Primary Genre"],
                      tmp["Genres"]
                      ))
    conn.commit()
    conn.close()
    print(' done !')


def populate_appstore_games_languages(df):
    print("\tpopulating table 'appstore_games_languages' ...", end='')
    conn = get_connection()
    curr = conn.cursor()
    for idx in range(df.shape[0]):
        tmp = df.iloc[idx]
        curr.execute("""INSERT INTO appstore_games_languages
            (Id,
            Game_Id,
            Language) VALUES
            (%s, %s, %s)""",
                     (idx,
                      int(tmp["ID"]),
                      tmp["Languages"]
                      ))
    conn.commit()
    conn.close()
    print(' done !')


############
#   MAIN   #
############


def main():
    print("IMPORTING CSVS ...")

    print("\timporting '{}'".format('appstore_games.normalized.csv'), end='')
    df = pd.read_csv("appstore_games.normalized.csv")
    print(' done !')
    print("\timporting '{}'".format(
        'appstore_games_genres.normalized.csv'), end='')
    df_genres = pd.read_csv("appstore_games_genres.normalized.csv")
    print(' done !')
    print("\timporting '{}'".format(
        'appstore_games_languages.normalized.csv'), end='')
    df_languages = pd.read_csv("appstore_games_languages.normalized.csv")
    print(' done !')

    print("DELETING TABLES ...")

    delete_table("appstore_games")
    delete_table("appstore_games_genres")
    delete_table("appstore_games_languages")

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
