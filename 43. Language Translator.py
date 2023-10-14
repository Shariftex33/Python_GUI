import tkinter as tk
from tkinter import ttk
from googletrans import Translator

def translate_text():
    text_to_translate = entry.get()
    translator = Translator()
    translated_text = translator.translate(text_to_translate, src=source_lang.get(), dest=destination_lang.get())
    result_label.config(text=f"Translation: {translated_text.text}")

# Create the main application window
root = tk.Tk()
root.title("Language Translator")

# Create and set labels
label1 = ttk.Label(root, text="Enter text to translate:")
label1.pack()

# Create a bigger text box for user input
entry = tk.Text(root, height=5, width=40)  # Adjust the height and width as needed
entry.pack()

# Create and set source language dropdown
source_label = ttk.Label(root, text="Select source language:")
source_label.pack()
source_lang = ttk.Combobox(root, values=['en', 'es', 'fr', 'de', 'ja', 'ko'])
source_lang.set('en')
source_lang.pack()

# Create and set destination language dropdown
destination_label = ttk.Label(root, text="Select destination language:")
destination_label.pack()
destination_lang = ttk.Combobox(root, values=['en', 'es', 'fr', 'de', 'ja', 'ko'])
destination_lang.set('es')
destination_lang.pack()

# Create a translate button
translate_button = ttk.Button(root, text="Translate", command=translate_text)
translate_button.pack()

# Create a label for displaying the translation result
result_label = ttk.Label(root, text="")
result_label.pack()

# Start the main application loop
root.mainloop()
