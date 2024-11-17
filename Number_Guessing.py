import streamlit as st
import random

# Function to start a new game
def start_new_game():
    return random.randint(1, 10), 0  # Return random number and number of attempts

# Title of the app
st.title("🎲 Number Guessing Game 🎮")

# Instructions
st.markdown("""
    ## Welcome to the Number Guessing Game!  
    I am thinking of a number between 1 and 100. Try to guess it!  
    Each time you make a guess, I will tell you whether the number is **higher** or **lower**.  
    Let's see how many attempts it takes for you to guess the correct number!  
""")

# Start the game
if 'secret_number' not in st.session_state:
    st.session_state.secret_number, st.session_state.attempts = start_new_game()

# Input for the player's guess
guess = st.number_input("Enter your guess:", min_value=1, max_value=10, step=1)

# Submit button
if st.button("Guess"):
    # Check if the guess is correct
    if guess < st.session_state.secret_number:
        st.session_state.attempts += 1
        st.success("🔼 Your guess is too low! Try again.")
    elif guess > st.session_state.secret_number:
        st.session_state.attempts += 1
        st.success("🔽 Your guess is too high! Try again.")
    else:
        st.session_state.attempts += 1
        st.balloons()
        st.success(f"🎉 Congratulations! You've guessed the number in {st.session_state.attempts} attempts.")
        st.session_state.secret_number, st.session_state.attempts = start_new_game()  # Reset game

# Show number of attempts
st.sidebar.subheader("Game Stats")
st.sidebar.write(f"Attempts: {st.session_state.attempts}")

# Button to start a new game
if st.sidebar.button("Start New Game"):
    st.session_state.secret_number, st.session_state.attempts = start_new_game()
    st.success("Game has been reset. Good luck!")
