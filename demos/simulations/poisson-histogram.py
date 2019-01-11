import numpy as np
import matplotlib.pyplot as plt
samples = np.random.poisson(5, 10000)
count, bins, ignored = plt.hist(samples, 14, density=True)


print('count')
print(count)
print('bins')
print(bins)
print('ignored')
print(ignored)
plt.show()