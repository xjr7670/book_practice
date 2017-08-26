import pygal
from pygal.style import DarkSolarizedStyle
from die import Die

# 创建三个D6
die_1 = Die()
die_2 = Die()
die_3 = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(500000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

frequencies = []

max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar(style=DarkSolarizedStyle)

hist.title = "Results of rolling three D6 1000 times."
hist.x_labels = [str(i) for i in range(3, 19)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6 + D6 + D6", frequencies)
hist.render_to_file('practice_15-8.svg')
