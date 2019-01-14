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

## Sources

* [NumPy Tutorial](https://www.tutorialspoint.com/numpy)

