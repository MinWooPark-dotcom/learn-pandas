import pandas as pd

file_path = './read_csv_sample.csv'

df1 = pd.read_csv(file_path)
print(df1)
print('\n')

df2 = pd.read_csv(file_path, header=None)
print(df2)
print('\n')

df3 = pd.read_csv(file_path, index_col=None)
print(df3)
print('\n')

df4 = pd.read_csv(file_path, index_col='c0')
print(df4)

#    c0   c1   c2   c3
# 0   0    1    4    7
# 1   1    2    5    8
# 2   2    3    6    9


#     0    1    2    3
# 0  c0   c1   c2   c3
# 1   0    1    4    7
# 2   1    2    5    8
# 3   2    3    6    9


#    c0   c1   c2   c3
# 0   0    1    4    7
# 1   1    2    5    8
# 2   2    3    6    9


#      c1   c2   c3
# c0
# 0     1    4    7
# 1     2    5    8
# 2     3    6    9
