import pandas as pd

df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']], index=[
                  '준서', '예은'], columns=['나이', '성별', '학교'])

print(df)
print('\n')
print(df.index)
print('\n')
print(df.columns)

#     나이 성별   학교
# 준서  15  남  덕영중
# 예은  17  여  수리중


# Index(['준서', '예은'], dtype='object')


# Index(['나이', '성별', '학교'], dtype='object')
