# Pandas

Pandas is a Python library which provides tools for data structures and data analysis. Pandas can accomplish the 5 typical steps in the processing and analysis of data: load, prepare, manipulate, model, and analyze.

* Frequently used with `NumPy`

```bash
pip install pandas
```

Pandas deals with the following 3 data structures

* **Series** - 1-dimensional array `[1, 2, 3, 4, 5]`
  * Homogeneous data
  * Size Immutable
  * Values of data are mutable
* **DataFrame** - 2D labeled array (container for series)
  * Example: a chart of people - their names, age, gender
  * Each column represents an attribute, and each row represents a person
* **Panel** - 3D labeled, size-mutable (container for DataFrame)

```python
# create a series
pandas.series(data, index, dtype, copy)
```

* `data` various forms such as `ndarray`, list, constants
* `index` must be unique and hashable, same length as data
* `dtype` if none, then dtype will be inferred
* `copy` default False

### Creating Series

```
import pandas as pd
import numpy as np

series_a = pd.Series()
print(series_a)
# Series([], dtype: float64)

data_b = np.array(['a', 'b', 'c', 'd', 'e'])
series_b = pd.Series(data_b)
print(series_b)
# 0    a
# 1    b
# 2    c
# 3    d
# 4    e
# dtype: object
# did not pass any index, so indices were assigned

# assigning indices
data_c = np.array(['a', 'b', 'c', 'd'])
series_c = pd.Series(data_c, index=[100, 101, 102, 103])
print(series_c)
# 100    a
# 101    b
# 102    c
# 103    d
# dtype: object

# create a series from a dict
# if no index is specified, then the keys become the index
data_d = {'a': 0.0, 'b': 1.0, 'c': 2.0}
series_d = pd.Series(data_d)
print(series_d)
# a    0.0
# b    1.0
# c    2.0
# dtype: float64

# series from Scaler
data_e = 5
series_e = pd.Series(data_e, index=[0, 1, 2, 3])
print(series_e)
# 0    5
# 1    5
# 2    5
# 3    5
# dtype: int64
```

### Accessing Data from Series

```python
data_f = [1, 2, 3, 4, 5]
index_f = ['a', 'b', 'c', 'd', 'e']
series_f = pd.Series(data_f, index=index_f)

# retrieve first element
print(series_f[0])
# 1

# retrieve first 3 elements
print(series_f[:3])
# a    1
# b    2
# c    3
# dtype: int64

# retrieve last 3 elements
print(series_f[-3:])
# c    3
# d    4
# e    5
# dtype: int64

# retrieve using label aka index
print(series_f['a'])
# 1

# retreive multiple elements with list of indices
print(series_f[['c', 'd']])
# c    3
# d    4
# dtype: int64
```

