# Display a bar chart to represent the frequency of each item in the given array categories.
# categories = ['A', 'B', 'C', 'D', 'E']
# values = [25, 40, 30, 35, 20]


import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [25, 40, 30, 35, 20]

plt.bar(categories, values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Frequency of Each Item in Categories')
plt.show()
