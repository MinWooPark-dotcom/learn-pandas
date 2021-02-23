import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.head())
print('\n')
#     age     fare
# 0  22.0   7.2500
# 1  38.0  71.2833
# 2  26.0   7.9250
# 3  35.0  53.1000
# 4  35.0   8.0500

print(type(df))
print('\n')
# <class 'pandas.core.frame.DataFrame'>

addition = df + 10
print(addition.head())
print('\n')
print(type(addition))

#     age     fare
# 0  32.0  17.2500
# 1  48.0  81.2833
# 2  36.0  17.9250
# 3  45.0  63.1000
# 4  45.0  18.0500

# <class 'pandas.core.frame.DataFrame'>
