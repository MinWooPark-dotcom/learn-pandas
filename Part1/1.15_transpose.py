import pandas as pd

exam_data = {'이름': ['서준', '우현', '인아'],
             '수학': [90, 80, 70],
             '영어': [98, 89, 95],
             '음악': [85, 95, 100],
             '체육': [100, 90, 90]}

df = pd.DataFrame(exam_data)

print(df)
print('\n')
# 이름  수학  영어   음악   체육
# 0  서준  90  98   85  100
# 1  우현  80  89   95   90
# 2  인아  70  95  100   90


# 데이터프레임 df를 전치하기 (메서드 활용)
df = df.transpose()
print(df)
print('\n')
#       0   1    2
# 이름   서준  우현   인아
# 수학   90  80   70
# 영어   98  89   95
# 음악   85  95  100
# 체육  100  90   90


# 데이터프레임 df를 다시 전치하기 (클래스 속성 활용)
df = df.T
print(df)
# 이름  수학  영어   음악   체육
# 0  서준  90  98   85  100
# 1  우현  80  89   95   90
# 2  인아  70  95  100   90

# ! my

exam_data = {'이름': ['김코딩', '박해커', '최고수'],
             '언어': ['JS', 'Python', 'C'],
             '경력': ['1년', '2년', '3년'],
             '취미': ['걷기', '독서', '등산'],
             '특기': ['양궁', '축구', '노래']}

df = pd.DataFrame(exam_data)
print(df)
print('\n')

df.transpose()
print(df)
print('\n')

df.T
print(df)
print('\n')

#     이름      언어  경력  취미  특기
# 0  김코딩      JS  1년  걷기  양궁
# 1  박해커  Python  2년  독서  축구
# 2  최고수       C  3년  등산  노래


#     이름      언어  경력  취미  특기
# 0  김코딩      JS  1년  걷기  양궁
# 1  박해커  Python  2년  독서  축구
# 2  최고수       C  3년  등산  노래


#     이름      언어  경력  취미  특기
# 0  김코딩      JS  1년  걷기  양궁
# 1  박해커  Python  2년  독서  축구
# 2  최고수       C  3년  등산  노래
