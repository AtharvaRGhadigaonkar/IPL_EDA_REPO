import numpy as np
import pandas as pd
import warnings
import streamlit as st
warnings.simplefilter(action='ignore', category=FutureWarning)

games_data = pd.read_csv(
    "../data/processed/cleaned_data_deliveries.csv",
    low_memory=False
)
games_data.drop(columns=["Unnamed: 0"],inplace=True)
games_data =games_data.drop(columns=['non_striker',
        'date', 'venue', 'toss_winner', 'toss_decision', 'winner',
       'result', 'result_margin', 'target_runs', 'target_overs', 'super_over',
       'method', 'umpire1', 'umpire2'])

st.write(games_data.columns)

def batsmen_data(year,batsmen):
    grouped_data = games_data.groupby("season").get_group(year).groupby("batter").get_group(batsmen)
    #Batting avg
    total_runs = grouped_data["batsman_runs"].sum()
    total_diss = grouped_data[grouped_data["player_dismissed"]==batsmen].shape[0]
    batting_avg = total_runs/total_diss
    st.write("batting_avg : " , batting_avg)
    #Strike Rate
    total_balls = grouped_data.shape[0] - grouped_data["extras_type"].value_counts().get("wides",0)
    strike_rate = round((total_runs/total_balls)*100,2)
    st.write("strike_rate: ",strike_rate)
    #Total Runs
    st.write("total_runs: ",total_runs)
    #boundary Percentage
    no_of_boundary =grouped_data["batsman_runs"].value_counts().get(4,0)*4+grouped_data["batsman_runs"].value_counts().get(6,0)*6
    boundary_percentage =round((no_of_boundary/total_runs)*100,2)
    st.write("boundary_percentage: ",boundary_percentage)
    #dot Ball
    total_dot_balls = grouped_data["batsman_runs"].value_counts().get(0,0)-grouped_data["extras_type"].value_counts().get("wides",0)
    dot_ball_percentage  = round((total_dot_balls/total_balls)*100,2)
    st.write("dot_ball_percentage: ",dot_ball_percentage)

with st.container(border=True):
    st.header("Batsmen")
    # Unique years for selection
    years = games_data["season"].unique()
    selected_year = st.selectbox("Select a year", years)

    # Get teams for the selected year

    players = games_data.groupby("season").get_group(selected_year)
    players = players["batter"].unique()
    selected_player = st.selectbox("Select a team", players)
    if st.button("Submit"):
        batsmen_data(selected_year,selected_player)


def bowler_data(year,bowler):
    bowler_grouped_data = games_data.groupby("season").get_group(year).groupby("bowler").get_group(bowler)
    
    no_of_balls = bowler_grouped_data.shape[0] - bowler_grouped_data[(bowler_grouped_data["extras_type"]=="noballs") | (bowler_grouped_data["extras_type"]=="wides") ].shape[0]
    st.write("No of Balls : " ,no_of_balls)
    no_of_overs = no_of_balls / 6
    st.write("No of overs: ", no_of_overs)
    total_runs = bowler_grouped_data["batsman_runs"].sum() + bowler_grouped_data[(bowler_grouped_data["extras_type"]=="noballs") | (bowler_grouped_data["extras_type"]=="wides") ].shape[0]
    st.write("No of total runs ",total_runs)
    economy = total_runs/no_of_overs
    st.write("econmomy " ,economy)
    no_of_wickets = bowler_grouped_data[bowler_grouped_data["dismissal_kind"].isna()==False].shape[0]
    st.write("No of Wickets " ,no_of_wickets)
    Bolwing_avg = total_runs/no_of_wickets
    st.write("Bolwing avg  " ,Bolwing_avg)
    strike_rate = no_of_balls/no_of_wickets
    boundary_percentage = ((bowler_grouped_data[bowler_grouped_data["batsman_runs"]== 4].shape[0])+(bowler_grouped_data[bowler_grouped_data["batsman_runs"]== 6].shape[0]))/no_of_balls
    boundary_percentage = boundary_percentage * 100
    st.write("Boundary percentage: " ,boundary_percentage)

with st.container(border=True):
    st.header("Bowler")
    # Unique years for selection
    years1 = games_data["season"].unique()
    selected_year1 = st.selectbox("Select a year 1", years1)

    # Get teams for the selected year

    players1 = games_data.groupby("season").get_group(selected_year1)
    players1 = players1["bowler"].unique()
    selected_player1 = st.selectbox("Select a Bowler", players1)
    if st.button("Submit1"):
        bowler_data(selected_year1,selected_player1)



def bowler_data_without_year(bowler):
    bowler_grouped_data = games_data.groupby("bowler").get_group(bowler)
    
    no_of_balls = bowler_grouped_data.shape[0] - bowler_grouped_data[(bowler_grouped_data["extras_type"]=="noballs") | (bowler_grouped_data["extras_type"]=="wides") ].shape[0]
    st.write("No of Balls : " ,no_of_balls)
    no_of_overs = no_of_balls / 6
    st.write("No of overs: ", no_of_overs)
    total_runs = bowler_grouped_data["batsman_runs"].sum() + bowler_grouped_data[(bowler_grouped_data["extras_type"]=="noballs") | (bowler_grouped_data["extras_type"]=="wides") ].shape[0]
    st.write("No of total runs ",total_runs)
    economy = total_runs/no_of_overs
    st.write("econmomy " ,economy)
    no_of_wickets = bowler_grouped_data[bowler_grouped_data["dismissal_kind"].isna()==False].shape[0]
    st.write("No of Wickets " ,no_of_wickets)
    Bolwing_avg = total_runs/no_of_wickets
    st.write("Bolwing avg  " ,Bolwing_avg)
    strike_rate = no_of_balls/no_of_wickets
    boundary_percentage = ((bowler_grouped_data[bowler_grouped_data["batsman_runs"]== 4].shape[0])+(bowler_grouped_data[bowler_grouped_data["batsman_runs"]== 6].shape[0]))/no_of_balls
    boundary_percentage = boundary_percentage * 100
    st.write("Boundary percentage: " ,boundary_percentage)

with st.container(border=True):
    st.header("Bowler no year")
    players2 = games_data["bowler"].unique()
    selected_player2 = st.selectbox("Select a Bowler 2", players2)
    if st.button("Submit2"):
        bowler_data_without_year(selected_player2)