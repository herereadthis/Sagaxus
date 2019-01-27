from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

n = 10
p = 0.3
# create a list of numbers from 0 to 20, for 21 values
k = np.arange(0,21)
print(k)

# probability of each value
binomial = stats.binom.pmf(k, n, p)
print(binomial)

plt.plot(k, binomial, 'o-')
plt.title('Binomial: n={0}, p={1}'.format(n,p))
plt.xlabel('Number of successes')
plt.ylabel('Probability of Successes')
plt.show()

