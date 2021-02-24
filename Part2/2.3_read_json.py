# -*- coding: utf-8 -*-

import pandas as pd

# read_json() 함수로 데이터프레임 변환
df = pd.read_json('./read_json_sample.json')
print(df)
print('\n')
print(df.index)

#            name  year        developer opensource
# pandas           2008    Wes Mckinneye       True
# NumPy            2006  Travis Oliphant       True
# matplotlib       2003   John D. Hunter       True


# Index(['pandas', 'NumPy', 'matplotlib'], dtype='object')
