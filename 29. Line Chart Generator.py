import matplotlib.pyplot as plt

# Data (you can change this data for different results)
x_values = [1, 2, 3, 4, 5]
y_values = [10, 15, 7, 12, 8]

# Create a line chart
plt.plot(x_values, y_values, marker='o', linestyle='-')

# Customize chart labels and title
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Simple Line Chart')

# Show the chart
plt.grid(True)  # Add gridlines
plt.show()
