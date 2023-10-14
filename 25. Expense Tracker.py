import tkinter as tk

def add_expense():
    expense = expense_entry.get()
    amount = float(amount_entry.get())

    if expense and amount > 0:
        expense_listbox.insert(tk.END, f"{expense}: ${amount:.2f}")
        total.set(total.get() + amount)
        expense_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Expense Tracker")

# Create and set a variable for the total expense
total = tk.DoubleVar()
total.set(0)

# Expense Entry
expense_label = tk.Label(root, text="Expense:")
expense_label.pack()
expense_entry = tk.Entry(root)
expense_entry.pack()

# Amount Entry
amount_label = tk.Label(root, text="Amount ($):")
amount_label.pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

# Add Expense Button
add_button = tk.Button(root, text="Add Expense", command=add_expense)
add_button.pack()

# Expense List
expense_listbox = tk.Listbox(root)
expense_listbox.pack()

# Total Expense Label
total_label = tk.Label(root, text="Total Expense ($):")
total_label.pack()
total_label_value = tk.Label(root, textvariable=total)
total_label_value.pack()

root.mainloop()
