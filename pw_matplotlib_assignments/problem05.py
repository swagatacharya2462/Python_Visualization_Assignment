# Show a pie chart to represent the percentage distribution of different sections in the array 'sections'.
# sections = ['Section A', 'Section B', 'Section C', 'Section D']
# sizes = [25, 30, 15, 30]


import matplotlib.pyplot as plt

sections = ['Section A', 'Section B', 'Section C', 'Section D']
sizes = [25, 30, 15, 30]

plt.pie(sizes, labels=sections, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Percentage Distribution of Sections')
plt.show()
