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
