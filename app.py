import streamlit as st
import pandas as pd
import preprocessor,helpper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/athlete_events.csv")
region_df = pd.read_csv("data/noc_regions.csv")

df = preprocessor.preprocess(df,region_df)

st.sidebar.title("Olympic")
user_menu = st.sidebar.radio(
    'Select an option',
    ('Medal Tally', 'Overall Analysis', 'Country-wise Analysis', 'Athlete wise Analysi')
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

    st.table(medal_tally)

if user_menu == "Overall Analysis":
    editions = df['Year'].unique().shape[0]-1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]



    st.title("Top Statistics")
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    
    with col2:
        st.header("Hosts")
        st.title(cities)

    with col3:
        st.header("Sports")
        st.title(sports)


    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(events)
    
    with col2:
        st.header("Hosts")
        st.title(nations)

    with col3:
        st.header("Sports")
        st.title(athletes)

    nations_over_time = helpper.data_over_time(df,'region')
    fig = px.line(nations_over_time, x='Edition', y='region')
    st.title("Participating Nations Over the Years")
    st.plotly_chart(fig)

    nations_over_time = helpper.data_over_time(df,'Event')
    fig = px.line(nations_over_time, x='Edition', y='Event')
    st.title("Events Over the Years")
    st.plotly_chart(fig)

    nations_over_time = helpper.data_over_time(df,'Name')
    fig = px.line(nations_over_time, x='Edition', y='Name')
    st.title("Athelets Over the Years")
    st.plotly_chart(fig)

    st.title("No. of Events over time(Every Sport)")
    fig, ax = plt.subplots(figsize=(20,20))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    ax = sns.heatmap(x.pivot_table(index='Sport',columns='Year',values='Event',aggfunc='count').fillna(0).astype('int'),annot=True)
    st.pyplot(fig)

    st.title("Most Successful Athletes")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')

    selected_sport = st.selectbox('Select a Sport', sport_list)
    x = helpper.most_successful(df,selected_sport)
    st.table(x)


if user_menu == 'Country-wise Analysis':

    st.sidebar.title('Country-wise Analysis')


    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()

    selected_country = st.sidebar.selectbox('Select a Country', country_list)

    country_df = helpper.yearwise_medal_tally(df, selected_country)
    fig = px.line(country_df, x='Year', y='Medal')
    st.title(selected_country + " Medal Tally over the years")
    st.plotly_chart(fig)



    st.title(selected_country + " Excel in the following sports ")
    pt = helpper.country_event_heatmap(df, selected_country)
    if pt.empty:
        st.warning("No data available for the selected filters")
    else:
        fig, ax = plt.subplots(figsize=(20,20))
        ax = sns.heatmap(pt,annot=True)
        st.pyplot(fig)


    st.title("Top 10 athelets of " + selected_country)
    top10_df = helpper.most_successful_athelets(df,selected_country)
    st.table(top10_df)