import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")

st.write('# Identifying the U23 Strikers of Interest')

st.write('This dataframe screenshot shows my selection of attacking players, which is based on the extensive data visualisation and analysis I have done so far. I chose these players due to their outlier performance across goals AND goal contributions (both total and per 90), as well as minutes played for some measure of consistent performance.')

st.image('Resources/Project Images/Screenshot Evidence/U23 Strikers of Interest.png')

st.write('But our work here is not yet finished! We have cleaned, screened, and visualised the data to find those outlier strikers among 3000+ players. The challenge is now to identify the outliers in this data of already outlier strikers across the selected leagues. I have selected a larger pool of players to also factor in higher transfer values that might remove an otherwise ideal player later in the data-scouting process.')

st.image('Resources/Project Images/Graph Images/% Contribution to Team Goals for U23 Strikers of Interest.png')

st.write('This is arguably one of the most important data visualisations in the entire project. It clearly shows the disproportionately important role of each player in the list, and would certainly raise questions for the in-person scouting and video footage later in the process. Do some strikers share the attacking responsibility, or do they roam as lone operators ahead of their team? Do some of these leagues have extra-weak defences?')

st.image('Resources/Project Images/Graph Images/Shot-Creating Actions (SCA) vs Goal-Creating Actions (GCA) per 90 for U23 Strikers of Interest.png')

st.write('This is one visualisation (among **many** others) that helped to identify the outliers among the outliers. In this example, I was able to find those players, who are creating a higher number of SCAs each game, or converting a higher percentage of fewer GCAs. It offered additional information, which (when taken as a whole) would inform the next step of the scouting process, as well as decisions about specific players to be pursued in the transfer market.')
