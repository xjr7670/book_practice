```python
>>> import pandas as pd
>>> import numpy as np

>>> print(np.__version__), print(pd.__version__)
1.14.3
0.23.0
```

## Series

### 从 numpy 数组创建，并指定索引值

```python
>>> s1 = pd.Series(np.random.rand(4), index=['a', 'b', 'c', 'd'])
>>> s1
a    0.390501
b    0.460804
c    0.176490
d    0.465754
dtype: float64
```

如果没有指定索引，则默认会创建从 0 到 N-1 的数组作为索引值，这里的 N 是 Series 的长度（即它所包含的元素个数）：

```python
>>> s2 = pd.Series(np.random.rand(4))
>>> s2
0    0.210839
1    0.979725
2    0.862411
3    0.780342
dtype: float64
```

**通过索引访问元素**

```python
>>> s1['c']
0.176490
>>> # 也可以给元素赋值（修改元素值）
>>> s1['c'] = 3.14
>>> # 同时访问多个元素
>>> s1[['c', 'a', 'b']]
c    3.140000
a    0.390501
b    0.460804
dtype: float64
```

### 从字典中创建

字典中的键将会作为索引值，字典中的值将会作为元素值：

```python
>>> s3 = pd.Series({'001': 'Nam', '002': 'Mary', '003': 'Peter'})
>>> s3
001      Nam
002     Mary
003    Peter
dtype: object
```

从字典中创建 Series 时，也可以自定义索引值或者是添加过滤（即指定只从字典中的某几个键进行创建）。当自定义的**索引值**不存在于字典中的**键**时，默认会用`NaN`来作为这个索引的值：

```python
>>> s4 = pd.Series({'001': 'Nam', '002': 'Mary', '003': 'Peter'}, index=['002', '001', '024', '065'])
>>> s4
002    Mary
001     Nam
024     NaN
065     NaN
dtype: object
```

可以看到，由于传进来的字典中只有`001`和`002`这两个键，于是创建的 Series 中只保留了这两项，而`024`和`065`对应的值则是`NaN`。

**判断元素是否为空**

```python
>>> pd.isnull(s4)
002    False
001    False
024     True
065     True
dtype: bool
```

### 从标量值创建

```python
>>> s5 = pd.Series(2.71, index=['x', 'y'])
>>> s5
x    2.71
y    2.71
dtype: float64
```

可以理解为：指定多少个索引，创建的 Series 中就会包含多少个相同值的元素

**相加**

这里主要演示的是，Pandas 会自动根据索引来对齐两个 Series 然后再进行数学运算

```python
>>> s6 = pd.Series(np.array([2.71, 3.14]), index=['z', 'y'])
>>> s6
z    2.71
y    3.14
dtype: float64
>>> s5 + s6
x     NaN
y    5.85
z     NaN
dtype: float64
```

## DataFrame

### 从字典中创建

```python
>>>  data = {'Year': [2000, 2005, 2010, 2014],
                     'Median_Age': [24.2, 26.4, 28.5, 30.3],
                     'Density': [244, 256, 268, 279]}
>>> df1 = pd.DataFrame(data)
>>> df1
   Year  Median_Age  Density
0  2000        24.2      244
1  2005        26.4      256
2  2010        28.5      268
3  2014        30.3      279
```

默认顺序是传进去的字典的顺序，也可以根据列名（column）进行指定：

```python
>>> df2 = pd.DataFrame(data, columns=['Year', 'Density', 'Median_Age'])
>>> df2
   Year  Density  Median_Age
0  2000      244        24.2
1  2005      256        26.4
2  2010      268        28.5
3  2014      279        30.3
```

也可以像 Series 那样指定索引值：

```python
>>> df3 = pd.DataFrame(data, columns=['Year', 'Density', 'Median_Age'], index=['a', 'b', 'c', 'd'])
>>> df3.index
Index(['a', 'b', 'c', 'd'], dtype='object')
```

### 直接从嵌套的列表中创建

```python
>>> df4 = pd.DataFrame([
         ['Peter', 16, 'pupil', 'TN', 'M', None],
         ['Mary', 21, 'student', 'SG', 'F', None],
         ['Nam', 22, 'student', 'HN', 'M', None],
         ['Mai', 31, 'nurse', 'SG', 'F', None],
         ['John', 28, 'laywer', 'SG', 'M', None]],
         columns=['name', 'age', 'careet', 'province', 'sex', 'award'])
>>> # 有两种方式可以取到某一列。前提是这个列名不包含空格等特殊字符
>>> # 如果包含空格，则只能使用第二种方式
>>> df4.name
0    Peter
1     Mary
2      Nam
3      Mai
4     John
Name: name, dtype: object
>>> df4['name']
0    Peter
1     Mary
2      Nam
3      Mai
4     John
Name: name, dtype: object
>>> # 修改某一列（整列）的内容
>>> df4['award'] = None
    name  age   careet province sex award
0  Peter   16    pupil       TN   M  None
1   Mary   21  student       SG   F  None
2    Nam   22  student       HN   M  None
3    Mai   31    nurse       SG   F  None
4   John   28   laywer       SG   M  None
```

### 从文件中生成

**从 CSV 文件中生成**

假设有名为 person.csv 的文件内容如下：

```
name,age,career,province,sex
Peter,16,pupil,TN,M
Mary,21,student,SG,F
Nam,22,student,HN,M
Mai,31,nurse,SG,F
John,28,lawer,SG,M
```

可使用`read_csv`来进行读取，直接生成 DataFrame

```python
>>> df4 = pd.read_csv('person.csv')
>>> df4
    name  age   career   province sex
0   Peter   16    pupil       TN        M
1    Mary   21    student   SG       F
2    Nam   22    student   HN       M
3      Mai   31    nurse      SG       F
4    John   28    lawer      SG       M
```

0.23.0 版本的 pandas 中的`read_csv`函数有 49 个参数，分别有不同的用途，比如指定分隔符、指定哪一行做为列名、跳过开头几行、忽略末尾几行等等。可以通过查看文档了解。