import matplotlib.pyplot as plt

# Sample data (change this to your own data)
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [15, 30, 10, 25]

# Create a bar chart
plt.bar(categories, values)

# Customize the chart
plt.title('Sample Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

# Display the chart
plt.show()
