import tkinter as tk

def convert_temperature():
    celsius = float(entry.get())
    fahrenheit = (celsius * 9/5) + 32
    result_label.config(text=f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")

# Create the main application window
app = tk.Tk()
app.title("Temperature Converter")

# Create labels and entry fields
label = tk.Label(app, text="Enter temperature in Celsius:")
label.pack()

entry = tk.Entry(app)
entry.pack()

result_label = tk.Label(app, text="")
result_label.pack()

# Create a Convert button
convert_button = tk.Button(app, text="Convert", command=convert_temperature)
convert_button.pack()

# Start the main event loop
app.mainloop()
