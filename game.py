import streamlit as st
import random

st.set_page_config(
    page_title="Vinyl Warrior Level 1",
    page_icon="🌴"
)

st.title("🌴 VINYL WARRIOR: THE LOST RIDDIM TRAIL")
st.subheader("🎧 Level 1: Blue Mountain Jungle")

# Game memory
if "health" not in st.session_state:
    st.session_state.health = 100
    st.session_state.score = 0
    st.session_state.stage = 1
    st.session_state.vinyl = 0


# Status bar
st.write("❤️ Health:", st.session_state.health)
st.write("💎 Score:", st.session_state.score)
st.write("💿 Golden Vinyl:", st.session_state.vinyl)

st.divider()


# Game over
if st.session_state.health <= 0:
    st.error("💀 The Riddim Warrior has fallen!")

    if st.button("Restart Game"):
        st.session_state.clear()
        st.rerun()


# LEVEL 1
elif st.session_state.stage == 1:

    st.header("🌿 Stage 1: Rainforest Path")

    st.write(
        "You enter the Jamaican mountains. "
        "Birds sing, rain falls and hidden treasures are everywhere."
    )

    if st.button("🚶 Walk Through Jungle"):

        item = random.choice(
            [
                "🥥 Coconut Energy",
                "🌿 Herbal Power",
                "💿 Golden Vinyl Piece"
            ]
        )

        st.success("You found: " + item)

        st.session_state.score += 10

        if "Vinyl" in item:
            st.session_state.vinyl += 1
        else:
            st.session_state.health += 5


    if st.button("Continue to Swamp 🌊"):
        st.session_state.stage = 2



elif st.session_state.stage == 2:

    st.header("🌊 Stage 2: The Swamp Challenge")

    st.write(
        "A dangerous swamp blocks the path. "
        "Choose your move carefully."
    )

    choice = st.radio(
        "What do you do?",
        [
            "Jump across the rocks",
            "Walk through the mud",
            "Turn back"
        ]
    )


    if st.button("Make Choice"):

        if choice == "Jump across the rocks":

            st.success(
                "Amazing jump! You crossed the swamp."
            )

            st.session_state.score += 50
            st.session_state.stage = 3

        else:

            st.warning(
                "You lose energy!"
            )

            st.session_state.health -= 20



elif st.session_state.stage == 3:

    st.header("🌉 Stage 3: The Wooden Bridge")

    st.write(
        "A small bridge hangs above the river. "
        "Enemy vinyl records fly towards you!"
    )


    move = st.radio(
        "Choose your defence:",
        [
            "Jump",
            "Vinyl Shield",
            "Stand Still"
        ]
    )


    if st.button("Cross Bridge"):

        if move != "Stand Still":

            st.success(
                "You crossed the bridge safely!"
            )

            st.session_state.score += 100
            st.session_state.stage = 4

        else:

            st.error(
                "You fell into the river!"
            )

            st.session_state.health -= 30



elif st.session_state.stage == 4:

    st.header("🌧️ Stage 4: Rain Storm Battle")

    st.write(
        "The Dark Selector appears! "
        "Choose your power."
    )


    power = st.radio(
        "Select Power:",
        [
            "🔥 FIRE BAAALL",
            "🌪️ HURRICANE DUB",
            "💿 VINYL THROW"
        ]
    )


    if st.button("Attack"):

        st.success(
            power + " defeated the Dark Selector!"
        )

        st.session_state.score += 200
        st.session_state.stage = 5



else:

    st.header("🔊 Mountain Sound Temple")

    st.success(
        "🏆 LEVEL COMPLETE!"
    )


    st.write(
        """
        Rewards unlocked:

        🏍️ Yamaha Bike Challenge

        💿 Golden Vinyl Power

        🔥 Fire Baall Ability

        🌴 Next Level: Kingston City
        """
    )



if st.button("Restart Level"):
    st.session_state.clear()
    st.rerun()
