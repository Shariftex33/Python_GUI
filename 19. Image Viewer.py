import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Image Viewer")

# Create a canvas to display the image
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Function to open and display an image
def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")])
    if file_path:
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.image = photo

# Create an "Open Image" button
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack()

# Create an "Exit" button to close the application
exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack()

# Start the Tkinter main loop
root.mainloop()
