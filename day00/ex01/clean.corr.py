###################
#   Ex01: Clean   #
###################


import pandas as pd
import re


def df_nan_filter(df):
    """Apply filters on NaN values
    Args:
      df: pandas dataframe.
    Returns:
      Filtered Dataframe.
    Raises:
      This function shouldn't raise any Exception.
    """
    # remove "Size" row if value is null
    # set "EN" as langage if value is null
    # set 0.0 as price if value is null
    # set median as user_rating if value is null
    # replace nan counts with 1

    df = df[df["Size"].notnull()].copy()
    df["Languages"].fillna("EN", inplace=True)
    df["Price"].fillna(0.0, inplace=True)
    df["Average User Rating"].fillna(
            df["Average User Rating"].median(), inplace=True)
    df["User Rating Count"].fillna(1, inplace=True)
    df.drop_duplicates(subset="ID", inplace=True)
    return (df)


def string_filter(s: str):
    """Apply filters in order to clean the string.
    Args:
      s: string.
    Returns:
      Filtered String.
    Raises:
      This function shouldn't raise any Exception.
    """
    # filter : \\t, \\n, \\U1a1b2c3d4, \\u1a2b, \\x1a
    s = re.sub(r'\\+(t|n|U[a-z0-9]{8}|u[a-z0-9]{4}|x[a-z0-9]{2})', ' ', s)
    s = re.sub(r'[\\\""]+', '', s)
    s = re.sub(r' +', ' ', s)
    return (s)


def change_date_format(date: str):
    """Change date format from dd/mm/yy to yy-mm-dd
    Args:
      date: a string representing the date.
    Returns:
      The date in the format yy-mm-dd.
    Raises:
      This function shouldn't raise any Exception.
    """
    tmp = date.split('/')
    return (tmp[2]+"-"+tmp[1]+"-"+tmp[0])


def main():
    df = pd.read_csv("appstore_games.csv")

    # selecting columns
    df = (
        df[["ID", "Name", "Average User Rating",
            "User Rating Count", "Price", "Description",
            "Developer", "Age Rating", "Languages",
            "Size", "Primary Genre", "Genres",
            "Original Release Date", "Current Version Release Date"]]
    )
    # apply nan_filter
    df = df_nan_filter(df)

    # apply string_filter
    df["Name"] = df["Name"].apply(lambda x: string_filter(x))
    df["Description"] = df["Description"].apply(lambda x: string_filter(x))

    # apply change_date_format
    df["Original Release Date"] = (
            df["Original Release Date"].apply(lambda x: change_date_format(x))
    )
    df["Current Version Release Date"] = (
        df["Current Version Release Date"].apply(
            lambda x: change_date_format(x)
        )
    )

    # apply int conversion
    df["Age Rating"] = df["Age Rating"].apply(lambda x: int(x[:-1]))
    df['User Rating Count'] = (
        df['User Rating Count'].apply(lambda x: int(float(x)))
    )
    df['Size'] = df['Size'].apply(lambda x: int(float(x)))

    # saving file as csv
    df.to_csv("appstore_games.cleaned.csv", index=False)


if __name__ == "__main__":
    main()
