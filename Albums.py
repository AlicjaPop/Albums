# -*- coding: utf-8 -*-
"""Albums.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AjHkiM72NrDXHLoW6UNqLwcOCY5ZoJ1E
"""

import numpy as np
import pandas as pd

data = pd.read_html('https://www.officialcharts.com/chart-news/the-best-selling-albums-of-all-time-on-the-official-uk-chart__15551/', header=0)

df=data[0]

"""Zad 1"""

renamed_df=df.rename(columns={"HIGH POSN":"MAX POZ", "TITLE":"TYTUŁ", "ARTIST":"ARTYSTA", "YEAR":"ROK"})
renamed_df

"""Zad 2"""

renamed_df["ARTYSTA"].nunique()

"""Na liście jest 47 artystów

Zad 3
"""

renamed_df["ARTYSTA"].value_counts()

"""Na liście najczęściej pojawiają się Coldplay i Take That

Zad 4
"""

formatted_df=renamed_df.rename(str.capitalize, axis="columns")
formatted_df

"""Zad 5"""

df_2=formatted_df.drop("Max poz", axis=1)
df_2

"""Zad 6"""

albums_per_year=df_2.groupby(pd.Grouper(key="Rok")).agg({"Artysta":"count"})
albums_per_year

albums_per_year.sort_values(by="Artysta", ascending=False)

"""Najwięcej albumów wyszło w latach 1987 oraz 2000

Zad 8
"""

albums_per_year.sort_index()

"""Najmłodszy album na liście został wydany w 2015 roku

Zadanie 7
"""

df_filtered = df_2[(df_2['Rok'] >= 1960) & (df_2['Rok'] <= 1990)]
df_filtered.count()

"""Na liście znajdują się 22 albumy wydane między 1960 a 1990 rokiem włącznie

Zad 9
"""

table_to_export=(formatted_df.sort_values(by="Rok", ascending=False)).drop_duplicates(subset="Artysta")

"""Zad 10"""

table_to_export.to_csv("C:/Users/user/OneDrive/Desktop/Kodilla/Albums/Exported_list.csv", index=False)