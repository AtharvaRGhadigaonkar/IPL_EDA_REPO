import numpy as np
import pandas as pd
import warnings
import streamlit as st
warnings.simplefilter(action='ignore', category=FutureWarning)

# Load the data
data = pd.read_csv("../data/processed/clean_data.csv")
toss_data = data.iloc[:, [1, 2, 3, 6, 7, 8, 9, 10, 11]]
toss_data_grouped = toss_data.groupby("season")




def team_toss_percentage(year,team):
    #(no of toss won)/(total no of matches played)
    returnlist=[]
    a = toss_data_grouped.get_group(year).iloc[:,4].value_counts()[team]
    b = toss_data_grouped.get_group(year).iloc[:,5].value_counts()[team]
    c = a+b
    d = toss_data_grouped.get_group(year).iloc[:,-3].value_counts()[team]
    returnlist.append(c)
    returnlist.append(d)
    returnlist.append((d/c)*100)
    # return (returnlist)
    with st.container(border=True):
	    col1, col2 = st.columns([2,2])  # Create two columns with a visible divider

	    with col1:
	        # Display the team logo and selected team
	        st.image("pages/images/CSK_logo2.png",width = 500) # Replace with actual logo path
	        
	    with col2:
	        # Display number of games played, won, and winning percentage
	        st.subheader(f"Team Statistics {selected_year}")
	        # st.write(f"Year: {selected_year}")
	        st.write(f"Games Played: {returnlist[0]}")
	        st.write(f"Games Won: {returnlist[1]}")
	        st.write(f"Winning Percentage: {returnlist[2]:.2f}%")


with st.container(border=True):
    st.header("Team Toss By Year")
    # Unique years for selection
    years = toss_data["season"].unique()
    selected_year = st.selectbox("Select a year", years)

    # Get teams for the selected year
    teams = toss_data_grouped.get_group(selected_year)
    team1 = teams["team1"].unique()
    team2 = teams["team2"].unique()
    team3 = np.unique(np.concatenate((team1, team2)))
    selected_team = st.selectbox("Select a team", team3)
    if st.button("Submit"):
    	a = team_toss_percentage(selected_year,selected_team)







def team_match_win_rate_after_toss_win(year,team):
    a = toss_data_grouped.get_group(year).groupby("toss_winner").get_group(team).value_counts("winner")[team]
    b = toss_data_grouped.get_group(year).iloc[:,-3].value_counts()[team]
    return("In {}, {} won {} toss out of which they won {} matches".format(year,team,b,a))

team_match_win_rate_after_toss_win("2009","CSK")

with st.container(border=True):
    st.header("Team Match Win Percentage After Toss Win")
    # Unique years for selection
    years = toss_data["season"].unique()
    selected_year = st.selectbox("Select a year pls", years)

    # Get teams for the selected year
    teams = toss_data_grouped.get_group(selected_year)
    team1 = teams["team1"].unique()
    team2 = teams["team2"].unique()
    team3 = np.unique(np.concatenate((team1, team2)))
    selected_team1 = st.selectbox("Select a team pls", team3)
    if st.button("Submit1"):
    	a = team_match_win_rate_after_toss_win(selected_year,selected_team1)
    	st.write(a)


def team_decision_after_toss_win(year,team):
    a = toss_data_grouped.get_group(year).groupby("toss_winner").get_group(team).value_counts("toss_decision")["bat"]
    b = toss_data_grouped.get_group(year).groupby("toss_winner").get_group(team).value_counts("toss_decision")["field"]
    c = toss_data_grouped.get_group(year).iloc[:,-3].value_counts()[team]
    return ("Team {} won {} times in {} and choose batting: {} percent and bowling :{} percent times".format(team,c,year,((a/c)*100),((b/c)*100)))
    # print((b/c)*100)


with st.container(border=True):
    st.header("Team Decision After Toss Won")
    # Unique years for selection
    years = toss_data["season"].unique()
    selected_year = st.selectbox("Select a year pls 1", years)

    # Get teams for the selected year
    teams = toss_data_grouped.get_group(selected_year)
    team1 = teams["team1"].unique()
    team2 = teams["team2"].unique()
    team3 = np.unique(np.concatenate((team1, team2)))
    selected_team1 = st.selectbox("Select a team pls 1", team3)
    if st.button("Submit pls 1"):
    	a = team_decision_after_toss_win(selected_year,selected_team1)
    	st.write(a)



