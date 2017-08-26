import pygal
from pygal.style import LightColorizedStyle as LCS
from pygal.style import LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Python Projects'
chart.x_labels = ['awesome-python', 'httpie', 'thefuck']

plot_dicts = [
        {'value': 37629, 'label': 'Description of awesome-pythn'},
        {'value': 31064, 'label': 'Description of httpie'},
        {'value': 29695, 'label': 'Description of thefuck'},
        ]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')
