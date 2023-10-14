# Import the Tkinter library
import tkinter as tk
from time import strftime

# Create a tkinter window
root = tk.Tk()
root.title("Digital Clock")

# Function to update the time
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

# Create a label for displaying time
label = tk.Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')

# Pack the label into the tkinter window
label.pack(anchor='center')

# Call the time function to update the time
time()

# Start the tkinter main loop
root.mainloop()