def after_decision_win_percentage(year,team):
    batted = toss_data_grouped.get_group(year).groupby("toss_winner").get_group(team).value_counts("toss_decision")["bat"]
    fielded = toss_data_grouped.get_group(year).groupby("toss_winner").get_group(team).value_counts("toss_decision")["field"]
    batted_win = toss_data_grouped.get_group(year).groupby("toss_winner").get_group(team).groupby("toss_decision").get_group("bat").value_counts("winner")[team]
    fielded_win = toss_data_grouped.get_group(year).groupby("toss_winner").get_group(team).groupby("toss_decision").get_group("field").value_counts("winner")[team]
    list1 = ["The team {} in {} won and took batting {} times and won the game {} times so the percentages are {}".format(team,year,batted,batted_win,((batted_win/batted)*100)),"The team {} in {} won and took fielding {} times and won the game {} times so the percentages are {}".format(team,year,fielded,fielded_win,((fielded_win/fielded)*100))]
    return (list1)



with st.container(border=True):
    st.header("After decision win percentage")
    # Unique years for selection
    years = toss_data["season"].unique()
    selected_year = st.selectbox("Select a year pls 2", years)

    # Get teams for the selected year
    teams = toss_data_grouped.get_group(selected_year)
    team1 = teams["team1"].unique()
    team2 = teams["team2"].unique()
    team3 = np.unique(np.concatenate((team1, team2)))
    selected_team1 = st.selectbox("Select a team pls 2", team3)
    if st.button("Submit pls 2"):
    	a = after_decision_win_percentage(selected_year,selected_team1)
    	st.write(a[0])
    	st.write(a[1])







import seaborn as sns
from matplotlib import pyplot as plt

import matplotlib.pyplot as plt

import plotly.express as px
import streamlit as st

import plotly.graph_objects as go
import streamlit as st

import plotly.graph_objects as go
import streamlit as st

def team_toss_win_at_venues_interactive(year, team):
    # Get the data for the given year and team
    a = toss_data_grouped.get_group(year).groupby("toss_winner").get_group(team).value_counts("venue").reset_index()

    # Create a simple, clean bar chart using Plotly Graph Objects
    fig = go.Figure(data=[
        go.Bar(x=a['venue'], y=a['count'], marker_color='#FF4B4B')  # Primary color for bars
    ])
    
    # Set custom dark background and layout
    fig.update_layout(
        title=f'Team Toss Wins at Venues for {team} in {year}',
        xaxis_title='Venue',
        yaxis_title='Number of Toss Wins',
        plot_bgcolor='#0E1117',    # Background color
        paper_bgcolor='#0E1117',   # Outer background color
        font=dict(color='#FAFAFA'),  # Text color
        title_font_size=24,
        xaxis=dict(tickangle=-45, linecolor='#262730'),  # Secondary background color for axis lines
        bargap=0.2,  # Bar gap for aesthetics
        yaxis=dict(gridcolor='#262730', linecolor='#262730'),  # Gridlines with secondary background color
    )

    # Return the interactive plot in Streamlit
    with st.container(border=True):
        st.plotly_chart(fig)

# Example usage in Streamlit:
# st.title("Interactive Toss Wins Visualization")
# team_toss_win_at_venues_interactive(2021, 'India')


with st.container(border=True):
    st.header("Team Toss Win Venue")
    # Unique years for selection
    years = toss_data["season"].unique()
    selected_year = st.selectbox("Select a year pls 3", years)

    # Get teams for the selected year
    teams = toss_data_grouped.get_group(selected_year)
    team1 = teams["team1"].unique()
    team2 = teams["team2"].unique()
    team3 = np.unique(np.concatenate((team1, team2)))
    selected_team1 = st.selectbox("Select a team pls 3", team3)
    if st.button("Submit pls 3"):
    	team_toss_win_at_venues_interactive(selected_year,selected_team1)








def team_win_percentage_at_venue(venue,team):
    b = toss_data[toss_data["venue"]==venue]
    c = b[(b["team1"]== team) | (b["team2"]== team)]
    c1 = c.shape[0]
    d = c[c["winner"]== team].shape[0]
    return (["Team {} played {} times on {} and won {} times.".format(team,c1,venue,d),"Making the win percentage at {}: {}.".format(venue,((d/c1)*100))])
    # print("Team {} played {} times on {} and won {} times.".format(team,c1,venue,d))
    # print("Making the win percentage at {}: {}.".format(venue,((d/c1)*100)))

with st.container(border=True):
    st.header("Team Win Percentage At Venue")
    # Unique years for selection
    venues = toss_data["venue"].unique()
    selected_venues = st.selectbox("Select a year pls 4", venues)

    # Get teams for the selected year
    teams = toss_data.groupby("venue").get_group(selected_venues)
    team1 = teams["team1"].unique()
    team2 = teams["team2"].unique()
    team3 = np.unique(np.concatenate((team1, team2)))
    selected_team1 = st.selectbox("Select a team pls 4", team3)
    if st.button("Submit pls 4"):
    	a = team_win_percentage_at_venue(selected_venues,selected_team1)
    	st.write(a[0])
    	st.write(a[1])
