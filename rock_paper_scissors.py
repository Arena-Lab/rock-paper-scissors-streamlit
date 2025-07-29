import streamlit as st
import random

# 🎵 Royalty-free audio assets
CLICK_SOUND = "https://assets.mixkit.co/sfx/preview/mixkit-select-click-1109.mp3"
WIN_SOUND = "https://assets.mixkit.co/sfx/preview/mixkit-achievement-bell-600.mp3"
LOSE_SOUND = "https://assets.mixkit.co/sfx/preview/mixkit-losing-bleeps-2026.mp3"
MUSIC_URL = "https://files.freemusicarchive.org/storage-freemusicarchive-org/music/no_curator/Loyalty_Freak_Music/LO-FI_GROOVES/Loyalty_Freak_Music_-_03_-_YOU_COULD_USE_ME.mp3"

# 🪨📄✂️ ASCII Art
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

# 🔧 Streamlit Config
st.set_page_config(page_title="Rock-Paper-Scissors", page_icon="✊", layout="centered")

# 🎶 Background Music Embed (autoplays on supported browsers)
st.markdown(
    f"""
    <audio autoplay loop>
        <source src="{MUSIC_URL}" type="audio/mpeg">
    </audio>
    """,
    unsafe_allow_html=True
)

# 🎮 App Title
st.title("🎮 Rock-Paper-Scissors Battle")
st.markdown("Customize your nickname and challenge the computer!")

# 🧍 Player Name
player_name = st.text_input("Enter your nickname", "Player")

# 🧮 Score Session
if "score" not in st.session_state:
    st.session_state.score = {"You": 0, "Computer": 0, "Ties": 0}

# 🧠 Game Logic
user_choice = st.selectbox("🤔 What will you throw?", choices)

if st.button("🔥 Play"):
    # 🔊 Click Sound
    st.audio(CLICK_SOUND, format="audio/mp3", autoplay=True)

    computer_choice = random.choice(choices)

    # 🖼️ Show Player Choice
    st.markdown(f"### 🧍 {player_name} chose:")
    st.code(ascii_art[user_choice])

    # 🖼️ Show Computer Choice
    st.markdown("### 🤖 Computer chose:")
    st.code(ascii_art[computer_choice])

    # 🧠 Determine Result
    if user_choice == computer_choice:
        result = "🤝 It's a tie!"
        st.session_state.score["Ties"] += 1
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "🎉 You won!"
        st.audio(WIN_SOUND, format="audio/mp3", autoplay=True)
        st.session_state.score["You"] += 1
    else:
        result = "😢 You lost!"
        st.audio(LOSE_SOUND, format="audio/mp3", autoplay=True)
        st.session_state.score["Computer"] += 1

    # 🏁 Show Result
    st.subheader(result)

# 🧾 Scoreboard
st.markdown("### 📊 Scoreboard")
st.write(st.session_state.score)

# 📱 Mobile Shortcut Tip
st.markdown("---")
st.info("💡 Tip: Add this site to your phone's Home Screen for app-like experience!")
