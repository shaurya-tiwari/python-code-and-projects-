import streamlit as st
import random
import time

# Page configuration
st.set_page_config(
    page_title="Dice Rolling Game",
    page_icon="🎲",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .dice-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 2rem;
        margin: 2rem 0;
    }
    .dice {
        font-size: 4rem;
        padding: 1rem;
        border: 3px solid #ddd;
        border-radius: 15px;
        background: white;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    .dice:hover {
        transform: scale(1.1);
    }
    .total {
        font-size: 2rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin: 1rem 0;
    }
    .roll-button {
        width: 100%;
        height: 3rem;
        font-size: 1.5rem;
        border-radius: 10px;
        background-color: #ff6b6b;
        color: white;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .roll-button:hover {
        background-color: #ff5252;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'dice_history' not in st.session_state:
    st.session_state.dice_history = []
if 'total_rolls' not in st.session_state:
    st.session_state.total_rolls = 0

# Header
st.title("🎲 Dice Rolling Game")
st.markdown("### Roll the dice and test your luck!")

# Game settings
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    num_dice = st.slider("Number of dice", 1, 6, 2)
with col2:
    sides = st.selectbox("Dice sides", [6, 8, 10, 12, 20], index=0)

# Roll dice button
if st.button("🎲 Roll Dice", key="roll_button", use_container_width=True):
    with st.spinner("Rolling..."):
        time.sleep(0.5)
        
        # Generate dice values
        dice_values = [random.randint(1, sides) for _ in range(num_dice)]
        total = sum(dice_values)
        
        # Store in history
        st.session_state.dice_history.append({
            'dice': dice_values,
            'total': total,
            'sides': sides
        })
        st.session_state.total_rolls += 1

# Display current roll
if st.session_state.dice_history:
    latest_roll = st.session_state.dice_history[-1]
    
    st.markdown("---")
    st.markdown("### Current Roll")
    
    # Display dice
    cols = st.columns(len(latest_roll['dice']))
    for idx, value in enumerate(latest_roll['dice']):
        with cols[idx]:
            st.markdown(f'<div class="dice">{value}</div>', unsafe_allow_html=True)
    
    # Display total
    st.markdown(f'<div class="total">Total: {latest_roll["total"]}</div>', unsafe_allow_html=True)

# Statistics
if st.session_state.dice_history:
    st.markdown("---")
    st.markdown("### Statistics")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Rolls", st.session_state.total_rolls)
    with col2:
        avg_total = sum(roll['total'] for roll in st.session_state.dice_history) / len(st.session_state.dice_history)
        st.metric("Average Total", f"{avg_total:.1f}")
    with col3:
        max_total = max(roll['total'] for roll in st.session_state.dice_history)
        st.metric("Highest Total", max_total)

# History
if st.session_state.dice_history:
    st.markdown("---")
    st.markdown("### Roll History")
    
    # Show last 5 rolls
    recent_rolls = st.session_state.dice_history[-5:]
    for idx, roll in enumerate(reversed(recent_rolls)):
        st.text(f"Roll {len(st.session_state.dice_history) - idx}: {roll['dice']} = {roll['total']}")

# Reset button
if st.button("🔄 Reset History"):
    st.session_state.dice_history = []
    st.session_state.total_rolls = 0
    st.rerun()
