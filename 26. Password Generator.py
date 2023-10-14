import tkinter as tk
import random
import string

# Function to generate a random password
def generate_password():
    password_length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(password_length))
    result_label.config(text=password)

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Label for password length
length_label = tk.Label(window, text="Password Length:")
length_label.pack()

# Entry field for password length
length_entry = tk.Entry(window)
length_entry.pack()

# Button to generate password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Label to display the generated password
result_label = tk.Label(window, text="")
result_label.pack()

# Start the Tkinter main loop
window.mainloop()
