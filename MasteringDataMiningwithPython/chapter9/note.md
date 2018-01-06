# 第9章 挖掘数据异常

其实这里有一部分内容是属于数据清洗的。不过也包含有一点挖掘异常数据的内容


## 用修正Z得分检测离群值

涉及的几个值：

* 中心值（均值）<br />
* 标准差<br />
* 离群值<br />

数据点与均值的标准差数称为Z得分。Z得分最大的数据点，则将其标记为一个离群值，从数据集中删除，并重复测试。这一过程被称为Grubb检验，或者最大规残差检验。


**代码理解**

计算Z得分

```
# 读入数据文件。每一行都是一个数字
with open('sloc.txt', encoding='utf-8') as f:
    data = f.readlines()
data = np.array(data, dtype=int) # 转换为numpy的序列

amax = np.amax(data, axis=0)    # 最大值
print("amax: ", amax)
amin = np.amin(data, axis=0)    # 最小值
print("amin: ", amin)
mean = np.mean(data)            # 均值
print("mean: ", mean)
median = np.median(data)        # 中位数
print("median: ", median)

sumsqdiff = np.sum(pow((data - median), 2)) # 求每个数与中位数的差的平方和
print("sumsqdiff: ", sumsqdiff)
sqrtdiff = np.sqrt(sumsqdiff)               # 再开平方
print("sqrtdiff: ", sqrtdiff)
mad = np.median(sqrtdiff)                   # 再取得它们的中位数。称为绝对中位差
print("mad: ", mad)

# 得到一个修正Z得分。
# 0.6745表示标准差的约2/3，表示大约为上、下四分位值之间距离一半的阈值
modzscore = (0.6745 * sumsqdiff) / mad      
print("Any value higher than", modzscore, "is an outlier")
```


## 用机器学习检测离群值

**代码理解**

```
# 加载数据
X1 = np.loadtxt('slocbool.txt')

# 建立EllipticEnvelope对象。contamination表示数据中被视为离群值的数据点不超过2％
ee = EllipticEnvelope(support_fraction=1., contamination=0.02)

# 设置X、Y轴的起点和终点，以及X和Y的总观测值数量，设置网络大小
xx, yy = np.meshgrid(np.linspace(0, 1500000, 542), np.linspace(0, 15000, 542))
# 用ee拟合数据
ee.fit(X1)
Z = ee.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(1)
plt.title("Outlier detection: SLOC vs BOOL")

# 画散点图
plt.scatter(X1[:, 0], X1[:, 1], color='black')
# 画椭圆
plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors='m')
plt.ylabel("count of boolean expressions")
plt.xlabel("count of source lines of code")
plt.show()
```
