import streamlit as st
import pandas as pd
import preprocessor,helpper

df = pd.read_csv("data/athlete_events.csv")
region_df = pd.read_csv("data/noc_regions.csv")

df = preprocessor.preprocess(df,region_df)

st.sidebar.title("Olympic")
user_menu = st.sidebar.radio(
    'Select an option',
    ('Medal Tally', 'Overal Analysis', 'Country-wise Analysis', 'Athlete wise Analysi')
)


if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years,country = helpper.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_country = st.sidebar.selectbox("Select Country", country)

    medal_tally = helpper.fetch_medal_tally(df,selected_year,selected_country)
    if selected_year == "Overall" and selected_country == "Overall":
        st.title("Overall Tally")
    if selected_year != "Overall" and selected_country == "Overall":
        st.title("Medal Tally in" + str(selected_year) + "Olympics")
    if selected_year == "Overall" and selected_country != 'Overall':
        st.title(selected_country + "overall performance")
    if selected_country != "Overall" and  selected_year != "Overall":
        st.title(selected_country + "performance in" + str(selected_year) + "Olympics")

    st.dataframe(medal_tally)
