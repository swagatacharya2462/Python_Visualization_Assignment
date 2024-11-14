# Create a scatter plot using Matplotlib to visualize the relationship between two arrays, x and y for the given data.
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y = [2, 4, 5, 7, 6, 8, 9, 10, 12, 13]


import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 5, 7, 6, 8, 9, 10, 12, 13]

plt.scatter(x, y)
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Scatter Plot of X vs Y')
plt.show()
