import tkinter as tk
from tkinter import ttk
import calendar

# Function to show the calendar for a given year and month
def show_calendar():
    year = int(year_entry.get())
    month = int(month_combobox.get())
    cal_text.delete(1.0, tk.END)  # Clear previous calendar
    cal = calendar.month(year, month)
    cal_text.insert(tk.END, cal)

# Create the main application window
root = tk.Tk()
root.title("Calendar App")

# Label and Entry for Year
year_label = tk.Label(root, text="Year:")
year_label.pack()
year_entry = tk.Entry(root)
year_entry.pack()

# Label and Combobox for Month
month_label = tk.Label(root, text="Month:")
month_label.pack()
months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
month_combobox = ttk.Combobox(root, values=months)
month_combobox.pack()

# Button to Show Calendar
show_button = tk.Button(root, text="Show Calendar", command=show_calendar)
show_button.pack()

# Text widget to display the calendar
cal_text = tk.Text(root, height=10, width=30)
cal_text.pack()

root.mainloop()
