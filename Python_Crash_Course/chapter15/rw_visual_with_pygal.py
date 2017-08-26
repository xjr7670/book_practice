import pygal
from pygal.style import LightColorizedStyle
from random_walk import RandomWalk

rw = RandomWalk(10000)
rw.fill_walk()

# 设置图例属性
my_config = pygal.Config()
my_config.show_y_guides = False
my_config.show_x_labels = False
my_config.show_y_labels = False
my_config.stroke = False
my_config.width = 1000
my_style = LightColorizedStyle()

xy_chart = pygal.XY(my_config, style=my_style)
points = zip(rw.x_values, rw.y_values)
xy_chart.add("Random Walk", list(points))
xy_chart.add("Start Point", [(rw.x_values[0], rw.y_values[0])])
xy_chart.add("End Point", [(rw.x_values[-1], rw.y_values[-1])])
xy_chart.render_to_file("rw_with_pygal.svg")
