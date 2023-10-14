import tkinter as tk

# Function to count words in the entered text
def count_words():
    text = input_text.get("1.0", "end-1c")  # Get text from the input Text widget
    words = text.split()  # Split text into words
    word_count = len(words)  # Count the number of words
    result_label.config(text=f"Word Count: {word_count}")

# Create the main application window
root = tk.Tk()
root.title("Word Counter")

# Create a Text widget for input
input_text = tk.Text(root, height=10, width=40)
input_text.pack()

# Create a button to trigger word counting
count_button = tk.Button(root, text="Count Words", command=count_words)
count_button.pack()

# Create a label to display the word count result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the Tkinter main loop
root.mainloop()
