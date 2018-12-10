from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import collections

binom_sim = data = stats.binom.rvs(n=100,p=0.3,size=100000)


values = list(collections.Counter(binom_sim).values())
keys = list(collections.Counter(binom_sim).keys())
print(values)
print(keys)

plt.plot(keys, values, 'o-')
plt.show()

