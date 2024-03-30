import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")

percentile_data = pd.read_excel('Resources/Updated Focus Player Data.xlsx')
focused_strikers_percentile = pd.read_excel('Resources/Updated Focus Player Data.xlsx', sheet_name='Percentile')

coeff_data = pd.read_excel('Resources/Updated Focus Player Data.xlsx', sheet_name='Coefficient', header=0)
focused_strikers_coeff = coeff_data.iloc[0:9, 0:21]
focused_strikers_coeff['Age'] = focused_strikers_coeff['Age'].astype('Int64')

percentile_columns = [
    'Contribution to Team Goals',
    'Total Shots per 90 mins',
    'SOT per 90 mins',
    'SOT Accuracy',
    'Goals per SOT',
    'Successful Penalty Kicks',
    'SCA per 90 mins',
    'SCA Live-Ball Passes',
    'SCA Take-ons',
    'Number of Live Touches',
    'Touches in Attacking 3rd',
    'Touches in Attacking Penalty Area',
    'Attempted Take-ons',
    'Times Tackled',
    'Progressive Carry Distance',
    'Passes Successfully Received',
    'Interceptions',
    'Loose Balls Recovered',
    'Aerial Duels Won'
]

def create_radar_overlay(focused_strikers_percentile, focused_strikers_coeff, player_name, percentile_columns):
    # Extract player data from both DataFrames
    player_percentile_data = focused_strikers_percentile[focused_strikers_percentile['Player'] == player_name].iloc[0]
    player_coeff_data = focused_strikers_coeff[focused_strikers_coeff['Player'] == player_name].iloc[0]

    # Extract values for the radar chart
    r_values_percentile = player_percentile_data[percentile_columns].values.flatten().tolist()
    r_values_coeff = player_coeff_data[percentile_columns].values.flatten().tolist()

    # Generate hover text for both sets of values
    hover_text_percentile = [f"Percentile {metric}: {value}" for metric, value in zip(percentile_columns, r_values_percentile)]
    hover_text_coeff = [f"Coeff {metric}: {value}" for metric, value in zip(percentile_columns, r_values_coeff)]

    # Create the radar chart
    fig = go.Figure()

    # Add a trace for the player's percentile data
    fig.add_trace(go.Scatterpolar(
        r=r_values_percentile,
        theta=percentile_columns,
        fill='toself',
        name="Outlier Percentile",
        hoverinfo='text',
        hovertext=hover_text_percentile,
        opacity=0.5  # Adjust opacity to make the trace more transparent
    ))

    # Add a trace for the player's coefficient data with reduced opacity
    fig.add_trace(go.Scatterpolar(
        r=r_values_coeff,
        theta=percentile_columns,
        fill='toself',
        name="League Adjustment",
        hoverinfo='text',
        hovertext=hover_text_coeff,
        line_color='red'
    ))

    # Set the radial axis range based on the percentile data only
    percentile_min = focused_strikers_percentile[percentile_columns].min()
    percentile_max = focused_strikers_percentile[percentile_columns].max()

    # Update the layout of the figure with a common polar args
    fig.update_layout(
    polar=dict(
        radialaxis=dict(
            range=[percentile_min, percentile_max],
            showticklabels=True,  # Shows tick labels
            tickfont=dict(size=10)  # Adjusts radial axis tick label font size
        )
    ),
    title={
        'text': f"Striker Metrics with League Adjustment - {player_name}",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
    },
    title_font_size=20,
    width=1000,  # Increase figure width
    height=600,  # Increase figure height
    autosize=False,
    margin=dict(t=100)
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
    fig = create_radar_overlay(focused_strikers_percentile, focused_strikers_coeff, selected_player, percentile_columns)
    col1, col2 = st.columns(2)
    with col1: 
        st.write(f"### {selected_player}")
        st.image(f"Resources/{selected_player}.jpg", width = 400)
    with col2:
        st.write("### Striker Profile")
        st.write("This chart visualises the **percentile-modified** player performance, particularly his strengths and outlier abilities.")
        st.plotly_chart(fig)
    st.write("### Player Data")
    st.write("The following table shows the **percentile-modified data** for the selected player when compared to the other strikers in this selected group of outliers.")
    st.dataframe(df_style)