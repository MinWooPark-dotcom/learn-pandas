import pandas as pd

exam_data = {'이름': ['서준', '우현', '인아'],
             '수학': [90, 80, 70], '영어': [98, 89, 95],
             '음악': [85, 95, 100], '체육': [100, 90, 90]}

df = pd.DataFrame(exam_data)

# '이름' 열을 새로운 인덱스로 지정하고, df 객체에 변경 사항 반영
df.set_index('이름', inplace=True)
print(df)
print('\n')
#     수학  영어   음악   체육
# 이름
# 서준  90  98   85  100
# 우현  80  89   95   90
# 인아  70  95  100   90

a = df.loc['서준', '음악']
print(a)  # 85
print('\n')
# 음악     85
# 체육    100
# Name: 서준, dtype: int64

b = df.iloc[0, 2]
print(b)  # 85
print('\n')
# 음악     85
# 체육    100
# Name: 서준, dtype: int64

c = df.loc['서준', ['음악', '체육']]
print(c)
print('\n')
# 음악     85
# 체육    100
# Name: 서준, dtype: int64

d = df.iloc[0, [2, 3]]
print(d)
print('\n')
# 음악     85
# 체육    100
# Name: 서준, dtype: int64

e = df.loc['서준', '음악': '체육']
print(e)
print('\n')
# 음악     85
# 체육    100
# Name: 서준, dtype: int64

f = df.iloc[0, 2:]
print(f)
# 음악     85
# 체육    100
# Name: 서준, dtype: int64

g = df.loc[['서준', '우현'], ['음악', '체육']]
print(g)
#     음악   체육
# 이름
# 서준  85  100
# 우현  95   90

h = df.iloc[[0, 1], [2, 3]]
print(h)
#     음악   체육
# 이름
# 서준  85  100
# 우현  95   90

i = df.loc['서준':'우현', '음악':'체육']
print(i)
#     음악   체육
# 이름
# 서준  85  100
# 우현  95   90

j = df.iloc[0:2, 2:]
print(j)
#     음악   체육
# 이름
# 서준  85  100
# 우현  95   90
