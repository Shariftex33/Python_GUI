import tkinter as tk
from textblob import TextBlob

# Function to perform sentiment analysis
def analyze_sentiment():
    text = text_entry.get("1.0", "end-1c")  # Get text from the input field
    analysis = TextBlob(text)
    
    # Determine sentiment polarity (positive, neutral, negative)
    if analysis.sentiment.polarity > 0:
        sentiment_label.config(text="Sentiment: Positive")
    elif analysis.sentiment.polarity == 0:
        sentiment_label.config(text="Sentiment: Neutral")
    else:
        sentiment_label.config(text="Sentiment: Negative")

# Create the main window
root = tk.Tk()
root.title("Sentiment Analysis Dashboard")

# Create and configure GUI elements
text_label = tk.Label(root, text="Enter text for analysis:")
text_label.pack()

text_entry = tk.Text(root, height=5, width=40)
text_entry.pack()

analyze_button = tk.Button(root, text="Analyze", command=analyze_sentiment)
analyze_button.pack()

sentiment_label = tk.Label(root, text="")
sentiment_label.pack()

# Start the main loop
root.mainloop()
