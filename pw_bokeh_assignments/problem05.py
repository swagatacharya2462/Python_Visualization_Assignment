from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColorBar, ColumnDataSource
from bokeh.transform import linear_cmap
import numpy as np
from bokeh.palettes import Viridis256

data_heatmap = np.random.rand(10, 10)
x = np.linspace(0, 1, 10)
y = np.linspace(0, 1, 10)
xx, yy = np.meshgrid(x, y)

# Flatten the arrays for plotting
xx_flat = xx.flatten()
yy_flat = yy.flatten()
values = data_heatmap.flatten()

# Create a ColumnDataSource
source = ColumnDataSource(data={'x': xx_flat, 'y': yy_flat, 'value': values})

# Create a figure
p = figure(title="Heatmap", x_axis_label='X', y_axis_label='Y', tools="hover,pan,box_zoom,reset")

# Create a color mapper using the data range
color_mapper = linear_cmap(field_name='value', palette=Viridis256, low=values.min(), high=values.max())

# Plot rectangles (heatmap cells)
p.rect(x='x', y='y', width=0.1, height=0.1, source=source,
       color=color_mapper, line_color=None)

# Add color bar
color_bar = ColorBar(color_mapper=color_mapper['transform'], width=8, location=(0, 0))
p.add_layout(color_bar, 'right')

show(p)
