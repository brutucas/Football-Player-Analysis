import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")

focused_strikers_percentile = pd.read_csv('Resources/Focused Striker Percentile.csv')

radar_metrics = ['Contribution to Team Goals', 'Total Shots per 90 mins', 'SOT Accuracy', 'Successful Penalty Kicks',
                 'Number of Live Touches', 'Touches in Attacking Penalty Area', 'Times Tackled', 'Progressive Carry Distance', 
                 'Passes Successfully Received', 'Loose Balls Recovered', 'Aerial Duels Won']

def create_radar_chart(focused_strikers_percentile, player_name, radar_metrics):
    # Extract player data
    player_data = focused_strikers_percentile[focused_strikers_percentile['Player'] == player_name].iloc[0]

    r_values = player_data[radar_metrics].values.flatten().tolist()
    hover_text = [f"{metric}: {value}" for metric, value in zip(radar_metrics, r_values)]

    # Add a trace for the player's data
    fig = go.Figure(go.Scatterpolar(
        r=r_values,
        theta=radar_metrics,
        fill='toself',
        name=player_name,
        hoverinfo = 'text',
        hovertext = hover_text
    ))

    # Find the global minimum and maximum across all metrics to set a common axis range
    all_min = focused_strikers_percentile[radar_metrics].min()
    all_max = focused_strikers_percentile[radar_metrics].max()

    # Update the layout of the figure with a common polar args
    fig.update_layout(
        polar=dict(
            radialaxis=dict(range=[all_min, all_max], showticklabels=True, tickangle=45)
        ),
        title=f"Performance Chart - {player_name}"
    )

    return fig

st.write("### Select a player")

selected_player = st.selectbox('Player Name', focused_strikers_percentile['Player'].unique()[:-1])
focused_strikers_percentile = focused_strikers_percentile.iloc[:-2]

df_style = focused_strikers_percentile.style.apply(lambda row: ['background-color: yellow' 
                 if row['Player'] == selected_player 
                 else 'background-color: white'] * len(row), axis=1)
df_style = df_style.format("{:.1f}", subset=pd.IndexSlice[:, focused_strikers_percentile.select_dtypes(include=['number']).columns])

if st.button("Show Chart"):
    fig = create_radar_chart(focused_strikers_percentile, selected_player, radar_metrics)
    col1, col2 = st.columns(2)
    with col1: 
        st.image(f"Resources/{selected_player}.jpg", width = 400)
    with col2:
        st.write("### Striker Profile")
        st.write("This chart visualises the **percentile-modified** player performance, particularly his strengths and outlier abilities.")
        st.plotly_chart(fig)
    st.write("### Player Data")
    st.write("The following table shows the **percentile-modified data** for the selected player when compared to the other strikers in this selected group of outliers.")
    st.dataframe(df_style)



