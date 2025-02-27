import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import csv
import numpy 



st.title("NCAA Women's Volleyball Match Stats")
#uploaded_file = st.file_uploader("Choose a CSV file", type="csv")


#Makes it so it only reads this data and no other
df = pd.read_csv("cleaned_volley_data.csv")
columns = df.columns.tolist()
team_column = "Team"
No_team_column = "aces_per_set","assists_per_set","team_attacks_per_set","blocks_per_set","digs_per_set","digs_per_set","hitting_pctg","kills_per_set","opp_hitting_pctg","W","L","win_loss_pctg"

st.subheader("Data Preview")
st.write(df.head())

st.subheader("Data Summary")
#This gets shows the mean, range(min and max) and median (the 50 percentile)
st.write(df.describe())
mode_for_vb = df.mode().iloc[0]  # Gets the first mode if there are multiple modes

# This is how it will show 
st.write("This is the mode:")
st.write(mode_for_vb)



#title
st.subheader("Plot Data")
x_column = st.selectbox("Select x-axis column", No_team_column )
y_column = st.selectbox("y-axis is Team", team_column)
# scatters the two different columns the one with teams and the one with everything else. 
if st.button("Generate Plot"):
    fig = px.scatter(df, x=x_column, y="Team" )
    st.plotly_chart(fig)
  

# title
st.subheader("Winning vs. Losing Teams Comparison")

# I defined a function to show the match outcome which divides the 'W' and 'L' columns. 
def get_match_outcome(row):
    if row["W"] > row["L"]:
        return 'W'
    else:
        return 'L'


# I created the 'match_outcome' column by applying the function to each row
df["match_outcome"] = df.apply(get_match_outcome, axis=1)
# Checking if the 'match_outcome' column is created
if "match_outcome" in df.columns:
    # Selecting the different stat to generate the plot. I used the format from plot data
    #selected_column = st.selectbox("Select column to filter by", No_team_column )
    #unique_values = df[selected_column].unique()
    vb_stats = st.selectbox("Select the statistic to plot", No_team_column )
   
    # Creating the box plot and it's comparing vb_stats by match outcome
    fig = px.box(df, x="match_outcome", y= vb_stats , title=f"{vb_stats} by Match Outcome")
    
    # Displaying the plot in Streamlit
    st.plotly_chart(fig)

