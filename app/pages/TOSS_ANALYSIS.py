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

# def team_decision_after_toss_win_and_match_win(year,team):
#     with st.container(border=True):
#         batted_win =0
#         fielded_win =0
#         batted = toss_data_grouped.get_group(year).groupby("toss_winner").get_group(team).value_counts("toss_decision")["bat"]
#         fielded = toss_data_grouped.get_group(year).groupby("toss_winner").get_group(team).value_counts("toss_decision")["field"]
#         if (toss_data_grouped.get_group(year).groupby("toss_winner").get_group(team).groupby("toss_decision").get_group("bat").value_counts("winner")[team] > 0):
#             batted_win = toss_data_grouped.get_group(year).groupby("toss_winner").get_group(team).groupby("toss_decision").get_group("bat").value_counts("winner")[team]

#         st.write(batted_win)
#         if (toss_data_grouped.get_group(year).groupby("toss_winner").get_group(team).groupby("toss_decision").get_group("bat").value_counts("winner")[team] > 0):
#             fielded_win = toss_data_grouped.get_group(year).groupby("toss_winner").get_group(team).groupby("toss_decision").get_group("field").value_counts("winner")[team]
#         st.write(fielded_win)

#         with st.container(border =True):
#             col1,col2=st.columns([2,2])
#             with col1:
#                 #put pie chart here
#             with col2:
#                 #put pie chart here
#         # print("The team {} in {} won and took batting {} times and won the game {} times so the percentages are {}".format(team,year,batted,batted_win,((batted_win/batted)*100)))
#         # print("The team {} in {} won and took fielding {} times and won the game {} times so the percentages are {}".format(team,year,fielded,fielded_win,((fielded_win/fielded)*100)))


import plotly.graph_objects as go
import streamlit as st

def team_decision_after_toss_win_and_match_win(year, team):
    with st.container(border=True):
        st.write(f"**{team}'s Toss Win and Match Win Analysis for {year}**")
        
        # Initialize win counts
        batted_win = 0
        fielded_win = 0
        
        # Retrieve counts for batting and fielding toss decisions
        toss_winner_data = toss_data_grouped.get_group(year).groupby("toss_winner").get_group(team)
        batted = toss_winner_data.value_counts("toss_decision").get("bat", 0)
        fielded = toss_winner_data.value_counts("toss_decision").get("field", 0)

        # Calculate the number of wins after choosing to bat or field
        if batted > 0 and toss_winner_data.groupby("toss_decision").get_group("bat").value_counts("winner").get(team, 0) > 0:
            batted_win = toss_winner_data.groupby("toss_decision").get_group("bat").value_counts("winner").get(team, 0)
        
        if fielded > 0 and toss_winner_data.groupby("toss_decision").get_group("field").value_counts("winner").get(team, 0) > 0:
            fielded_win = toss_winner_data.groupby("toss_decision").get_group("field").value_counts("winner").get(team, 0)

        # Display win counts
        st.write(f"**Batting Wins**: {batted_win}")
        st.write(f"**Fielding Wins**: {fielded_win}")
        
        # Create pie chart data for batted and fielded wins
        with st.container(border=True):
            col1, col2 = st.columns([2, 2])
            with col1:
                # Pie chart for batting decision
                labels = ['Wins After Batting', 'Lost After Batting']
                values = [batted_win, batted -batted_win]
                
                fig1 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.4, marker_colors=['#FF4B4B', '#262730'])])
                fig1.update_layout(
                    title_text='',
                    annotations=[dict(text='Batting', x=0.5, y=0.5, font_size=12, showarrow=False)],
                    showlegend=False,
                    template='plotly_white',
                    margin=dict(t=0, b=0, l=0, r=0),
                    height=200, width=200  # Set chart size
                )
                st.plotly_chart(fig1, use_container_width=False, config={'displayModeBar': False})

            with col2:
                # Pie chart for fielding decision
                labels = ['Wins After Fielding', 'Lost After Fielding']
                values = [fielded_win,fielded -fielded_win]
                
                fig2 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.4, marker_colors=['#FF4B4B', '#262730'])])
                fig2.update_layout(
                    title_text='',
                    annotations=[dict(text='Fielding', x=0.5, y=0.5, font_size=12, showarrow=False)],
                    showlegend=False,
                    template='plotly_white',
                    margin=dict(t=0, b=0, l=0, r=0),
                    height=200, width=200  # Set chart size
                )
                st.plotly_chart(fig2, use_container_width=False, config={'displayModeBar': False})

# Example usage
# team_decision_after_toss_win_and_match_win(2021, 'India')


# Example usage
# team_decision_after_toss_win_and_match_win(2021, 'India')



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


    