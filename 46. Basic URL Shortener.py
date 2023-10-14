import tkinter as tk
import pyshorteners

# Function to shorten the URL and copy to clipboard
def shorten_url():
    original_url = input_entry.get()
    
    # Check if the URL is empty
    if not original_url:
        result_label.config(text="Please enter a URL", fg="red")
    else:
        # Create a Shortener object
        s = pyshorteners.Shortener()
        shortened_url = s.tinyurl.short(original_url)
        
        # Display the shortened URL
        result_label.config(text=f"Shortened URL: {shortened_url}", fg="green")
        
        # Copy the shortened URL to the clipboard
        window.clipboard_clear()
        window.clipboard_append(shortened_url)
        window.update()

# Create the main window
window = tk.Tk()
window.title("URL Shortener")

# Create and place input label and entry
input_label = tk.Label(window, text="Enter the URL:")
input_label.pack()
input_entry = tk.Entry(window, width=40)
input_entry.pack()

# Create and place shorten button
shorten_button = tk.Button(window, text="Shorten", command=shorten_url)
shorten_button.pack()

# Create and place result label
result_label = tk.Label(window, text="", fg="black")
result_label.pack()

# Start the main loop
window.mainloop()
