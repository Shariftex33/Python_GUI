import tkinter as tk
from tkinter import messagebox
import time
import winsound

# Function to set the alarm
def set_alarm():
    alarm_time = entry.get()
    try:
        time.strptime(alarm_time, "%H:%M")
        while True:
            current_time = time.strftime("%H:%M")
            if current_time == alarm_time:
                messagebox.showinfo("Alarm", "Time to wake up!")
                winsound.Beep(1000, 1000)  # Beep sound for 1 second
                break
    except ValueError:
        messagebox.showerror("Error", "Invalid time format. Use HH:MM.")

# Create the main window
root = tk.Tk()
root.title("Alarm Clock")

# Label and entry for setting the alarm time
label = tk.Label(root, text="Enter alarm time (HH:MM):")
label.pack(pady=10)
entry = tk.Entry(root)
entry.pack()

# Button to set the alarm
set_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_button.pack()

# Run the Tkinter main loop
root.mainloop()
