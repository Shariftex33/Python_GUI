import tkinter as tk
from datetime import datetime

def start():
    global running
    running = True
    update()

def stop():
    global running
    running = False

def reset():
    global running
    running = False
    global counter
    counter = 0
    time_label.config(text="00:00:00")

def update():
    if running:
        global counter
        counter += 1
    minutes, seconds = divmod(counter, 60)
    hours, minutes = divmod(minutes, 60)
    time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    time_label.config(text=time_string)
    root.after(1000, update)

running = False
counter = 0

root = tk.Tk()
root.title("Stopwatch")

time_label = tk.Label(root, text="00:00:00", font=("Arial", 48))
start_button = tk.Button(root, text="Start", command=start)
stop_button = tk.Button(root, text="Stop", command=stop)
reset_button = tk.Button(root, text="Reset", command=reset)

time_label.pack()
start_button.pack()
stop_button.pack()
reset_button.pack()

root.mainloop()
