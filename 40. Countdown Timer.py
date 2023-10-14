import tkinter as tk
from tkinter import ttk
import time

# Function to start the countdown
def start_countdown():
    try:
        # Get the user-defined countdown duration in seconds
        countdown_time = int(entry.get())
        
        # Update the label to show the initial countdown time
        label.config(text=f"Time Left: {countdown_time} seconds")
        
        # Disable the entry field and start button
        entry.config(state=tk.DISABLED)
        start_button.config(state=tk.DISABLED)
        
        # Start the countdown
        while countdown_time > 0:
            label.config(text=f"Time Left: {countdown_time} seconds")
            root.update()
            time.sleep(1)
            countdown_time -= 1
        
        # After the countdown is finished, re-enable the entry field and start button
        entry.config(state=tk.NORMAL)
        start_button.config(state=tk.NORMAL)
        label.config(text="Countdown Complete!")
    
    except ValueError:
        label.config(text="Please enter a valid number")

# Create the main window
root = tk.Tk()
root.title("Countdown Timer")

# Create a label for displaying the countdown
label = tk.Label(root, text="", font=("Helvetica", 24))
label.pack(pady=10)

# Create an entry field for user input
entry = ttk.Entry(root, font=("Helvetica", 18))
entry.pack(pady=10)

# Create a start button to initiate the countdown
start_button = ttk.Button(root, text="Start Countdown", command=start_countdown)
start_button.pack(pady=10)

# Run the application
root.mainloop()
