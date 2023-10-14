import matplotlib.pyplot as plt

# Data Points (Change these values to customize your plot)
x = [1, 2, 3, 4, 5]
y = [10, 12, 5, 8, 15]

# Scatter Plot Generation
plt.scatter(x, y, color='blue', marker='o', s=100, label='Scatter Plot')

# Customize the Plot
plt.title('Scatter Plot Generator')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend(loc='upper left')

# Display the Plot (Change this line to save the plot if needed)
plt.show()
