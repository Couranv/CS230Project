"""
Name: Anton Spiridonov
CS230: Section 005
Data: Nuclear Explosions
URL: FILL IN LINK

Description:
Create a web page to present data and allow the user to make conclusions off the graphs they see.
There are 4 pages, each one has its own visual to show and provides its own information.

"""


import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

df = pd.read_csv("nuclear_explosions.csv")
df.columns = df.columns.str.replace('Data.', '')
df.columns = df.columns.str.replace('Date.', '')
df.columns = df.columns.str.replace('Location.Cordinates.', '')

# [DA7]
df = df.drop('Purpose', axis=1)
# [DA9]
df['Yeild.Average'] = df[['Yeild.Lower', 'Yeild.Upper']].mean(axis=1)
df.columns = df.columns.str.capitalize()

countries = df['Weapon source country'].unique()
country_counts = df['Weapon source country'].value_counts()

st.title("CS 230 Project For Nuclear Bombs")
# [ST3]
countrySelect = st.multiselect("Select which countries you would like to see", options=list(countries), default=list(countries))

filteredCountry = country_counts[countrySelect]

plt.figure(figsize=(10, 6))
# [VIZ3]
plt.pie(filteredCountry, autopct='%1.1f%%')
plt.title("Percentage Of Total Nuclear Bombs Dropped")
plt.axis('equal')
plt.legend(labels=filteredCountry.index, loc='upper left')

st.pyplot()

st.dataframe(filteredCountry)
