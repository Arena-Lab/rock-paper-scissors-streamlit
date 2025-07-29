
import streamlit as st
import random

# 3D ASCII Art
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

# Page Config
st.set_page_config(page_title="Rock-Paper-Scissors 3D", page_icon="🕹️", layout="centered")

# CSS Fix for Input Visibility and Style
st.markdown("""
    <style>
    html, body, [class*="css"] {
        background: linear-gradient(to right, #1c1c2b, #2e2e3a);
        color: #fff;
        font-family: 'Segoe UI', sans-serif;
    }
    input, select, textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
        border-radius: 8px !important;
        padding: 10px !important;
        font-size: 16px !important;
    }
    .stButton>button {
        background: linear-gradient(to right, #ff416c, #ff4b2b);
        color: white;
        font-size: 16px;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.05);
    }
    .emoji {
        font-size: 60px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='emoji'>🎮 Rock-Paper-Scissors Battle</h1>", unsafe_allow_html=True)
st.markdown("#### Enter your name and challenge the computer in a 3D-styled battle!")

# Input
player_name = st.text_input("Your Nickname:", value="", max_chars=20)

# Score Tracker
if "score" not in st.session_state:
    st.session_state.score = {"You": 0, "Computer": 0, "Ties": 0}

# Choice selection
user_choice = st.selectbox("🧠 What will you throw?", choices)

if st.button("🔥 Play"):
    computer_choice = random.choice(choices)

    st.markdown(f"### 🧍 {player_name or 'You'} chose:")
    st.code(ascii_art[user_choice])

    st.markdown("### 🤖 Computer chose:")
    st.code(ascii_art[computer_choice])

    # Game logic
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

    st.subheader(result)

# Scoreboard
st.markdown("---")
st.markdown("## 📊 Scoreboard")
st.markdown(f"""
- 🧍 You: `{st.session_state.score['You']}`
- 🤖 Computer: `{st.session_state.score['Computer']}`
- 🤝 Ties: `{st.session_state.score['Ties']}`
""")

# Mobile Shortcut Info
st.markdown("---")
st.info("💡 Tip: On mobile, tap the browser's menu and **'Add to Home Screen'** for app-like use!")
