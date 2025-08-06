import streamlit as st
import random
import time

# Page configuration
st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🔢",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .difficulty-card {
        padding: 1rem;
        border-radius: 10px;
        border: 2px solid #ddd;
        margin: 0.5rem 0;
        transition: all 0.3s ease;
    }
    .difficulty-card:hover {
        transform: scale(1.02);
        border-color: #1f77b4;
    }
    .progress-bar {
        width: 100%;
        height: 20px;
        background-color: #f0f0f0;
        border-radius: 10px;
        overflow: hidden;
    }
    .progress-fill {
        height: 100%;
        background-color: #4CAF50;
        transition: width 0.3s ease;
    }
    .hint-box {
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        text-align: center;
    }
    .too-low {
        background-color: #e3f2fd;
        color: #1976d2;
    }
    .too-high {
        background-color: #fff3e0;
        color: #f57c00;
    }
    .correct {
        background-color: #e8f5e8;
        color: #388e3c;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'game_state' not in st.session_state:
    st.session_state.game_state = 'setup'
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'max_attempts' not in st.session_state:
    st.session_state.max_attempts = 10
if 'history' not in st.session_state:
    st.session_state.history = []
if 'games_played' not in st.session_state:
    st.session_state.games_played = 0
if 'games_won' not in st.session_state:
    st.session_state.games_won = 0

# Header
st.title("🔢 Number Guessing Game")
st.markdown("### Can you guess the secret number?")

# Game setup
if st.session_state.game_state == 'setup':
    st.markdown("---")
    st.markdown("#### Choose Difficulty Level")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🟢 Easy\n1-50\n15 attempts"):
            st.session_state.target_number = random.randint(1, 50)
            st.session_state.max_attempts = 15
            st.session_state.range_min = 1
            st.session_state.range_max = 50
            st.session_state.game_state = 'playing'
            st.session_state.attempts = 0
            st.session_state.history = []
            st.session_state.games_played += 1
            st.rerun()
    
    with col2:
        if st.button("🟡 Medium\n1-100\n10 attempts"):
            st.session_state.target_number = random.randint(1, 100)
            st.session_state.max_attempts = 10
            st.session_state.range_min = 1
            st.session_state.range_max = 100
            st.session_state.game_state = 'playing'
            st.session_state.attempts = 0
            st.session_state.history = []
            st.session_state.games_played += 1
            st.rerun()
    
    with col3:
        if st.button("🔴 Hard\n1-200\n7 attempts"):
            st.session_state.target_number = random.randint(1, 200)
            st.session_state.max_attempts = 7
            st.session_state.range_min = 1
            st.session_state.range_max = 200
            st.session_state.game_state = 'playing'
            st.session_state.attempts = 0
            st.session_state.history = []
            st.session_state.games_played += 1
            st.rerun()

# Game playing
elif st.session_state.game_state == 'playing':
    st.markdown("---")
    
    # Game info
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Range", f"{st.session_state.range_min}-{st.session_state.range_max}")
    with col2:
        st.metric("Attempts", f"{st.session_state.attempts}/{st.session_state.max_attempts}")
    with col3:
        st.metric("Remaining", st.session_state.max_attempts - st.session_state.attempts)
    
    # Progress bar
    progress = st.session_state.attempts / st.session_state.max_attempts
    st.markdown('<div class="progress-bar"><div class="progress-fill" style="width: {}%"></div></div>'.format(progress * 100), unsafe_allow_html=True)
    
    # Input guess
    st.markdown("---")
    st.markdown("#### Enter your guess:")
    
    guess = st.number_input(
        f"Guess a number between {st.session_state.range_min} and {st.session_state.range_max}",
        min_value=st.session_state.range_min,
        max_value=st.session_state.range_max,
        value=st.session_state.range_min,
        key="guess_input"
    )
    
    if st.button("🎯 Submit Guess", use_container_width=True):
        st.session_state.attempts += 1
        st.session_state.history.append(guess)
        
        if guess < st.session_state.target_number:
            st.markdown('<div class="hint-box too-low">📈 Too low! Try a higher number.</div>', unsafe_allow_html=True)
        elif guess > st.session_state.target_number:
            st.markdown('<div class="hint-box too-high">📉 Too high! Try a lower number.</div>', unsafe_allow_html=True)
        else:
            st.session_state.games_won += 1
            st.session_state.game_state = 'won'
            st.rerun()
        
        # Check if out of attempts
        if st.session_state.attempts >= st.session_state.max_attempts and guess != st.session_state.target_number:
            st.session_state.game_state = 'lost'
            st.rerun()

    # Guess history
    if st.session_state.history:
        st.markdown("---")
        st.markdown("#### Your guesses:")
        cols = st.columns(min(5, len(st.session_state.history)))
        for idx, past_guess in enumerate(st.session_state.history[-5:]):
            with cols[idx % 5]:
                st.info(f"Guess {idx + 1}: {past_guess}")

# Game won
elif st.session_state.game_state == 'won':
    st.markdown("---")
    st.markdown('<div class="hint-box correct">🎉 Congratulations! You guessed it!</div>', unsafe_allow_html=True)
    
    st.success(f"""
    **You won!** 🏆
    - The number was: **{st.session_state.target_number}**
    - Attempts used: **{st.session_state.attempts}**
    - Success rate: **{(st.session_state.games_won / st.session_state.games_played * 100):.1f}%**
    """)
    
    if st.button("🎮 Play Again"):
        st.session_state.game_state = 'setup'
        st.rerun()

# Game lost
elif st.session_state.game_state == 'lost':
    st.markdown("---")
    st.error(f"""
    **Game Over!** 😢
    - The number was: **{st.session_state.target_number}**
    - You used all {st.session_state.max_attempts} attempts
    - Better luck next time!
    """)
    
    if st.button("🎮 Try Again"):
        st.session_state.game_state = 'setup'
        st.rerun()

# Statistics
st.markdown("---")
st.markdown("### Game Statistics")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Games Played", st.session_state.games_played)
with col2:
    st.metric("Games Won", st.session_state.games_won)
with col3:
    if st.session_state.games_played > 0:
        win_rate = (st.session_state.games_won / st.session_state.games_played) * 100
        st.metric("Win Rate", f"{win_rate:.1f}%")
    else:
        st.metric("Win Rate", "0%")
