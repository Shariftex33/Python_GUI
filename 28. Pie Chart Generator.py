import matplotlib.pyplot as plt

# Data for the pie chart (change this data to customize your chart)
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [30, 45, 15, 10]
colors = ['lightblue', 'lightcoral', 'lightgreen', 'lightsalmon']
explode = (0.1, 0, 0, 0)  # Explode the 1st slice (Category A)

# Create a pie chart
plt.figure(figsize=(8, 8))  # Set the figure size
plt.pie(values, labels=categories, colors=colors, explode=explode, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart Example')  # Set the title

# Display the chart
plt.show()
