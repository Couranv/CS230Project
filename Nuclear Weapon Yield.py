"""
Name: Anton Spiridonov
CS230: Section 005
Data: Nuclear Explosions
URL: FILL IN LINK
"""

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv("nuclear_explosions.csv")

# [PY2]
def minMaxYear(df):
    min_year = int(df['Year'].min())
    max_year = int(df['Year'].max())
    return min_year, max_year

# [DA1]
df.columns = df.columns.str.replace('Data.', '')
df.columns = df.columns.str.replace('Date.', '')
df.columns = df.columns.str.replace('Location.Cordinates.', '')

# [DA7]
df = df.drop('Purpose', axis=1)
# [DA9]
df['Yeild.Average'] = df[['Yeild.Lower', 'Yeild.Upper']].mean(axis=1)
df.columns = df.columns.str.capitalize()

st.title("Nuclear Explosions Analysis")
# [DA3]
minYear, maxYear = minMaxYear(df)

# [ST1]
year_range = st.slider('Select a range of years', minYear, maxYear, (minYear, maxYear))

# [DA5]
df_Year = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]

grouped_df = df_Year.groupby(['Year', 'Weapon source country'])['Yeild.average'].mean().unstack()

# [VIZ2]
grouped_df.plot(kind='bar', stacked=True)
plt.xlabel('Year')
plt.ylabel('Average Yield')
plt.title('Average Yield by Country and Year')
# Module not covered in class (how to edit the tick marks) -- I found it on GeeksForGeeks
plt.xticks(ticks=range(0, len(grouped_df.index), 5), labels=grouped_df.index[::5])

st.pyplot()