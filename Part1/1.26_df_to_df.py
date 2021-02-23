import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.tail())
print('\n')
print(type(df))
print('\n')

addition = df + 10
print(addition.tail())
print('\n')
print(type(addition))
print('\n')

subtraction = addition - df
print(subtraction.tail())
print('\n')
print(type(subtraction))


#       age   fare
# 886  27.0  13.00
# 887  19.0  30.00
# 888   NaN  23.45
# 889  26.0  30.00
# 890  32.0   7.75


# <class 'pandas.core.frame.DataFrame'>


#       age   fare
# 886  37.0  23.00
# 887  29.0  40.00
# 888   NaN  33.45
# 889  36.0  40.00
# 890  42.0  17.75


# <class 'pandas.core.frame.DataFrame'>


#       age  fare
# 886  10.0  10.0
# 887  10.0  10.0
# 888   NaN  10.0
# 889  10.0  10.0
# 890  10.0  10.0


# <class 'pandas.core.frame.DataFrame'>
