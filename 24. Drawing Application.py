# Import the Tkinter library
import tkinter as tk

# Create a function to change the pen color
def change_color(new_color):
    global pen_color
    pen_color = new_color

# Create a function to clear the canvas
def clear_canvas():
    canvas.delete("all")

# Create a function to handle mouse button click
def start_drawing(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

# Create a function to handle mouse movement
def draw(event):
    global last_x, last_y
    x, y = event.x, event.y
    canvas.create_line((last_x, last_y, x, y), fill=pen_color, width=2)
    last_x, last_y = x, y

# Create the main application window
app = tk.Tk()
app.title("Drawing Application")

# Create a canvas for drawing
canvas = tk.Canvas(app, bg="white", width=400, height=400)
canvas.pack()

# Create buttons for color selection and clearing canvas
colors = ["red", "green", "blue", "black"]
for color in colors:
    tk.Button(app, bg=color, width=2, command=lambda c=color: change_color(c)).pack(side="left")

tk.Button(app, text="Clear", width=8, command=clear_canvas).pack(side="left")

# Bind mouse events to canvas
canvas.bind("<Button-1>", start_drawing)
canvas.bind("<B1-Motion>", draw)

# Initialize the pen color
pen_color = "black"

# Initialize variables to store last mouse position
last_x, last_y = None, None

# Start the Tkinter main loop
app.mainloop()
