'''
Multiply two matrices
a 4x4 matrix times a 4x1 matrix
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

print(x2)
