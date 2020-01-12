#######################
#   Ex02: Normalize   #
#######################

import pandas as pd

def explode_format(x):
    t = []
    for e in x.split(','):
        t.append(e.strip())
    return(t)

def nf1_normalization(df):
    l_df = df[["ID","Languages"]].copy()
    l_df["Languages"] = l_df["Languages"].apply(lambda x: explode_format(x))
    l_df = l_df.explode('Languages')
    l_df = l_df.reset_index(drop=True)

    g_df = df[["ID", "Primary Genre", "Genres"]].copy()
    g_df["Genres"] = g_df["Genres"].apply(lambda x: explode_format(x))
    g_df = g_df.explode('Genres')
    g_df = g_df.reset_index(drop=True)
    return(l_df, g_df)

df = pd.read_csv("../ex01/appstore_games.cleaned.csv")
l_df, g_df = nf1_normalization(df)
l_df.to_csv("appstore_games_languages.normalized.csv", index=False)
g_df.to_csv("appstore_games_genres.normalized.csv", index=False)

df = df.drop(['Languages', 'Primary Genre', 'Genres'], axis=1)
df.to_csv("appstore_games.normalized.csv", index=False)
