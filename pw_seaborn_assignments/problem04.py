# Generate a dataset with categories and numerical values. Visualize the distribution of a numerical variable across different categories.

import matplotlib.pyplot as plt
import numpy as np

categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
values = np.random.randint(10, 100, size=5)

plt.bar(categories, values, color='orange')
plt.title('Distribution of Numerical Values Across Categories')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()
