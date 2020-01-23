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
    df = df[df["Size"].notnull()].copy()              # remove "Size" row if size is null
    df["Languages"].fillna("EN", inplace=True)        # set "EN" as langage if value is null
    df["Price"].fillna(0.0, inplace=True)             # set 0.0 as price if value is null
    df["Average User Rating"].fillna(
    df["Average User Rating"].median(), inplace=True) # set median as user_rating if value is null
    df["User Rating Count"].fillna(1, inplace=True)   #replace nan counts with 1
    df.drop_duplicates(subset ="ID",inplace = True)
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
    if len(tmp) < 3:
        print(tmp)
    return (tmp[2]+"-"+tmp[1]+"-"+tmp[0])
    
df = pd.read_csv("appstore_games.csv")

df = df[["ID", "Name", "Average User Rating",
          "User Rating Count", "Price", "Description",
          "Developer", "Age Rating", "Languages",
          "Size", "Primary Genre", "Genres",
          "Original Release Date", "Current Version Release Date"]]

df = df_nan_filter(df)

df["Description"] = df["Description"].apply(lambda x: string_filter(x))

df["Original Release Date"] = df["Original Release Date"].apply(lambda x: change_date_format(x))
df["Current Version Release Date"] = df["Current Version Release Date"].apply(lambda x: change_date_format(x))
df["Age Rating"] = df["Age Rating"].apply(lambda x: int(x[:-1]))
df['User Rating Count'] = df['User Rating Count'].apply(lambda x: int(float(x)))
df['Size'] = df['Size'].apply(lambda x: int(float(x)))

df.to_csv("appstore_games.cleaned.csv", index=False)
