from bokeh.plotting import figure, show
from bokeh.io import output_file

fruits = ['Apples', 'Oranges', 'Bananas', 'Pears']
counts = [20, 25, 30, 35]

p = figure(x_range=fruits, title="Fruit Counts", x_axis_label='Fruit', y_axis_label='Count', toolbar_location=None)

p.vbar(x=fruits, top=counts, width=0.4, color="blue")

show(p)
