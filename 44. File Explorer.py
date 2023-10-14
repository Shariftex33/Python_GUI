import tkinter as tk
from tkinter import filedialog
import os

# Function to open the file explorer dialog
def open_file_explorer():
    filepath = filedialog.askopenfilename()
    if filepath:
        status_label.config(text=f"Selected File: {os.path.basename(filepath)}")
    else:
        status_label.config(text="No file selected")

# Create the main window
root = tk.Tk()
root.title("File Explorer")

# Create and configure a label to display file status
status_label = tk.Label(root, text="", padx=10, pady=10)
status_label.pack()

# Create a button to open the file explorer dialog
browse_button = tk.Button(root, text="Open File Explorer", command=open_file_explorer)
browse_button.pack(padx=20, pady=10)

# Run the Tkinter main loop
root.mainloop()
