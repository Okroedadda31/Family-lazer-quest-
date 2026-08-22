import streamlit as st
import random

st.set_page_config(page_title="Family Laser Quest", page_icon="🔫")

st.title("🔫 Family Laser Quest")

st.write("A fun family laser battle game!")

if "scores" not in st.session_state:
    st.session_state.scores = {}

players = st.text_input("Enter player names (separated by commas):", "Player 1, Player 2")

if st.button("Start / Reset Game"):
    names = [p.strip() for p in players.split(",") if p.strip()]
    st.session_state.scores = {name: 0 for name in names}
    st.success("Game started!")

if st.session_state.scores:
    st.subheader("Players")

    for player in list(st.session_state.scores.keys()):
        col1, col2 = st.columns([2, 1])

        with col1:
            st.write(f"🎯 {player}: {st.session_state.scores[player]} points")

        with col2:
            if st.button(f"Laser hit {player}", key=player):
                points = random.randint(1, 10)
                st.session_state.scores[player] += points
                st.rerun()

    winner = max(st.session_state.scores, key=st.session_state.scores.get)
    st.subheader(f"🏆 Leader: {winner}")

st.write("Keep playing until someone reaches the highest score!")
