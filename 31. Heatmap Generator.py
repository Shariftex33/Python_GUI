import numpy as np
import matplotlib.pyplot as plt

# Create random data for the heatmap (replace with your data)
data = np.random.rand(10, 10)

# Create a heatmap
plt.imshow(data, cmap='YlOrRd', interpolation='nearest')
plt.colorbar(label='Intensity')

# Add labels to the axes
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

# Add a title
plt.title('Heatmap Example')

# Display the heatmap
plt.show()
