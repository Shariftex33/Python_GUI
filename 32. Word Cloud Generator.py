# Importing required libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Sample text data (you can change this to your own text)
text_data = "Python is an amazing programming language. It's versatile, powerful, and beginner-friendly. Python can be used for web development, data analysis, machine learning, and more."

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)

# Display the Word Cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Hide the axis
plt.show()
