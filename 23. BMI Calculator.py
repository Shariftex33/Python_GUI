import tkinter as tk

# Function to calculate BMI
def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get()) / 100  # Convert height from cm to meters
    bmi = weight / (height ** 2)
    result_label.config(text=f"Your BMI: {bmi:.2f}")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create labels
weight_label = tk.Label(root, text="Weight (kg):")
height_label = tk.Label(root, text="Height (cm):")
result_label = tk.Label(root, text="Your BMI will appear here")

# Create entry widgets
weight_entry = tk.Entry(root)
height_entry = tk.Entry(root)

# Create a calculate button
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)

# Pack widgets
weight_label.pack()
weight_entry.pack()
height_label.pack()
height_entry.pack()
calculate_button.pack()
result_label.pack()

# Start the GUI main loop
root.mainloop()
