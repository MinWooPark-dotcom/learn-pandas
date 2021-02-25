# -*- coding: utf-8 -*-

import pandas as pd

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

# 데이터프레임 df의 내용을 일부 확인
print(df.head())     # 처음 5개의 행
print('\n')
print(df.tail())     # 마지막 5개의 행

# df의 모양과 크기 확인: (행의 개수, 열의 개수)를 투플로 반환
print(df.shape)
print('\n')

# 데이터프레임 df의 내용 확인
print(df.info())
print('\n')

# 데이터프레임 df의 자료형 확인
print(df.dtypes)
print('\n')

# 시리즈(mog 열)의 자료형 확인
print(df.mpg.dtypes)
print('\n')

# 데이터프레임 df의 기술통계 정보 확인
print(df.describe())
print('\n')
print(df.describe(include='all'))

#! print(df.head()): 처음 5개의 행
#  mpg  cylinders  displacement horsepower  weight  acceleration  model year  origin                       name
# 0  18.0          8         307.0      130.0  3504.0          12.0          70       1  chevrolet chevelle malibu
# 1  15.0          8         350.0      165.0  3693.0          11.5          70       1          buick skylark 320
# 2  18.0          8         318.0      150.0  3436.0          11.0          70       1         plymouth satellite
# 3  16.0          8         304.0      150.0  3433.0          12.0          70       1              amc rebel sst
# 4  17.0          8         302.0      140.0  3449.0          10.5          70       1                ford torino

#! print(df.tail()): 마지막 5개의 행
#       mpg  cylinders  displacement horsepower  weight  acceleration  model year  origin             name
# 393  27.0          4         140.0      86.00  2790.0          15.6          82       1  ford mustang gl
# 394  44.0          4          97.0      52.00  2130.0          24.6          82       2        vw pickup
# 395  32.0          4         135.0      84.00  2295.0          11.6          82       1    dodge rampage
# 396  28.0          4         120.0      79.00  2625.0          18.6          82       1      ford ranger
# 397  31.0          4         119.0      82.00  2720.0          19.4          82       1       chevy s-10

#! print(df.shape): df의 모양과 크기 확인 (행의 개수, 열의 개수)를 투플로 반환
# (398, 9)

#! print(df.info()): 데이터프레임 df의 내용 확인
# <class 'pandas.core.frame.DataFrame'> #! 클래스 유형
# RangeIndex: 398 entries, 0 to 397 #! 행 인덱스 구성
# Data columns (total 9 columns): #! 열에 관한 정보
#  #   Column        Non-Null Count  Dtype #! 열 이름 / 데이터 개수 / 자료형
# ---  ------        --------------  -----
#  0   mpg           398 non-null    float64
#  1   cylinders     398 non-null    int64
#  2   displacement  398 non-null    float64
#  3   horsepower    398 non-null    object
#  4   weight        398 non-null    float64
#  5   acceleration  398 non-null    float64
#  6   model year    398 non-null    int64
#  7   origin        398 non-null    int64
#  8   name          398 non-null    object
# dtypes: float64(4), int64(3), object(2) #! 자료형
# memory usage: 28.1+ KB #! 메모리 사용량
# None #! df요약 후 None반환


#! print(df.dtypes): 데이터프레임 df의 자료형 확인
# mpg             float64
# cylinders         int64
# displacement    float64
# horsepower       object
# weight          float64
# acceleration    float64
# model year        int64
# origin            int64
# name             object
# dtype: object


#! print(df.mpg.dtypes): 시리즈(mog 열)의 자료형 확인, 특정 열만 선택 가능
# float64

#! print(df.describe()): 데이터프레임 df의 산술 데이터를 갖는 열에 대한 기술통계 정보 확인,
#               mpg   cylinders  displacement       weight  acceleration  model year      origin
# count  398.000000  398.000000    398.000000   398.000000    398.000000  398.000000  398.000000
# mean    23.514573    5.454774    193.425879  2970.424623     15.568090   76.010050    1.572864
# std      7.815984    1.701004    104.269838   846.841774      2.757689    3.697627    0.802055
# min      9.000000    3.000000     68.000000  1613.000000      8.000000   70.000000    1.000000
# 25%     17.500000    4.000000    104.250000  2223.750000     13.825000   73.000000    1.000000
# 50%     23.000000    4.000000    148.500000  2803.500000     15.500000   76.000000    1.000000
# 75%     29.000000    8.000000    262.000000  3608.000000     17.175000   79.000000    2.000000
# max     46.600000    8.000000    455.000000  5140.000000     24.800000   82.000000    3.000000

#! print(df.describe(include='all')): 산술 데이터가 아닌 열에 대한 정보를 포함하고 싶을 때는, inclued='all' 옵션 사용
#                mpg   cylinders  displacement horsepower       weight  acceleration  model year      origin        name
# count   398.000000  398.000000    398.000000        398   398.000000    398.000000  398.000000  398.000000         398
# unique         NaN         NaN           NaN         94          NaN           NaN         NaN         NaN         305
# top            NaN         NaN           NaN      150.0          NaN           NaN         NaN         NaN  ford pinto
# freq           NaN         NaN           NaN         22          NaN           NaN         NaN         NaN           6
# mean     23.514573    5.454774    193.425879        NaN  2970.424623     15.568090   76.010050    1.572864         NaN
# std       7.815984    1.701004    104.269838        NaN   846.841774      2.757689    3.697627    0.802055         NaN
# min       9.000000    3.000000     68.000000        NaN  1613.000000      8.000000   70.000000    1.000000         NaN
# 25%      17.500000    4.000000    104.250000        NaN  2223.750000     13.825000   73.000000    1.000000         NaN
# 50%      23.000000    4.000000    148.500000        NaN  2803.500000     15.500000   76.000000    1.000000         NaN
# 75%      29.000000    8.000000    262.000000        NaN  3608.000000     17.175000   79.000000    2.000000         NaN
# max      46.600000    8.000000    455.000000        NaN  5140.000000     24.800000   82.000000    3.000000         NaN
