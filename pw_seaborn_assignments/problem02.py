# Generate a dataset of random numbers. Visualize the distribution of a numerical variable.

import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=30, edgecolor='black')
plt.title('Histogram: Distribution of a Numerical Variable')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
