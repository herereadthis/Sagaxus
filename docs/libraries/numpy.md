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
 ```

## Sources

* [NumPy Tutorial](https://www.tutorialspoint.com/numpy)

