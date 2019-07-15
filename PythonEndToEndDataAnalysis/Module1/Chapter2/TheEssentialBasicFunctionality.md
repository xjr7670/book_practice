> 接上一篇 [Pandas Series 与 DataFrame 数据创建](https://www.cnblogs.com/wuzhiblog/p/pandas_series_dataframe_basic_use.html)


## Reindexing

重索引。对应的方法为`reindex`。<br>
重索引其实等于是通过新的（指定的）索引从原来的 Series 或者 DataFrame 中获取对应的行，如果新的索引不存在于原来的对象中，则用默认值来填充，这个默认值也可以通过参数指定。

```python
>>> s2.reindex([0, 2, 'b', 3])
0    0.210839
2    0.862411
b         NaN
3    0.780342
dtype: float64
>>> df1.reindex([0, 2, 'b', 3], columns=['Density', 'Year', 'Median_Age', 'C'])
   Density    Year  Median_Age   C
0    244.0  2000.0        24.2 NaN
2    268.0  2010.0        28.5 NaN
b      NaN     NaN         NaN NaN
3    279.0  2014.0        30.3 NaN
```

