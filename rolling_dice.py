from plotly.graph_objs import Bar, Layout
from plotly import offline

from dice import Dice

die = Dice()

results = []
num_rolls = 1000
for i in range(num_rolls):
	results.append(die.roll())

frequencies = [0 for _ in range(die.sides)]
for i in range(1, die.sides+1):
	frequencies[i-1] = results.count(i)

x_values = list(range(1, die.sides+1))
data = [Bar(x=x_values, y=frequencies)] # histogram bars

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title=f'Result of rolling d{die.sides} {num_rolls} times',
	xaxis=x_axis_config, yaxis=y_axis_config) # layout settings

offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')

