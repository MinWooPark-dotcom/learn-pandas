import pandas as pd
import numpy as np

student1 = pd.Series({'국어': np.nan, '영어': 80, '수학': 90})
student2 = pd.Series({'수학': 80, '국어': 90})
print(student1)
print('\n')
# 국어     NaN
# 영어    80.0
# 수학    90.0
# dtype: float64

print(student2)
print('\n')
# 수학    80
# 국어    90
# dtype: int64

addition = student1 + student2
subtraction = student1 - student2
multiplication = student1 * student2
division = student1 / student2
print(type(division))
print('\n')
# <class 'pandas.core.series.Series' >

result = pd.DataFrame([addition, subtraction, multiplication, division],
                      index=['덧셈', '뺄셈', '곱셈', '나눗셈'])

print(result)

#      국어    수학    영어
# 덧셈  NaN   170.000 NaN
# 뺄셈  NaN    10.000 NaN
# 곱셈  NaN  7200.000 NaN
# 나눗셈 NaN     1.125 NaN
