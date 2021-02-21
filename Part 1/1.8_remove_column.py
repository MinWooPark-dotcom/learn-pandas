import pandas as pd

exam_data = {'수학': [90, 80, 70], '영어': [98, 89, 95],
             '음악': [85, 95, 100], '체육': [100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print('\n')

df4 = df[:]
df4.drop('수학', axis=1, inplace=True)
print(df4)
print('\n')

df5 = df[:]
df5.drop(['영어', '음악'], axis=1, inplace=True)
print(df5)

df6 = df[:]
df6.drop(['서준'], axis=0, inplace=True)  # aixs=0 혹은 생략 시, 행 삭제
print(df6)

#     수학  영어   음악   체육
# 서준  90  98   85  100
# 우현  80  89   95   90
# 인아  70  95  100   90


#     영어   음악   체육
# 서준  98   85  100
# 우현  89   95   90
# 인아  95  100   90


#     수학   체육
# 서준  90  100
# 우현  80   90
# 인아  70   90

#     수학  영어   음악  체육
# 우현  80  89   95  90
# 인아  70  95  100  90
