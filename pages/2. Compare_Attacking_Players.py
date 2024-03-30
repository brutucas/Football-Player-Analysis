import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")

st.write('# Comparing Attacking Players in Selected Leagues')
st.write('\n')

col1, col2 = st.columns(2)

with col1:
    st.write('These graphs show the comparison of goals scored (including per 90 minutes) for the top attacking players in the selected leagues. The bottom graph shows this comparison of goals scored for those strikers and midfielders aged 23 and under.')
    st.image('Resources/Project Images/Graph Images/Total Goals for Top 30 Attacking Players.png')
    st.image('Resources/Project Images/Graph Images/Total Goals per 90 for Top 30 Attacking Players.png')
    st.image('Resources/Project Images/Graph Images/Total Goals and Goals per 90 for U23 Strikers.png')

with col2:
    st.write('The metric of goal contributions is a simple calculation of goals + assists. The top two graphs show goal contributions by the top attacking players, while the bottom graph visualises the goal contributions for those under-23 attacking players.')
    st.image('Resources/Project Images/Graph Images/Total Goal Contributions for Top 30 Attacking Players.png')
    st.image('Resources/Project Images/Graph Images/Top Goal Contributions per 90 for Top 30 Attacking Players.png')
    st.image('Resources/Project Images/Graph Images/Total Goal Contributions and Goal Contributions per 90 for U23 Strikers.png')