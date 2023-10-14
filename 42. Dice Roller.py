import tkinter as tk
import random

# Function to roll the dice and update the result label
def roll_dice():
    result = random.randint(1, 6)  # Generate a random number between 1 and 6
    result_label.config(text=f"Result: {result}")

# Create the main application window
app = tk.Tk()
app.title("Dice Roller")

# Create a button to roll the dice
roll_button = tk.Button(app, text="Roll Dice", command=roll_dice)
roll_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(app, text="", font=("Arial", 24))
result_label.pack()

# Start the GUI application
app.mainloop()
