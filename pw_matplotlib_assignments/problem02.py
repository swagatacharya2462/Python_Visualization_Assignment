# Generate a line plot to visualize the trend of values for the given data.
# data = np.array([3, 7, 9, 15, 22, 29, 35])


import numpy as np
import matplotlib.pyplot as plt

data = np.array([3, 7, 9, 15, 22, 29, 35])
plt.plot(data)
plt.title('Trend of Values')
plt.xlabel('Index')
plt.ylabel('Value')
plt.show()
