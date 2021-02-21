import pandas as pd

list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data)
print(sr)

# index Data Value

# 0    2019-01-02
# 1          3.14
# 2           ABC
# 3           100
# 4          True
# dtype: object

idx = sr.index
val = sr.values
print(idx)
print(val)

# RangeIndex(start=0, stop=5, step=1)
# ['2019-01-02' 3.14 'ABC' 100 True]
