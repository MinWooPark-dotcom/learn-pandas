import pandas as pd

exam_data = {'수학': [90, 80, 70], '영어': [98, 89, 95],
             '음악': [85, 95, 100], '체육': [100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print('\n')

#     수학  영어   음악   체육
# 서준  90  98   85  100
# 우현  80  89   95   90
# 인아  70  95  100   90

label1 = df.loc['서준']
position1 = df.iloc[0]

print(label1)
print('\n')
print(position1)

# 수학     90
# 영어     98
# 음악     85
# 체육    100
# Name: 서준, dtype: int64


# 수학     90
# 영어     98
# 음악     85
# 체육    100
# Name: 서준, dtype: int64
