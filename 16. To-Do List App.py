import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)

# Create the main window
root = tk.Tk()
root.title("To-Do List App")

# Create a listbox to display tasks
listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.pack(pady=20)

# Create an entry widget for adding tasks
entry = tk.Entry(root)
entry.pack(pady=5)

# Create Add and Remove buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
add_button.pack()
remove_button.pack()

root.mainloop()
