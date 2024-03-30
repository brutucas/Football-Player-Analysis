import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")

st.write('# Finding Players in Data')

strikers_under_23 = pd.read_csv('Resources/Data Files/strikers_under_23.csv')

st.write('These visualisations conceal a significant volume of time spent finding, cleaning, and filtering data to both identify suitable players, but also better understand the direction of the project. To a certain extent, the data began to guide the direction of the project.')
st.write('Upon filtering for age and position, we ended up with roughly 1060 attacking players (Midfield and/or Forward), who had (at this mid-seasons point) played >= 13 matches. These graphs helped to visualise those outlier players, who were very efficiently assisting and scoring goals.')
st.write('For Shaolin.FC, once those outlier players had been identified in the interactive graphs, they could be considered (and further analysed) as potential candidates for the upcoming transfer market and an exciting new addition as goalscoring Number 9 for the club.')

fig = px.scatter(strikers_under_23, 
                   x='Minutes Played', 
                   y='Goals', 
                   hover_data=['Player'], 
                   title='Total Goals vs Minutes Played for U23 Strikers')

fig_1 = px.scatter(strikers_under_23, 
                   x='Minutes Played', 
                   y='Goals per 90', 
                   hover_data=['Player'], 
                   title='Goals (per 90) vs Minutes Played for U23 Strikers')

fig_2 = px.scatter(strikers_under_23, 
                 x='Minutes Played',
                 y='Goals + Assists', 
                 hover_data=['Player'], 
                 title='Total Goal Contributions vs Minutes Played for U23 Strikers')

fig_3 = px.scatter(strikers_under_23, 
                 x='Minutes Played', 
                 y='Goals + Assists per 90', 
                 hover_data=['Player'], 
                 title='Goal Contributions (per 90) vs Minutes Played for U23 Strikers')

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig)
    st.plotly_chart(fig_1)

with col2:
    st.plotly_chart(fig_2)
    st.plotly_chart(fig_3)