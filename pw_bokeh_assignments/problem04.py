from bokeh.plotting import figure, show
from bokeh.io import output_file
import numpy as np

data_hist = np.random.randn(1000)
hist, edges = np.histogram(data_hist, bins=30)

p = figure(title="Histogram", x_axis_label='Value', y_axis_label='Frequency', tools="pan,box_zoom,reset")

p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color="skyblue", line_color="white", alpha=0.7)

show(p)
