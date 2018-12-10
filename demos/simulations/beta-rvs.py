from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import collections

binom_sim = data = stats.binom.rvs(n=100,p=0.3,size=100000)

a = 80
b = 220
x = np.arange(0.01, 1, 0.01)
y = stats.beta.pdf(x, a, b)

plt.plot(x, y)
plt.show()
