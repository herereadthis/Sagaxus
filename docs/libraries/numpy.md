# NumPy

* NumPy (Numerical Python) is Python Package library of multidimenional array objects and routines for processing them.
* When used in combination with `SciPy` (Scientific Python) and `Mat-plotlib`, it can be an alternative to MatLab
* install:
  ```bash
  pip install numpy
  ```

* The most important object defined in NumPay is an N-dimensional array type called `ndarray` whcih describes a collection of items of the same type.
  * each item in an ndarray takes the same size memory
  * each element is an `dtype` data-type object
  * instantiate an ndarray
    ```python
    numpy.array
    numpy.array(object, dtype=None, copy = True, order = None, subok = False, ndmin = 0)
    ```
    * `object` any object exposing the array interface method
    * `dtype` desired type of array
      * examples: `np.bool`, `np.int`
    * `copy` default: object is copied
    * `order` C (row) or F (column) or A (any, default)
    * `subok` default: returned array is base class, not sub-class
    * `ndmin` minimum dimensions of array

 ```python
import numpy as np

a = np.array([1, 2, 3])
print(a)
# [1 2 3]

# multidimensional array
b = np.array([[1, 2], [3, 4]])
print(b)
# [[1 2]
#  [3 4]]

# define dimensions
c = np.array([1, 2, 3, 4, 5], ndmin = 2)
print(c)
# [[1 2 3 4 5]]


# define data type
dt = np.dtype(np.int32)
foo = np.array([1, 2, 3], dtype=dt)
 ```

`shape` attribute returns a tuple of array dimensions. You can also use it to resize the array.

```python
import numpy as np

foo = np.array([[1,2,3], [4,5,6]])
# output: (2, 3) aka 2 rows 3 columns
print(foo.shape)

# resize the array
foo.shape = (3,2)
# output: array([[1, 2], [3, 4], [5, 6]])
print(foo)
```

`reshape` will resize an array

```python
import numpy as np

foo = np.array([[1,2,3], [4,5,6]])
bar = foo.reshape(3,2)
# output: [[1,2],[3,4],[5,6]]
```

`flatten()` will flatten an array

```python
import numpy as np

foo = np.array([[1,2,3], [4,5,6]])
bar = foo.flatten()
# output: [[1,2],[3,4],[5,6]]
```

`T` - transpose an array also `numpy.transpose()`

```python
import numpy as np

foo = np.array([[1,2,3], [4,5,6]])
bar = foo.T
# same result
bar = np.transpose(foo)
# output: [[1,2],[3,4],[5,6]]
print(bar)
```

`ndim` attribute returns the number of array dimensions

```python
import numpy as np

foo = np.arrange(5)
# output: array([0, 1, 2, 3, 4])
print(foo)
# output: 1
print(foo.ndim)
```

`itemsize` gets length of each element in bytes

```python
import numpy as np

foo = np.arrange(5)
# output: 8
print(foo.itemsize)
```

Creation

```python
# create an empty array of a specified shape
foo = np.empty([3,2])

# create an array filled with zeros
foo = np.zeros([3,2])
# output: [[0,0], [0,0], [0,0]]
print(foo)

bar = np.zeros(5)
# output: [0,0,0,0,0]
print(bar)

# create an array filled with ones
foo = np.ones([3,2])
# output: [[1,1], [1,1], [1,1]]
print(foo)


# create an array from an existing array
# asarray has fewer params
my_array = [1,2,3]
foo = np.asarray(my_array)

my_tuple = (1,2,3)
foo = np.asarray(my_tuple)
```

`numpy.arange` creates an array of evenly spaced values within a range

```python
foo = np.arange(start, stop, step, dtype)
foo = np.arange(0, 10, 2)
# output [0,2,4,6,8]
print(foo)
```

`numpy.linspace` creates an array where you specify the number of intervals in the range
* `endpoint` whether to include the last number in the range (stop value)

```python
foo = np.linspace(start, stop, num, endpoint, retstep, dtype)
foo = np.linspace(0, 10, 6)
# output [0,2,4,6,8,10]
print(foo)
```

`numpy.logspace` is like `linspace` except intervals are on a log scale.

```python
foo = np.logspace(start, stop, num, endpoint, retstep, dtype)
```

`slice` an array

```
slice(start, stop, step)
foo = np.arange(10)
slicer = slice(2,7,2)
# output: [2, 4, 6]
print(a[s])

# shorthand, same result
print(a[2:7:2])

# slice from index
# output: [7,8,9]
print(a[7:])


# multidimensional slicing with ellipsis...
foo = np.array([[1,2,3],[4,5,6],[7,8,9]])

# get items in second column: [2,4,5]
print(foo[...,1])

# get items in second row: [4,5,6]
print(foo[1,...])

# get second column and any column after that [[2,3],[5,6],[8,9]]
print(foo[...,1:])
```

* Indexing you can get elements from an array based on its dimension index

```python
# get elements at (0,0, (1,1), and (2,0)
foo = np.array([1,2],[3,4],[5,6])
bar = foo[[0,1,2],[0,1,0]]
# output: [1, 4, 5]
print(bar)
```

Use an array to get an array from the array say what?

```python
foo = np.array([[1,2,3],[4,5,6],[7,8,9]])
rows = np.array([[0,1],[1,2]])
cols = np.array([[2,2],[0,1]])
bar = foo[rows, cols]
# output: [[3,6],[4,8]]
print(bar)
```

Boolean indexing: return values passing `True` for some condition.

```python
import numpy as np
foo = np.array([[1,2,3],[4,5,6],[7,8,9]])
bar = foo[foo > 5]
# output: [6, 7, 8, 9]
print(bar)
```

`numpy.nditer` iterates over an array.


```python
import numpy as np
foo = np.arange(0,18,2)
# output: [[ 0,  2,  4,  6,  8, 10, 12, 14, 16]]
print(foo)
foo.reshape(3,3)
# output: [[0,2,4],[6,8,10],[12,14,16]]

for x in np.nditer(foo):
    print(x)

```

### Statistics


* `numpy.amin()` - returns minimum at axis
* `numpy.amax()` - returns maximum at axis

```python
import numpy as np
foo = np.array([[3,7,5],[8,4,3],[2,4,9]])

# minimum of the flattened array: 2
print(np.amin(foo))

# minimum on first axis: [2, 4, 3]
print(np.amin(a,0))
print(np.amin(a, axis=0))

# minimum on second axis: [3, 3, 2]
print(np.amin(a,1))

# maximum of the flattened array: 9
print(np.amax(foo))

# maximum on first axis: [8, 7, 9])
print(np.amax(a,0))

# maximum on second axis: [7, 8, 9]
print(np.amax(a,1))
```


* `numpy.median()` - returns median at axis
* `numpy.mean()` - returns mean at axis
* `numpy.average()` - returns a weighted average, given an array

```python
import numpy as np
foo = np.array([1,2,3,4])
bar = np.array([4,3,2,1])

# output: 2.5
print(np.average(foo))

#output: 2
print(np.average(foo, weights=bar))
```

* `numpy.std()` - returns standard deviation
* `numpy.var()` - returns variance

```python
import numpy as np
foo = np.array([1,2,3,4])

# output: 1.118033988749895
print(np.std(foo))

# output: 1.25
print(np.var(foo))
```

## Sources

* [NumPy Tutorial](https://www.tutorialspoint.com/numpy)

