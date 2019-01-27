'''
Multiply two matrices
a 4x4 matrix times a 4x1 matrix
Reference: sagaxus/docs/numpy.md
'''
import numpy as np

a = [
    [.25, .20, .25, .30],
    [.20, .30, .25, .30],
    [.25, .20, .40, .10],
    [.30, .30, .10, .30]
]

x0 = [[1], [0], [0], [0]]
x1 = np.matmul(a, x0)
x2 = np.matmul(a, x1)
x3 = np.matmul(a, x2)
x4 = np.matmul(a, x3)
x5 = np.matmul(a, x4)
x6 = np.matmul(a, x5)
x7 = np.matmul(a, x6)
x8 = np.matmul(a, x7)
x9 = np.matmul(a, x8)
x10 = np.matmul(a, x9)
x11 = np.matmul(a, x10)
x12 = np.matmul(a, x11)
x13 = np.matmul(a, x12)
x14 = np.matmul(a, x13)
x15 = np.matmul(a, x14)
x16 = np.matmul(a, x15)
x17 = np.matmul(a, x16)
x18 = np.matmul(a, x17)
x19 = np.matmul(a, x18)
x20 = np.matmul(a, x19)

print(x20)
