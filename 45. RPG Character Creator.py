import tkinter as tk
from tkinter import Canvas, Button, Entry
from PIL import Image, ImageDraw

# Create a function to generate a digital signature
def generate_signature():
    text = entry.get()
    image = Image.new("RGB", (300, 100), "white")
    draw = ImageDraw.Draw(image)
    draw.text((10, 40), text, fill="black")
    image.save("signature.png")
    status_label.config(text="Signature created as 'signature.png'")

# Create the main window
root = tk.Tk()
root.title("Digital Signature Creator")

# Create and configure the canvas
canvas = Canvas(root, width=300, height=100, bg="white")
canvas.pack()

# Create and configure the input field
entry = Entry(root, width=30)
entry.pack(pady=10)

# Create and configure the Generate button
generate_button = Button(root, text="Generate Signature", command=generate_signature)
generate_button.pack()

# Create and configure the status label
status_label = tk.Label(root, text="", fg="green")
status_label.pack()

root.mainloop()
