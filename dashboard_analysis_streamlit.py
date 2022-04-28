

import streamlit as st
import pandas as pd

games = pd.read_csv('games.csv')
teams = pd.read_csv('nfl_teams.csv')

st.title('NFL Team Betting Analysis')

option = st.selectbox('Which analysis would you like to see?', 
    ['Win/Loss Record', 'Over/Under Record', 'Record Against the Spread', 'Profit from Betting the Spread'])

team = st.selectbox('Select a team:', teams['team_id'].unique())

season = st.selectbox('Select a season', games['schedule_season'].unique())

subset_year = games[games['schedule_season'] == season]

if option == 'Win/Loss Record':

    wins = (subset_year.winning_team == team).sum()
    losses = (subset_year.losing_team == team).sum()
    ties = (subset_year.tying_team_home == team).sum() + (subset_year.tying_team_away == team).sum()

    st.write(team, ' went ', wins, '-', losses, '-', ties, ' in ', season)

elif option == 'Over/Under Record':

    wins = (subset_year.over_winner_home == team).sum() + (subset_year.over_winner_away == team).sum()
    losses = (subset_year.over_loser_home == team).sum() + (subset_year.over_loser_away == team).sum()
    ties = (subset_year.over_push_home == team).sum() + (subset_year.over_push_away == team).sum()

    st.write(team, ' went ', wins, '-', losses, '-', ties, ' in beating the over ', season)

elif option == 'Record Against the Spread':

    wins = (subset_year.spread_winner == team).sum()
    losses = (subset_year.spread_loser == team).sum()
    ties = (subset_year.push_team_home == team).sum() + (subset_year.push_team_away == team).sum()

    st.write(team, ' went ', wins, '-', losses, '-', ties, ' against the spread in ', season)

else:

    wins = (subset_year.spread_winner == team).sum()
    losses = (subset_year.spread_loser == team).sum()
    ties = (subset_year.push_team_home == team).sum() + (subset_year.push_team_away == team).sum()

    winnings = wins * 90.91 - (losses * 100)
    winnings = round(winnings, 2)

    st.write('If you bet 100 dollars on ', team, ' to cover the spread in every game in ', 
        season, ', you would have won (or lost) ', winnings, ' dollars')





