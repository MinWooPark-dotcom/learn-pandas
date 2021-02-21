import pandas as pd

tup_data = ('영인', '2010-05-01', '여', True)
sr = pd.Series(tup_data, index=['이름', '생년월일', '성별', '학생여부'])
print(sr)

# 이름              영인
# 생년월일    2010-05-01
# 성별               여
# 학생여부          True
# dtype: object

print(sr[0])  # 영인
print(sr['이름'])  # 영인
print('\n')

print(sr[[1, 2]])
print('\n')
print(sr[['생년월일', '성별']])
print('\n')
# 생년월일    2010-05-01
# 성별               여
# dtype: object


# 생년월일    2010-05-01
# 성별               여
# dtype: object

print(sr[1: 2])  # slicing은 end 미포함
print('\n')
print(sr[['생년월일', '성별']])

# 생년월일    2010-05-01
# dtype: object


# 생년월일    2010-05-01
# 성별               여
# dtype: object
