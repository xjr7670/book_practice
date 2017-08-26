import matplotlib.pyplot as plt
from die import Die

# 创建两个D6
die_1 = Die()
die_2 = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(10000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
plt.bar(range(2, max_result+1), frequencies)
plt.title("Result of rolling two D6 10000 times")
plt.xlabel("Result")
plt.ylabel("Frequency of Result")
plt.legend(["D6 + D6"])
plt.show()
