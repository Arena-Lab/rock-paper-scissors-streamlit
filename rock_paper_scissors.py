import streamlit as st
import random

# ASCII Art
ascii_art = {
    "Rock": ''' 
    _______
---'   ____)
      (_____)
      (_____)    
      (____)
---.__(___)
ROCK''',
    "Paper": ''' 
     _______
---'    ____)____
           ______)
          _______)     
         _______)
---.__________)
PAPER''',
    "Scissors": ''' 
    _______
---'   ____)____
          ______)
       __________)    
      (____)
---.__(___)
SCISSORS'''
}

choices = ["Rock", "Paper", "Scissors"]

# Set page config
st.set_page_config(page_title="Rock-Paper-Scissors", page_icon="🎮")

# Title
st.title("🎮 Rock-Paper-Scissors Game")
st.write("Choose Rock, Paper, or Scissors to play against the computer!")

# Score Tracking
if "score" not in st.session_state:
    st.session_state.score = {"You": 0, "Computer": 0, "Ties": 0}

# User Choice
user_choice = st.selectbox("Make your choice:", choices)

if st.button("Play"):
    computer_choice = random.choice(choices)

    # Show Choices
    st.markdown("### 🧍 You chose:")
    st.code(ascii_art[user_choice])
    
    st.markdown("### 🤖 Computer chose:")
    st.code(ascii_art[computer_choice])

    # Game Logic
    if user_choice == computer_choice:
        result = "🤝 It's a tie!"
        st.session_state.score["Ties"] += 1
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "🎉 You won!"
        st.session_state.score["You"] += 1
    else:
        result = "😢 You lost!"
        st.session_state.score["Computer"] += 1

    # Show result
    st.subheader(result)

    # Display Score
    st.markdown("### 🧮 Scoreboard")
    st.write(st.session_state.score)

# Footer
st.markdown("---")
st.info("Deploy this app on Streamlit Cloud and share the link with friends!")
