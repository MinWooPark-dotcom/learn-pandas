import pandas as pd

dict_data = {'c': [1, 2, 3], 'c1': [4, 5, 6], 'c2': [
    7, 8, 9, ], 'c3': [10, 11, 12], 'c4': [13, 14, 15]}

df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
print('\n')
#     c  c1  c2  c3  c4
# r0  1   4   7  10  13
# r1  2   5   8  11  14
# r2  3   6   9  12  15

new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf = df.reindex(new_index)
print(ndf)
print('\n')
#       c   c1   c2    c3    c4
# r0  1.0  4.0  7.0  10.0  13.0
# r1  2.0  5.0  8.0  11.0  14.0
# r2  3.0  6.0  9.0  12.0  15.0f
# r3  NaN  NaN  NaN   NaN   NaN
# r4  NaN  NaN  NaN   NaN   NaN

ndf2 = df.reindex(new_index, fill_value=0)
print(ndf2)
#     c  c1  c2  c3  c4
# r0  1   4   7  10  13
# r1  2   5   8  11  14
# r2  3   6   9  12  15
# r3  0   0   0   0   0
# r4  0   0   0   0   0