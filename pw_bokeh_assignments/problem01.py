from bokeh.plotting import figure, show
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

p = figure(title="Sine Wave", x_axis_label='X', y_axis_label='Y')
p.line(x, y, legend_label="Sine Wave", line_width=2)

show(p)
