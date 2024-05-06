"""
Name: Anton Spiridonov
CS230: Section 005
Data: Nuclear Explosions
URL: FILL IN LINK
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

# [PY1]
def bombsPerDecade(df, country='USA'):
    # [DA4]
    country_df = df[df['Weapon source country'] == country]
    yearsOfCountry = country_df['Year']

    # I had to search up how to iterate over a list of years so that I can get the decade (StackOverflow)
    # [PY4], [PY5], [DA5]
    bombs_per_decade = {
        i: len(country_df[(yearsOfCountry >= i) & (yearsOfCountry < i + 10)])
        for i in range(yearsOfCountry.min() // 10 * 10, yearsOfCountry.max() // 10 * 10 + 10, 10)
    }
    return bombs_per_decade

st.title("Nuclear Explosions Analysis")

# [ST2]
select_country = st.selectbox("Please select a country.", countries)

bombsDecade = bombsPerDecade(df, select_country)
decades_df = pd.DataFrame(list(bombsDecade.items()), columns=["Decade", "numBombs"])

# [VIZ1]
decades_df.plot(x="Decade", y="numBombs", kind="bar", legend=False)
plt.xlabel("Decade")
plt.ylabel("Number Of Bombs")
plt.title(f"Number Of Bombs Per Decade For {select_country}")
st.pyplot()
