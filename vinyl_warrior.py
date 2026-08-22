import streamlit as st
import random

st.set_page_config(page_title="Vinyl Warrior", page_icon="💿")

st.title("🌴 VINYL WARRIOR: Rise of the Riddim King")

if "level" not in st.session_state:
    st.session_state.level = 1
    st.session_state.points = 0
    st.session_state.items = []

character = st.selectbox("Choose your warrior", [
    "Malik - Riddim Warrior",
    "Amara - Dub Queen",
    "Jax - Future Selector"
])

terrain = st.selectbox("Choose your adventure", [
    "Kingston Streets 🌆",
    "Blue Mountains ⛰️",
    "Jamaica Coast 🌴",
    "Rural Road 🏍️"
])

st.write("Hero:", character)
st.write("Location:", terrain)
st.write("Level:", st.session_state.level)
st.write("Points:", st.session_state.points)

if st.button("🚶 Walk through Jamaica"):
    item = random.choice(["🥥 Coconut", "🥭 Mango", "🌿 Herb", "💎 Riddim Gem"])
    st.session_state.items.append(item)
    st.session_state.points += 10
    st.success("Found " + item)

q = st.selectbox("Bush challenge: What is the capital of Jamaica?", ["Choose answer", "Kingston", "Montego Bay", "Negril"])

if st.button("Answer"):
    if q == "Kingston":
        st.session_state.level += 1
        st.session_state.points += 25
        st.success("Correct! Riddim power increased!")
    else:
        st.error("Wrong answer!")

st.subheader("💿 Powers")
st.button("🔥 FIRE BAAALL")
st.button("🎧 SELECTAAAA")
st.button("🌪️ HURRICANE DUB")

if st.session_state.level >= 5:
    st.success("🏍️ Red Yamaha bike unlocked!")

st.write("Collected:", st.session_state.items)
