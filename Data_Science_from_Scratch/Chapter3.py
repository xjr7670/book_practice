# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from collections import Counter
import matplotlib.pyplot as plt
import matplotlib.font_manager as ftmng

plt.style.use('ggplot')
font_path = "/usr/share/fonts/adobe-source-han-sans-cn/SourceHanSansCN-Regular.otf"
myfont = ftmng.FontProperties(fname=font_path)

def line_chart():
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14598.3]
    
    # 创建一幅线图,X轴是年份,Y轴是GDP
    plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
    
    # 添加一个标题
    plt.title(u"名义GDP", fontproperties=myfont)
    
    # 给Y轴加标记
    plt.ylabel(u"十亿美元", fontproperties=myfont)
    plt.show()
    

def bar_chart():
    movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
    num_oscars = [5, 11, 3, 8, 10]
    
    # 条形的默认宽度是0.8，因此对左侧坐标加上0.1
    # 这样每个条形就放置在中心了
    xs = [i + 0.1 for i, _ in enumerate(movies)]
    
    # 使用左侧X坐标[xs]和高度[num_oscars]画条形图
    plt.bar(xs, num_oscars)
    
    # 给每条柱添加标记
    for x, n in zip(xs, num_oscars):
        plt.annotate(n, xy=(x, n), xytext=(0, +5), textcoords='offset points')
    plt.ylabel(u'所获奥斯卡金像奖数量', fontproperties=myfont)
    plt.title(u'我最喜爱的电影', fontproperties=myfont)
    
    # 使用电影的名字标记X轴，位置在X轴上条形的中心
    plt.xticks([i + 0.1 for i, _ in enumerate(movies)], movies)
    plt.show()
    

def bar_chart2():
    grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
    decile = lambda grade: grade // 10 * 10
    histogram = Counter(decile(grade) for grade in grades)
    
    # 给每个条形设置正确的高度
    # 每个条形的宽度设置为8
    plt.bar([x for x in histogram.keys()], histogram.values(), 8)
    # x轴聚会从－5到105，Y轴取值从0到5
    plt.axis([-5, 105, 0, 5])
    
    # X轴标记不0，10，20，。。。 100
    plt.xticks([10 * i for i in range(11)])
    plt.xlabel("十分相", fontproperties=myfont)
    plt.ylabel("学生数", fontproperties=myfont)
    plt.title("考试分数分页图", fontproperties=myfont)
    plt.show()
    

def wrong_ex():
    mentions = [500, 505]
    years = [2013, 2014]
    
    plt.bar(years, mentions, 0.8)
    plt.xticks(years)
    plt.ylabel("听到有人提及'数据科学'的次数", fontproperties=myfont)
    
    plt.axis([2012.5, 2014.5, 499, 506])
    plt.title("快看如此'巨大'的增长！", fontproperties=myfont)
    plt.show()
    
def correct_ex():
    mentions = [500, 505]
    years = [2013, 2014]
    
    plt.bar(years, mentions, 0.8)
    plt.xticks(years)
    plt.ylabel("听到有人提及'数据科学'的次数", fontproperties=myfont)
    
    plt.axis([2012.5, 2014.5, 0, 550])
    plt.title("增长不那么巨大了", fontproperties=myfont)
    plt.show()
    
    
def line_chart2():
    variance = [2 ** x for x in range(1, 9)]
    bias_squared = sorted(variance, reverse=True)
    total_error = [x + y for x, y in zip(variance, bias_squared)]
    xs = [i for i, _ in enumerate(variance)]
    
    plt.plot(xs, variance, 'g-', label='variance')
    plt.plot(xs, bias_squared, 'r-', label='bias^2')
    plt.plot(xs, total_error, 'b:', label='total error')
    plt.annotate("key point", xy=(3.5, 25), xytext=(0, 50), \
                 textcoords="offset points", arrowprops={"width": 5})
    plt.legend(loc=9)
    plt.xlabel("模型复杂度", fontproperties=myfont)
    plt.title("偏差－方差权衡图", fontproperties=myfont)
    plt.show()


def scatter_chart():
    friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
    minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    
    plt.scatter(friends, minutes)
    
    for label, friend_count, minute_count in zip(labels, friends, minutes):
        plt.annotate(label, \
                     xy=(friend_count, minute_count), \
                     xytext=(5, -5), \
                     textcoords='offset points')
    plt.title("日分钟数与朋友数", fontproperties=myfont)
    plt.xlabel("朋友数", fontproperties=myfont)
    plt.ylabel("花在网站上的日分钟数", fontproperties=myfont)
    plt.show()
        

    
# line_chart()
#bar_chart()
#bar_chart2()
#wrong_ex()
#correct_ex()
line_chart2()
#scatter_chart()