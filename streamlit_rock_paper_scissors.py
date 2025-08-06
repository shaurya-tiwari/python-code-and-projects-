import streamlit as st
import random
import time

# Page configuration
st.set_page_config(
    page_title="Rock Paper Scissors",
    page_icon="✊",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton > button {
        width: 100%;
        height: 3rem;
        font-size: 1.2rem;
        border-radius: 10px;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: scale(1.05);
    }
    .result-box {
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
    }
    .win { background-color: #d4edda; color: #155724; }
    .lose { background-color: #f8d7da; color: #721c24; }
    .draw { background-color: #fff3cd; color: #856404; }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'score' not in st.session_state:
    st.session_state.score = {'player': 0, 'computer': 0, 'draws': 0}
if 'game_history' not in st.session_state:
    st.session_state.game_history = []

# Game logic
def determine_winner(player_choice, computer_choice):
    choices = {'rock': '✊', 'paper': '✋', 'scissors': '✌️'}
    rules = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    if player_choice == computer_choice:
        return "draw"
    elif rules[player_choice] == computer_choice:
        return "win"
    else:
        return "lose"

# Header
st.title("🎮 Rock Paper Scissors")
st.markdown("### Choose your weapon and battle the computer!")

# Score display
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Your Score", st.session_state.score['player'])
with col2:
    st.metric("Computer Score", st.session_state.score['computer'])
with col3:
    st.metric("Draws", st.session_state.score['draws'])

# Game choices
st.markdown("---")
st.markdown("#### Make your choice:")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("✊ Rock"):
        player_choice = 'rock'
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        
        result = determine_winner(player_choice, computer_choice)
        
        # Update score
        if result == "win":
            st.session_state.score['player'] += 1
            st.success("🎉 You Win!")
        elif result == "lose":
            st.session_state.score['computer'] += 1
            st.error("😢 You Lose!")
        else:
            st.session_state.score['draws'] += 1
            st.warning("🤝 It's a Draw!")
        
        # Display choices
        col_a, col_b = st.columns(2)
        with col_a:
            st.info(f"**You chose:** {player_choice} ✊")
        with col_b:
            st.info(f"**Computer chose:** {computer_choice} {['✊', '✋', '✌️'][['rock', 'paper', 'scissors'].index(computer_choice)]}")

with col2:
    if st.button("✋ Paper"):
        player_choice = 'paper'
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        
        result = determine_winner(player_choice, computer_choice)
        
        if result == "win":
            st.session_state.score['player'] += 1
            st.success("🎉 You Win!")
        elif result == "lose":
            st.session_state.score['computer'] += 1
            st.error("😢 You Lose!")
        else:
            st.session_state.score['draws'] += 1
            st.warning("🤝 It's a Draw!")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.info(f"**You chose:** {player_choice} ✋")
        with col_b:
            st.info(f"**Computer chose:** {computer_choice} {['✊', '✋', '✌️'][['rock', 'paper', 'scissors'].index(computer_choice)]}")

with col3:
    if st.button("✌️ Scissors"):
        player_choice = 'scissors'
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        
        result = determine_winner(player_choice, computer_choice)
        
        if result == "win":
            st.session_state.score['player'] += 1
            st.success("🎉 You Win!")
        elif result == "lose":
            st.session_state.score['computer'] += 1
            st.error("😢 You Lose!")
        else:
            st.session_state.score['draws'] += 1
            st.warning("🤝 It's a Draw!")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.info(f"**You chose:** {player_choice} ✌️")
        with col_b:
            st.info(f"**Computer chose:** {computer_choice} {['✊', '✋', '✌️'][['rock', 'paper', 'scissors'].index(computer_choice)]}")

# Reset button
if st.button("🔄 Reset Score"):
    st.session_state.score = {'player': 0, 'computer': 0, 'draws': 0}
    st.rerun()
