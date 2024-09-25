#imports
import numpy as np
import pandas as pd
import warnings
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
warnings.simplefilter(action='ignore', category=FutureWarning)

# Load the data
data = pd.read_csv("../data/processed/clean_data.csv")
toss_data = data.iloc[:, [1, 2, 3, 6, 7, 8, 9, 10, 11]]
toss_data_grouped = toss_data.groupby("season")



def team_win_percentage(year,team):
    with st.container(border=True):
        a = toss_data_grouped.get_group(year).iloc[:,4].value_counts()[team]
        b = toss_data_grouped.get_group(year).iloc[:,5].value_counts()[team]
        c = a+b
        d = toss_data_grouped.get_group(year).iloc[:,-3].value_counts()[team]
        toss_win_percentage = round((d/c)*100,2)
        st.write(f"**Toss Win Percentage : {toss_win_percentage}%**")

def team_match_win_rate_after_toss_win(year,team):
    with st.container(border=True):
        a = toss_data_grouped.get_group(year).groupby("toss_winner").get_group(team).value_counts("winner")[team]
        b = toss_data_grouped.get_group(year).iloc[:,-3].value_counts()[team]
        st.write("**Won {} Tosses Out Of Which Won {} Matches**".format(b,a)) 
        
def team_decision_after_toss_win(year, team):
    with st.container(border=True):
        st.write("**Decision After Toss Win**")
        
        values = []
        # Retrieve data
        toss_winner_data = toss_data_grouped.get_group(year).groupby("toss_winner").get_group(team)
        a = toss_winner_data.value_counts("toss_decision").get("bat", 0)
        b = toss_winner_data.value_counts("toss_decision").get("field", 0)
        c = toss_data_grouped.get_group(year).iloc[:, -3].value_counts().get(team, 0)

        # Calculate percentages
        batting_percentage = (a / c * 100) if c > 0 else 0
        bowling_percentage = (b / c * 100) if c > 0 else 0
        
        # Prepare data for plotting
        labels = ['Batting', 'Bowling']
        values.append(batting_percentage)
        values.append(bowling_percentage)

        # Create the bar chart
        fig = go.Figure(data=[
            go.Bar(name='Decision', x=labels, y=values, marker_color=['blue', 'orange'])
        ])

        fig.update_layout(
            xaxis_title='Decision',
            yaxis_title='Percentage (%)',
            yaxis=dict(range=[0, 100]),  # Set y-axis range from 0 to 100
            margin=dict(t=10, b=30, l=30, r=30),  # Adjust margins here
            template='plotly_white'
        )
        fig.update_layout(dragmode=False)
        st.plotly_chart(fig, config={'displayModeBar': False})

def team_decision_after_toss_win_and_match_win(year,team):
    with st.container(border=True):
        batted_win =0
        fielded_win =0
        batted = toss_data_grouped.get_group(year).groupby("toss_winner").get_group(team).value_counts("toss_decision")["bat"]
        fielded = toss_data_grouped.get_group(year).groupby("toss_winner").get_group(team).value_counts("toss_decision")["field"]
        if (toss_data_grouped.get_group(year).groupby("toss_winner").get_group(team).groupby("toss_decision").get_group("bat").value_counts("winner")[team] > 0):
            batted_win = toss_data_grouped.get_group(year).groupby("toss_winner").get_group(team).groupby("toss_decision").get_group("bat").value_counts("winner")[team]

        st.write(batted_win)
        if (toss_data_grouped.get_group(year).groupby("toss_winner").get_group(team).groupby("toss_decision").get_group("bat").value_counts("winner")[team] > 0):
            fielded_win = toss_data_grouped.get_group(year).groupby("toss_winner").get_group(team).groupby("toss_decision").get_group("feild").value_counts("winner")[team]
        st.write(fielded_win)
        print("The team {} in {} won and took batting {} times and won the game {} times so the percentages are {}".format(team,year,batted,batted_win,((batted_win/batted)*100)))
        print("The team {} in {} won and took fielding {} times and won the game {} times so the percentages are {}".format(team,year,fielded,fielded_win,((fielded_win/fielded)*100)))



#input figuring 
with st.container(border = True):
    col1, col2 = st.columns([2,2])
    with col1:
        years = toss_data["season"].unique()
        selected_year = st.selectbox("Select a year", years)
    with col2:
        teams = toss_data_grouped.get_group(selected_year)
        team1 = teams["team1"].unique()
        team2 = teams["team2"].unique()
        team3 = np.unique(np.concatenate((team1, team2)))
        selected_team = st.selectbox("Select a team", team3)
    if st.button("Submit"):
        st.write("---")
        with st.container(border=None):
            column1,column2,column3 = st.columns([1,1,1])
            with column1:
                team_win_percentage(selected_year,selected_team)
                team_decision_after_toss_win(selected_year,selected_team)
                
            with column2:
                team_match_win_rate_after_toss_win(selected_year,selected_team)
                team_decision_after_toss_win_and_match_win(selected_year,selected_team)
            with column3:
                st.write("column3")


    