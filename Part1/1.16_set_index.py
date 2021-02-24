import pandas as pd

exam_data = {'이름': ['서준', '우현', '인아'],
             '수학': [90, 80, 70],
             '영어': [98, 89, 95],
             '음악': [85, 95, 100],
             '체육': [100, 90, 90]}

df = pd.DataFrame(exam_data)
print(df)
print('\n')

#    이름  수학  영어   음악   체육
# 0  서준  90  98   85  100
# 1  우현  80  89   95   90
# 2  인아  70  95  100   90

# 특정 열(column)을 데이터프레임의 행 인덱스(index)로 설정
ndf = df.set_index(['이름'])
print(ndf)
print('\n')
# 수학  영어   음악   체육
# 이름
# 서준  90  98   85  100
# 우현  80  89   95   90
# 인아  70  95  100   90


ndf2 = ndf.set_index('음악')
print(ndf2)
print('\n')
# 수학  영어   체육
# 음악
# 85   90  98  100
# 95   80  89   90
# 100  70  95   90


ndf3 = ndf.set_index(['수학', '음악'])
print(ndf3)
#         영어   체육
# 수학 음악
# 90 85   98  100
# 80 95   89   90
# 70 100  95   90

# ! my

exam_data = {'이름': ['김코딩', '박해커', '최고수'],
             '언어': ['JS', 'Python', 'C'],
             '경력': ['1년', '2년', '3년'],
             '취미': ['걷기', '독서', '등산'],
             '특기': ['양궁', '축구', '노래']}

df = pd.DataFrame(exam_data)
print(df)
print('\n')

ndf = df.set_index(['이름'])
print(ndf)
print('\n')

ndf2 = df.set_index(['언어'])
print(ndf2)
print('\n')

#     이름      언어  경력  취미  특기
# 0  김코딩      JS  1년  걷기  양궁
# 1  박해커  Python  2년  독서  축구
# 2  최고수       C  3년  등산  노래


#          언어  경력  취미  특기
# 이름
# 김코딩      JS  1년  걷기  양궁
# 박해커  Python  2년  독서  축구
# 최고수       C  3년  등산  노래


#          이름  경력  취미  특기
# 언어
# JS      김코딩  1년  걷기  양궁
# Python  박해커  2년  독서  축구
# C       최고수  3년  등산  노래
