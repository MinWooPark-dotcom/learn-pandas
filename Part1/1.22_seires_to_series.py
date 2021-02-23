import pandas as pd

student1 = pd.Series({'국어': 100, '영어': 80, '수학': 90})
student2 = pd.Series({'수학': 80, '국어': 90, '영어': 80})
print(student1)
print('\n')
# 국어    100
# 영어     80
# 수학     90
# dtype: int64

print(student2)
print('\n')
# 수학    80
# 국어    90
# 영어    80
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
# 국어        수학      영어
# 덧셈    190.000000   170.000   160.0
# 뺄셈     10.000000    10.000     0.0
# 곱셈   9000.000000  7200.000  6400.0
# 나눗셈     1.111111     1.125     1.0
