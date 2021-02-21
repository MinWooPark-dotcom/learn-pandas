import pandas as pd

dict_data = {'a': 1, 'b': 2, 'c': 3}

sr = pd.Series(dict_data)

print(type(sr))  # <class 'pandas.core.series.Series'>

print('\n')

print(sr)
# a    1
# b    2
# c    3
# dtype: int64
