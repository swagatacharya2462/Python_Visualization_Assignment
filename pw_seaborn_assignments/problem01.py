# Create a scatter plot to visualize the relationship between two variables, by generating a synthetic dataset.

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
x = np.random.rand(100)
y = 2 * x + np.random.normal(0, 0.1, 100)

plt.scatter(x, y)
plt.title('Scatter Plot: Relationship Between Two Variables')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.show()
