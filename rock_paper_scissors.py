import streamlit as st
import random
import time

# 🎵 Royalty-free audio links
CLICK_SOUND = "https://assets.mixkit.co/sfx/preview/mixkit-select-click-1109.mp3"
WIN_SOUND = "https://assets.mixkit.co/sfx/preview/mixkit-achievement-bell-600.mp3"
LOSE_SOUND = "https://assets.mixkit.co/sfx/preview/mixkit-losing-bleeps-2026.mp3"

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

# Setup
st.set_page_config(page_title="Couple RPS", page_icon="💑", layout="centered")

st.title("💑 Couple Rock-Paper-Scissors")
st.markdown("Let two players battle it out with animated fun and emoji-filled action!")

# Player names
p1 = st.text_input("Player 1 Name (🧍)", value="Player 1")
p2 = st.text_input("Player 2 Name (🧍‍♀️)", value="Player 2")

# Score Tracker
if "score" not in st.session_state:
    st.session_state.score = {p1: 0, p2: 0, "Ties": 0}

# Player 1 Choice
p1_choice = st.selectbox(f"{p1}, make your move ✊✋✌️", choices, key="p1_choice")
if st.button("✅ Lock Player 1's Choice"):
    st.session_state.p1_choice_locked = p1_choice
    st.success(f"{p1} has locked their choice! Now it's {p2}'s turn.")

# Player 2 Choice
if "p1_choice_locked" in st.session_state:
    p2_choice = st.selectbox(f"{p2}, your move ✊✋✌️", choices, key="p2_choice")
    if st.button("🔥 Play Round"):
        st.audio(CLICK_SOUND, format="audio/mp3", autoplay=True)
        time.sleep(0.4)

        # Show Choices
        st.markdown(f"### 🧍 {p1} chose:")
        st.code(ascii_art[st.session_state.p1_choice_locked])
        time.sleep(0.4)

        st.markdown(f"### 🧍‍♀️ {p2} chose:")
        st.code(ascii_art[p2_choice])
        time.sleep(0.4)

        # Determine result
        p1_move = st.session_state.p1_choice_locked
        p2_move = p2_choice

        if p1_move == p2_move:
            result = "🤝 It's a tie!"
            st.session_state.score["Ties"] += 1
        elif (p1_move == "Rock" and p2_move == "Scissors") or \
             (p1_move == "Paper" and p2_move == "Rock") or \
             (p1_move == "Scissors" and p2_move == "Paper"):
            result = f"🎉 {p1} wins this round!"
            st.audio(WIN_SOUND, format="audio/mp3", autoplay=True)
            st.session_state.score[p1] += 1
        else:
            result = f"🔥 {p2} wins this round!"
            st.audio(LOSE_SOUND, format="audio/mp3", autoplay=True)
            st.session_state.score[p2] += 1

        # Show result with animation
        st.balloons()
        st.subheader(result)

        # Reset turn
        del st.session_state.p1_choice_locked

# Scoreboard
st.markdown("### 📊 Scoreboard")
st.write(st.session_state.score)

# Reset Option
if st.button("🔁 Reset Game"):
    st.session_state.score = {p1: 0, p2: 0, "Ties": 0}
    st.success("Game has been reset!")

st.markdown("---")
st.info("📱 Tip: Add this to your phone's home screen to play anytime!")
