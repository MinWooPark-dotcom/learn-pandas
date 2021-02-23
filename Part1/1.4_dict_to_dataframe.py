import pandas as pd

dict_data = {'c0': [1, 2, 3], 'c1': [4, 5, 6], 'c2': [
    7, 8, 9], 'c3': [10, 11, 12], 'c4': [13, 14, 15]}

df = pd.DataFrame(dict_data)

print(type(df))
print('\n')
print(df)

# <class 'pandas.core.frame.DataFrame'>


#    c0  c1  c2  c3  c4
# 0   1   4   7  10  13
# 1   2   5   8  11  14
# 2   3   6   9  12  15
