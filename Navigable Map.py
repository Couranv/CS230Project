"""
Name: Anton Spiridonov
CS230: Section 005
Data: Nuclear Explosions
URL: FILL IN LINK

"""

import pandas as pd
import streamlit as st
import pydeck as pdk

df = pd.read_csv("nuclear_explosions.csv")


def minMaxYear(df):
    min_year = int(df['Year'].min())
    max_year = int(df['Year'].max())
    return min_year, max_year


df.columns = df.columns.str.replace('Data.', '')
df.columns = df.columns.str.replace('Date.', '')
df.columns = df.columns.str.replace('Location.Cordinates.', '')
# [DA7]
df = df.drop('Purpose', axis=1)
df.columns = df.columns.str.capitalize()

countries = df['Weapon source country'].unique()

st.title("A Visual Of Nuclear Explosion Locations")
select_country = st.selectbox("Please select a country", countries)

minYear, maxYear = minMaxYear(df)

# [ST1]
year_range = st.slider('Select a range of years', minYear, maxYear, (minYear, maxYear))

df_Year = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]

country_df = df_Year[df_Year['Weapon source country'] == select_country]

ICON_URL = "https://upload.wikimedia.org/wikipedia/commons/d/d9/Gartoon_apps_clanbomber_replaced.svg"
icon_data = {
    "url": ICON_URL,
    "width": 100,
    "height": 100,
    "anchorY": 1
}

country_df["icon_data"] = None
for i in country_df.index:
    country_df.at[i, "icon_data"] = icon_data

icon_layer = pdk.Layer(
    type="IconLayer",
    data=country_df,
    get_icon="icon_data",
    get_position="[Longitude, Latitude]",
    get_size=20,
    pickable=True
)

view_state = pdk.ViewState(
    latitude=country_df['Latitude'].mean(),
    longitude=country_df['Longitude'].mean(),
    zoom=3
)

tooltip = {
    "html": "<b>Name:</b> {Name}<br/><b>Weapon deployment location:</b> {Weapon deployment location}<br/><b>Year:</b> {Year}",
    "style": {"backgroundColor": "steelblue", "color": "white"}
}

icon_map = pdk.Deck(
    map_style='mapbox://styles/mapbox/navigation-day-v1',
    layers=[icon_layer],
    initial_view_state=view_state,
    tooltip=tooltip
)

# [VIZ1]
st.pydeck_chart(icon_map)