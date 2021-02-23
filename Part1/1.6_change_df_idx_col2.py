import pandas as pd

df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']], index=[
                  '준서', '예은'], columns=['나이', '성별', '학교'])

print(df)
print('\n')

df.rename(columns={'나이': '연령', '성별': '남녀', '학교': '소속'}, inplace=True)
df.rename(index={'준서': '학생1', '에은': '학생2'}, inplace=True)

print(df)

#     나이 성별   학교
# 준서  15  남  덕영중
# 예은  17  여  수리중


#      연령 남녀   소속
# 학생1  15  남  덕영중
# 예은   17  여  수리중
