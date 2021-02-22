import pandas as pd

dict_data = {'c': [1, 2, 3, ], 'c1': [4, 5, 6], 'c2': [
    7, 8, 9], 'c3': [10, 11, 12], 'c4': [13, 14, 15]}

df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
print('\n')
#     c  c1  c2  c3  c4
# r0  1   4   7  10  13
# r1  2   5   8  11  14
# r2  3   6   9  12  15
[]
ndf = df.sort_values(by='c1', ascending=False)
print(ndf)
#     c  c1  c2  c3  c4
# r2  3   6   9  12  15
# r1  2   5   8  11  14
# r0  1   4   7  10  13
