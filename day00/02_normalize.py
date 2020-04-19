#######################
#   Ex02: Normalize   #
#######################


import re
import pandas as pd


def nf_normalization_genres(df):
    """Get normalized genres dataframe.
    Args:
      df: pandas dataframe.
    Returns:
      df_genres: pandas dataframe.
    Raises:
      This function shouldn't raise any Exception.
    """
    df_genres = df[["ID", "Primary Genre", "Genres"]].copy()
    df_genres['Genre'] = df_genres['Genres'].apply(lambda x: re.sub(r' & ', '_&_', x))
    df_genres["Genre"] = df_genres["Genre"].apply(lambda x: re.split(r'[ ,]+', x))
    df_genres = df_genres.drop(columns=['Genres'])
    df_genres = df_genres.explode('Genre')
    df_genres = df_genres[df_genres["Genre"] != "Games"]
    df_genres = df_genres.reset_index(drop=True)
    return(df_genres)


def nf_normalization_languages(df):
    """Get normalized languages dataframe.
    Args:
      df: pandas dataframe.
    Returns:
      df_languages: pandas dataframe.
    Raises:
      This function shouldn't raise any Exception.
    """
    df_languages = df[["ID", "Languages"]].copy()
    df_languages["Language"] = (
      df_languages["Languages"].apply(lambda x: re.split(r'[ ,]+', x))
    )
    df_languages = df_languages.drop(columns=['Languages'])
    df_languages = df_languages.explode('Language')
    df_languages = df_languages.reset_index(drop=True)
    return(df_languages)


@run_task('Normalization of data', oneline=False)
def main():
    df = pd.read_csv("appstore_games.cleaned.csv")

    # normalize dataframes
    df_genres = nf_normalization_genres(df)
    df_languages = nf_normalization_languages(df)
    df = df.drop(['Languages', 'Primary Genre', 'Genres'], axis=1)

    # saving dataframes into csv files
    df.to_csv("appstore_games.normalized.csv", index=False)
    df_genres.to_csv("appstore_games_genres.normalized.csv", index=False)
    df_languages.to_csv("appstore_games_languages.normalized.csv", index=False)


if __name__ == "__main__":
    main()
