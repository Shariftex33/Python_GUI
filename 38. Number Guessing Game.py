import tkinter as tk
import random

# Function to check the user's guess
def check_guess():
    user_guess = int(entry_guess.get())
    if user_guess < secret_number:
        result_label.config(text="Too low! Try again.")
    elif user_guess > secret_number:
        result_label.config(text="Too high! Try again.")
    else:
        result_label.config(text=f"Congratulations! You guessed it right, the number was {secret_number}.")

# Function to start a new game
def new_game():
    global secret_number
    secret_number = random.randint(1, 100)
    result_label.config(text="Guess a number between 1 and 100:")
    entry_guess.delete(0, 'end')

# Create the main window
window = tk.Tk()
window.title("Number Guessing Game")

# Create and configure widgets
title_label = tk.Label(window, text="Number Guessing Game", font=("Arial", 18))
result_label = tk.Label(window, text="Guess a number between 1 and 100:", font=("Arial", 12))
entry_guess = tk.Entry(window, width=10, font=("Arial", 12))
check_button = tk.Button(window, text="Check", command=check_guess, font=("Arial", 12))
new_game_button = tk.Button(window, text="New Game", command=new_game, font=("Arial", 12))

# Arrange widgets using grid layout
title_label.grid(row=0, column=0, columnspan=2)
result_label.grid(row=1, column=0, columnspan=2)
entry_guess.grid(row=2, column=0, padx=5, pady=5)
check_button.grid(row=2, column=1, padx=5, pady=5)
new_game_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

# Start a new game when the program runs
new_game()

# Run the main loop
window.mainloop()
