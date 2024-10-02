import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')


# Load cleaned data
all_df = pd.read_csv("./dashboard/main-data-df.csv")

# Menyesuaikan tipe data datetime
all_df['datetime'] = pd.to_datetime(all_df['datetime'])
all_df.set_index('datetime', inplace=True)

# Filter data berdasarkan rentang waktu
min_date = all_df.index.min()
max_date = all_df.index.max()

with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    start_date, end_date = st.date_input(
        label='Rentang Waktu', min_value=min_date, max_value=max_date,
        value=[min_date, max_date]
    )

main_df = all_df.loc[start_date:end_date]

# Visualisasi total order dan pendapatan
st.header('Bike Sharing Analysis:')
st.text('Hello! Welcome to the Bike Sharing Analysis Dashboard, where we explore bike rental trends and customer behavior.')

st.subheader('Total Bike Rentals by Season')

season_rent_df = all_df.groupby("season").total_count.sum().sort_values(ascending=False).reset_index()
season_rename = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
season_rent_df['season'] = season_rent_df['season'].replace(season_rename)

fig, ax = plt.subplots(figsize=(8, 6))

ax.bar(season_rent_df['season'], season_rent_df['total_count'], color='skyblue')

ax.set_title('Total Bike Rentals by Season', fontsize=16)
ax.set_xlabel('season', fontsize=12)
ax.set_ylabel('total_count', fontsize=12)

st.pyplot(fig)

st.subheader('Comparison of Total Bike Rentals between 2011 and 2012')
year_rent_df = all_df.groupby("year")['total_count'].sum().reset_index()
year_rename = {0: '2011', 1: '2012'}
year_rent_df['year'] = year_rent_df['year'].replace(year_rename)

fig, ax = plt.subplots(figsize=(8, 6))

ax.bar(year_rent_df['year'], year_rent_df['total_count'], color=['lightblue', 'orange'])

ax.set_title('Comparison of Total Bike Rentals between 2011 and 2012', fontsize=16)
ax.set_xlabel('year', fontsize=12)
ax.set_ylabel('total_count', fontsize=12)

st.pyplot(fig)

st.text('This dashboard explores various factors affecting bike-sharing usage, including weather conditions.')
st.subheader('Number of Users by Weather Condition')

weater_rent_df = all_df.groupby("weater_condition")['total_count'].sum().reset_index()
weater_rename = {1 :'clear', 2 : 'cloudy', 3 : 'Thunderstorm', 4 : 'Heavy Rain'}
weater_rent_df['weater_condition'] = weater_rent_df['weater_condition'].replace(weater_rename)
fig, ax = plt.subplots(figsize=(50,25))

ax.bar(all_df["weater_condition"], all_df["total_count"], color="pink")
ax.set_title("Number of Customer by Weather", loc="center", fontsize=100)
ax.set_ylabel("Customer",fontsize=100)
ax.set_xlabel("Weather",fontsize=100)
ax.tick_params(axis='x', labelsize=80)
ax.tick_params(axis='y', labelsize=80)
st.pyplot(fig)
