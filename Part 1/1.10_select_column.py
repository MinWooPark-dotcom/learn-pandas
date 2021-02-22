import pandas as pd

exam_data = {'이름': ['서준', '우현', '인아'],
             '수학': [90, 80, 70], '영어': [98, 89, 95],
             '음악': [85, 95, 100], '체육': [100, 90, 90]}

df = pd.DataFrame(exam_data)
print(df)  # 데이터프레임 반환
print(type(df))
print('\n')
#    이름  수학  영어   음악   체육
# 0  서준  90  98   85  100
# 1  우현  80  89   95   90
# 2  인아  70  95  100   90
# <class 'pandas.core.frame.DataFrame' >


math1 = df['수학']  # 시리즈 반환
print(type(math1))
print('\n')
# <class 'pandas.core.series.Series' >


english = df.영어  # 시리즈 반환
print(english)
print(type(english))
print('\n')
# 0    98
# 1    89
# 2    95
# Name: 영어, dtype: int64
# <class 'pandas.core.series.Series' >

music_gym = df[['음악', '체육']]
print(music_gym)
print(type(music_gym))
print('\n')

#     음악   체육
# 0   85  100
# 1   95   90
# 2  100   90
# <class 'pandas.core.frame.DataFrame'>

math2 = df[['수학']]
print(math2)
print(type(math2))

#    수학
# 0  90
# 1  80
# 2  70
# <class 'pandas.core.frame.DataFrame'>
