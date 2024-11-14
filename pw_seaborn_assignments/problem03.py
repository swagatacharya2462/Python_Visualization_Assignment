# Create a dataset representing categories and their corresponding values. Compare different categories based on numerical values.

import matplotlib.pyplot as plt

categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
values = [15, 30, 45, 20, 60]

plt.bar(categories, values, color='skyblue')
plt.title('Comparison of Categories Based on Numerical Values')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()
