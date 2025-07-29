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

st.set_page_config(page_title="Rock-Paper-Scissors", page_icon="🎮")

st.title("🎮 Rock-Paper-Scissors Game")
st.write("Choose Rock, Paper, or Scissors to play against the computer!")

# Score Tracking
if "score" not in st.session_state:
    st.session_state.score = {"You": 0, "Computer": 0, "Ties": 0_
