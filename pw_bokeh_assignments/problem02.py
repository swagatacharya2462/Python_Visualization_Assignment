from bokeh.plotting import figure, show
import numpy as np
import pandas as pd

x = np.random.rand(100)
y = np.random.rand(100)
sizes = np.random.randint(5, 20, size=100)
colors = np.random.choice(['red', 'green', 'blue', 'yellow'], size=100)

data = pd.DataFrame({'x': x, 'y': y, 'sizes': sizes, 'colors': colors})

p = figure(title="Scatter Plot", x_axis_label='X', y_axis_label='Y')

p.scatter('x', 'y', size='sizes', color='colors', legend_field='colors', source=data)

show(p)
