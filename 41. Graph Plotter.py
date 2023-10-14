import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create the main application window
root = tk.Tk()
root.title("Graph Plotter")

# Function to plot the graph
def plot_graph():
    expression = entry.get()  # Get the user-entered expression
    try:
        x = range(-10, 11)  # Define the x-axis range
        y = [eval(expression.replace('x', str(i))) for i in x]  # Calculate y values
        ax.clear()  # Clear previous plot
        ax.plot(x, y)  # Plot the graph
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.set_title("Function: " + expression)
        canvas.draw()
    except Exception as e:
        result_label.config(text="Error: " + str(e))

# Create a label and an entry for the user to enter a function
label = ttk.Label(root, text="Enter a function (e.g., x**2 + 2*x - 3):")
label.pack()

entry = ttk.Entry(root)
entry.pack()

# Create a button to trigger the graph plotting
plot_button = ttk.Button(root, text="Plot Graph", command=plot_graph)
plot_button.pack()

# Create a Matplotlib figure for the graph
fig = Figure(figsize=(6, 4))
ax = fig.add_subplot(111)

# Create a Matplotlib canvas for Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Create a label to display errors
result_label = ttk.Label(root, text="", foreground="red")
result_label.pack()

root.mainloop()
