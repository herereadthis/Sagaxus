import pandas as pd
import numpy as np

print('Creating Series')

series_a = pd.Series()
print(series_a)

data_b = np.array(['a', 'b', 'c', 'd', 'e'])
series_b = pd.Series(data_b)
print(series_b)

# assigning indices
data_c = np.array(['a', 'b', 'c', 'd'])
series_c = pd.Series(data_c, index=[100, 101, 102, 103])
print(series_c)

# series from a dict
data_d = {'a': 0.0, 'b': 1.0, 'c': 2.0}
series_d = pd.Series(data_d)
print(series_d)

# series from Scaler
data_e = 5
series_e = pd.Series(data_e, index=[0, 1, 2, 3])
print(series_e)

print('Accessing Data')

# accessing data from series with position
data_f = [1, 2, 3, 4, 5]
index_f = ['a', 'b', 'c', 'd', 'e']
series_f = pd.Series(data_f, index=index_f)

# retrieve first element
print(series_f[0])
# 1

# retrieve first 3 elements
print(series_f[:3])

# retrieve last 3 elements
print(series_f[-3:])

# retrieve using label aka index
print(series_f['a'])

# retreive multiple elements with list of indices
print(series_f[['c', 'd']])