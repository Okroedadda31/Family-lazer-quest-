import streamlit as st
import random
import time

st.set_page_config(
    page_title="Vinyl Warrior: Rise of the Riddim",
    page_icon="🌴"
)

# Game title
st.title("🌴 VINYL WARRIOR: Rise of the Riddim 🔥")

st.write(
    "A Jamaican adventure where rhythm, culture and courage rule the island!"
)

# Start values
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.level = 1
    st.session_state.power = "None"
    st.session_state.items = []

# Character choice
character = st.selectbox(
    "Choose your warrior:",
    [
        "Malik - Riddim Warrior 🎧",
        "Amara - Dub Queen 👑",
        "Jax - Future Selector 🤖"
    ]
)

terrain = st.selectbox(
    "Choose your adventure:",
    [
        "Kingston Streets 🌆",
        "Blue Mountain Jungle 🌴",
        "Caribbean Coast 🌊"
    ]
)

st.divider()

st.subheader(f"Level {st.session_state.level}")
st.write(f"Warrior: {character}")
st.write(f"Location: {terrain}")

# Collect items
items = [
    "🥥 Coconut Power",
    "🌿 Herbal Energy",
    "🎵 Golden Vinyl",
    "🔥 Fire Riddim",
    "💎 Island Gem"
]

if st.button("Walk Forward 🚶🏾"):
    
    item = random.choice(items)
    
    st.session_state.items.append(item)
    st.session_state.score += 10
    
    st.success(f"You found: {item}")
    
    if item == "🔥 Fire Riddim":
        st.session_state.power = "Fire Blast 🔥"
    elif item == "🎵 Golden Vinyl":
        st.session_state.power = "Vinyl Shield 🎧"
    elif item == "🌿 Herbal Energy":
        st.session_state.power = "Nature Strength 🌿"

# Challenge
questions = [
    ("What is the capital of Jamaica?", "Kingston"),
    ("What instrument is famous in reggae?", "Drums"),
    ("Which sea surrounds Jamaica?", "Caribbean")
]

question, answer = random.choice(questions)

st.subheader("🧠 Jungle Challenge")

user_answer = st.text_input(question)

if st.button("Answer Challenge"):
    if user_answer.lower() == answer.lower():
        st.session_state.score += 20
        st.success("Correct! Bonus points added 🎉")
    else:
        st.error("Not quite! Keep learning!")

# Enemy battle
st.subheader("⚔️ Enemy Encounter")

if st.button("Battle Enemy"):
    
    power = random.choice(
        [
            "Vinyl Laser 🎧",
            "Fire Ball 🔥",
            "Hurricane Wind 🌪️",
            "Dub Blast 🔊"
        ]
    )

    st.write(f"You used {power}!")
    
    win = random.choice([True, True, False])

    if win:
        st.success("Enemy defeated! Riddim power grows!")
        st.session_state.score += 50
        st.session_state.level += 1
    else:
        st.warning("Enemy escaped! Train harder!")

# Status
st.divider()

st.subheader("🏆 Warrior Status")

st.write("Score:", st.session_state.score)
st.write("Power:", st.session_state.power)
st.write("Collected:", st.session_state.items)

if st.session_state.level >= 5:
    st.balloons()
    st.success("👑 You have reached KING STATUS!")
