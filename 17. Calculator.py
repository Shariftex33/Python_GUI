import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Entry field for user input
entry = tk.Entry(window, width=20, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4)

# Function to perform arithmetic operations
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Create buttons for numbers and operations
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(window, text=button, padx=20, pady=20, font=("Arial", 18), command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Function to calculate and display the result
def calculate():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, result)

# Clear button
tk.Button(window, text="C", padx=20, pady=20, font=("Arial", 18), command=lambda: entry.delete(0, tk.END)).grid(row=row_val, column=col_val)

# Equal button
tk.Button(window, text="=", padx=20, pady=20, font=("Arial", 18), command=calculate).grid(row=row_val, column=col_val + 1)

# Run the application
window.mainloop()
