import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import csv
import numpy 
df = pd.read_csv("cleaned_volley_data.csv")
columns = df.columns.tolist()
team_column = "Team"
No_team_column = "aces_per_set","assists_per_set","team_attacks_per_set","blocks_per_set","digs_per_set","digs_per_set","hitting_pctg","kills_per_set","opp_hitting_pctg","W","L","win_loss_pctg"
hitting_team_column = "Team","hitting_pctg"
with st.sidebar: 

    selected = option_menu( 

            menu_title=None,  # required 

            options=["Home", "Statisics", "Form","Feedback"],  # required 

            icons=["house", "clipboard2-data", "file-earmark-person","patch-question"],  # optional 

            menu_icon="cast",  # optional 

            default_index=0,  # optional 

             

         styles={ 

                "container": {"padding": "0!important", "background-color": "#00AEEF"}, 

                "icon": {"color": "#000000", "font-size": "25px"}, 

                "nav-link": { 

                    "font-size": "25px", 

                    "text-align": "left", 

                    "margin": "0px", 

                    "--hover-color": "#3b6894", 

                }, 

                "nav-link-selected": {"background-color": "#FFCC00"}, 

            }, 

  ) 

 

if selected == "Home": 
    st.title("NCAA Women's Volleyball Match Stats")

    st.subheader("Introduction")
    st.write("This project is a critical analysis of key performance metrics of the 2022-2023 NCAA Division 1 Women's Volleyball league, particularly with regard to offense and defense. Using a Streamlit dashboard, I analyze various statistics like attack attempts, kills, blocks, digs, and overall team performance to determine efficiency, success percentage, and overall game outcomes. NCAA Women's Volleyball revolves around an attack-defense system upon which kills depend upon defense plays like blocks and digs. Kill-to-attack ratio for 2022-2023 averages 22%-27%, meaning approximately one in four or five attempts that kill. It varies with team play and opposition defense. Performance measurement, winning strategies, and factors leading to success are highlighted using visualizations since between teams they are compared and tracking patterns.")
    st.subheader("Key terms")
    st.markdown("**Attack**- hitting the ball to the floor on the opponent’s side.")
    st.markdown("**Block**- One or more players making a defensive play to return a spiked ball to the hitter's court")
    st.markdown("**Kill**- An attack that causes immediate point or side out.")
    st.markdown("**Dig**- Diving to save and pass a spiked or fast-moving ball close to the floor.")
    st.markdown("**Assits**- Passing or setting the ball to a teammate who attacks the ball for a kill.")
    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    #This gets shows the mean, range(min and max) and median (the 50 percentile)
    st.write(df.describe())
    mode_for_vb = df.mode().iloc[0]  # Gets the first mode if there are multiple modes

    # This is how it will show 
    st.write("This is the mode:")
    st.write(mode_for_vb)



    


   
elif selected == "Statisics": 
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

elif selected == "Form":
  
    with st.form("volleyball_query_form"):
    # User selects a question
        question = st.selectbox("What do you want to know?", [
        "Show all teams with more than X wins",
        "Compare two teams",
        "Show teams with a hitting percentage above X",
        "Which team has the most aces per set?"
    ])

    # Dynamic input fields based on the selected question
        if question == "Show all teams with more than X wins":
            min_wins = st.number_input("Enter minimum wins:", min_value=0, step=1, value=10)
        elif question == "Compare two teams":
            team1 = st.selectbox("Select first team", df["Team"])
            team2 = st.selectbox("Select second team", df["Team"])
        elif question == "Show teams with a hitting percentage above X":
            min_hitting = st.slider("Select minimum hitting percentage:", 0.0, 1.0, 0.2)

    # Submit button
        submitted = st.form_submit_button("Submit")

        if submitted:
            components.html("""
        <script>
        alert('You have submitted the form!');  // Alert after form submission
        </script>
    """, height=0)
        st.write("### 📊 **Results**")

        

        if question == "Show all teams with more than X wins":
            filtered_teams = df[df["W"] > min_wins]
            st.write(filtered_teams[["Team","W"]])

        elif question == "Compare two teams":
            compare_df = df[df["Team"].isin([team1, team2])]
            st.write(compare_df)
            

        elif question == "Show teams with a hitting percentage above X":
            filtered_teams = df[df["hitting_pctg"] > min_hitting]
            st.write(filtered_teams[["Team","hitting_pctg"]])

        elif question == "Which team has the most aces per set?":
            best_aces_team = df.loc[df["aces_per_set"].idxmax()]
            st.write(best_aces_team["Team"], "has the most aces per set:", best_aces_team["aces_per_set"])

elif selected == "Feedback":
    st.write("hi")
    

