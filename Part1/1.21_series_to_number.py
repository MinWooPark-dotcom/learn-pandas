import pandas as pd

student1 = pd.Series({'국어': 100, '영어': 80, '수학': 90})
print(student1)
print('\n')
# 국어    100
# 영어     80
# 수학     90
# dtype: int64

percentage = student1/200

print(percentage)
print('\n')
print(type(percentage))
# 국어    0.50
# 영어    0.40
# 수학    0.45
# dtype: float64


# <class 'pandas.core.series.Series'>
