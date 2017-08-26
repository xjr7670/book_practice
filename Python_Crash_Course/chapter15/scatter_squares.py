import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# s表示点大小
# edgecolor表示轮廓颜色
# c表示点颜色
# p1t.scatter(x_values, y_values, s=40, edgecolor='none', c='red')
 
# cmap设置颜色映射，数据从小到大，则颜色由浅变深
# 这里要设置点颜色c=y_values
plt.scatter(x_values, y_values, s=40, edgecolor='none', c=y_values, cmap=plt.cm.Blues)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis="both", which="major", labelsize=8)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])
plt.show()
