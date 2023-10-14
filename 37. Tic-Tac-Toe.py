import tkinter as tk
from tkinter import messagebox

# Initialize the game
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create variables
current_player = "X"
board = [" " for _ in range(9)]

# Create buttons
buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", font=("normal", 20), width=5, height=2,
                       command=lambda i=i: handle_click(i))
    buttons.append(button)
    button.grid(row=i // 3, column=i % 3)

# Function to handle button clicks
def handle_click(index):
    global current_player
    if board[index] == " ":
        buttons[index].config(text=current_player)
        board[index] = current_player
        if check_winner(current_player):
            messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
            reset_game()
        elif " " not in board:
            messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

# Function to check for a winner
def check_winner(player):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to reset the game
def reset_game():
    global current_player, board
    current_player = "X"
    board = [" " for _ in range(9)]
    for button in buttons:
        button.config(text=" ")
    
# Run the game
root.mainloop()
