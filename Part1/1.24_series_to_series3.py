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

sr_add = student1.add(student2, fill_value=0)
sr_sub = student1.sub(student2, fill_value=0)
sr_mul = student1.mul(student2, fill_value=0)
sr_div = student1.div(student2, fill_value=0)

result = pd.DataFrame([sr_add, sr_sub, sr_mul, sr_div],
                      index=['덧셈', '뺄셈', '곱셈', '나눗셈'])

print(result)
# 국어        수학    영어
# 덧셈   90.0   170.000  80.0
# 뺄셈 - 90.0    10.000  80.0
# 곱셈    0.0  7200.000   0.0
# 나눗셈   0.0     1.125   inf
