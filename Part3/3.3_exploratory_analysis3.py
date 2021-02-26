# -*- coding: utf-8 -*-

import pandas as pd

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

#! 평균값
print(df.mean())
print('\n')
# mpg               23.514573
# cylinders          5.454774
# displacement     193.425879
# weight          2970.424623
# acceleration      15.568090
# model year        76.010050
# origin             1.572864
# dtype: float64

print(df['mpg'].mean())
print(df.mpg.mean())
print('\n')
# 23.514572864321615
# 23.514572864321615

print(df[['mpg', 'weight']].mean())
# mpg         23.514573
# weight    2970.424623
# dtype: float64

#! 중간값
print(df.median())
print('\n')
print(df['mpg'].median())

# 최대값
print(df.max())
print('\n')
print(df['mpg'].max())

# 최소값
print(df.min())
print('\n')
print(df['mpg'].min())

# 표준편차
print(df.std())
print('\n')
print(df['mpg'].std())

# 상관계수
print(df.corr())
print('\n')
print(df[['mpg', 'weight']].corr())


# mpg               23.0
# cylinders          4.0
# displacement     148.5
# weight          2803.5
# acceleration      15.5
# model year        76.0
# origin             1.0
# dtype: float64


# 23.0
# mpg                         46.6
# cylinders                      8
# displacement                 455
# horsepower                     ?
# weight                      5140
# acceleration                24.8
# model year                    82
# origin                         3
# name            vw rabbit custom
# dtype: object


# 46.6
# mpg                                   9
# cylinders                             3
# displacement                         68
# horsepower                        100.0
# weight                             1613
# acceleration                          8
# model year                           70
# origin                                1
# name            amc ambassador brougham
# dtype: object


# 9.0
# mpg               7.815984
# cylinders         1.701004
# displacement    104.269838
# weight          846.841774
# acceleration      2.757689
# model year        3.697627
# origin            0.802055
# dtype: float64


# 7.815984312565782
#                    mpg  cylinders  displacement    weight  acceleration  model year    origin
# mpg           1.000000  -0.775396     -0.804203 -0.831741      0.420289    0.579267  0.563450
# cylinders    -0.775396   1.000000      0.950721  0.896017     -0.505419   -0.348746 -0.562543
# displacement -0.804203   0.950721      1.000000  0.932824     -0.543684   -0.370164 -0.609409
# weight       -0.831741   0.896017      0.932824  1.000000     -0.417457   -0.306564 -0.581024
# acceleration  0.420289  -0.505419     -0.543684 -0.417457      1.000000    0.288137  0.205873
# model year    0.579267  -0.348746     -0.370164 -0.306564      0.288137    1.000000  0.180662
# origin        0.563450  -0.562543     -0.609409 -0.581024      0.205873    0.180662  1.000000


#              mpg    weight
# mpg     1.000000 -0.831741
# weight -0.831741  1.000000
