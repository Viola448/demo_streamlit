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
team_column = ["Team"]
No_team_column = ["aces_per_set","assists_per_set","team_attacks_per_set","blocks_per_set","digs_per_set","hitting_pctg","kills_per_set","opp_hitting_pctg","W","L","win_loss_pctg"]
W_L_column = ["W","L"]
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
    x_column = st.selectbox("Select x-axis column", No_team_column,key="x_column_plot" )
    y_column = st.selectbox("y-axis is Team", team_column,key="y_column_plot")
    # scatters the two different columns the one with teams and the one with everything else. 
    if st.button("Generate plot"):
        fig = px.scatter(df, x=x_column, y= team_column )
        st.plotly_chart(fig)
        #Used keys as there were too many similar selectboxes
    x_column_selectbox = st.selectbox("Select x-axis column", "Team", key="x_column_box"  )
    y_column_selectbox = st.selectbox("y-axis is Team", W_L_column,key="y_column_box") 
    # Shows wins and loses of teams    
    if st.button("Generate Histogram"):
        fig = px.histogram(df,  x=x_column_selectbox, y=y_column_selectbox)
        st.plotly_chart(fig)

   


elif selected == "Form":
  with st.form("volleyball_questions"):
    # User selects a question
        question = st.selectbox("What do you want to know?", [
        "Show all teams with more than X wins",
        "Compare two teams",
        "Show teams with a hitting percentage above X",
        "Which team has the most aces per set?"
    ])

    # if questions 
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
            #javascript alert uses script to pop up message
            components.html("""
        <script>
        alert('You have submitted the form!');  
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
    #recomdentation
    st.markdown("**You can view from the plot how teams perform in different areas like aces per set, assists per set, team attacks per set, blocks per set, and digs per set.**")
    st.markdown("If we look at the aces per set statistic, there are teams like **Lafayette** and **Delaware ST.** that seem to dominate and outperform others consistently. These teams have a very good serving game, and it would be best to focus on maintaining or building on this. Serving can actually be used to put pressure on the other team right away and earn points outright.")
    st.markdown("The digs per set shows that **Mcneese** is defending strongly. With more digs, they are managing to successfully return balls and maintain rallies even under pressure. Teams weaker in this area might need to devote more time in training to developing defensive skills, particularly receiving serve and defending against strong attacking.")
    st.markdown("In blocks per set, **Maryland** is progressing with outstanding net defense. Large blocking numbers are often among the secrets of stifling opponent attack. Lower rated teams in terms of block percentage success may take some time working on block skills—improved timing and positioning could place them more solidly in charge at the net.")
    st.markdown("The team with the most wins are three teams **Louisville**, **San Diego** and **Pitsburgh** which might seem suprising as most of their performences are high but they arent the outstanding ones. You see by this that it's important to keep a high percentage in everything to have a good overall win streak")
    st.markdown("**My recommendation is that each team has to identify their weak point and improve on it to become more skilled and rank higher. I hope my project helped coaches and players see what they need to improve on.**")
    st.write("What did you think of this website?")
    sentiment = ["one","two","three","four","five"]
    select = st.feedback("stars")
    if select is not None:
        st.markdown(f"You have selected {sentiment[select]}")
    

