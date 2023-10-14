import tkinter as tk
import random

# Function to handle user choice and determine the winner
def play_game(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result_label.config(text="It's a Tie!")
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result_label.config(text="You Win!")
    else:
        result_label.config(text="Computer Wins!")

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Create a label for instructions
instructions_label = tk.Label(root, text="Select Rock, Paper, or Scissors:")
instructions_label.pack()

# Create buttons for player's choices
rock_button = tk.Button(root, text="Rock", command=lambda: play_game("Rock"))
paper_button = tk.Button(root, text="Paper", command=lambda: play_game("Paper"))
scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("Scissors"))

rock_button.pack()
paper_button.pack()
scissors_button.pack()

# Create a label to display the game result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the Tkinter event loop
root.mainloop()
