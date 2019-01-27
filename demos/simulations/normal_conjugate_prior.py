'''
Simululate a Z-normal (mean = 1, variance = 1) distribution by generating
random values and plotting as a histogram.
'''

import math
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import norm

sns.set_style('white')
sns.set_context('talk')

# this resets the random number generator
# if you set this, then every random generation will be the same.
np.random.seed(123)

# numpy.random.randn() generates numbers from a random distribution
data = np.random.randn(20)

print(data)

def calc_posterior_analytical(data, x, mu_0, sigma_0):
    sigma = 1.
    n = len(data)
    mu_post_numerator = (mu_0 / sigma_0**2 + data.sum() / sigma**2)
    mu_posterior = mu_post_numerator / (1. / sigma_0**2 + n / sigma**2)
    mu_post = (mu_0 / sigma_0**2 + data.sum() / sigma**2) / (1. / sigma_0**2 + n / sigma**2)
    sigma_posterior = (1. / sigma_0**2 + n / sigma**2)**-1

    return norm(mu_posterior, math.sqrt(sigma_posterior)).pdf(x)

ax = plt.subplot()
x = np.linspace(-1, 1, 500)
posterior_analytical = calc_posterior_analytical(data, x, 0., 1.)
ax.plot(x, posterior_analytical)
ax.set(xlabel='mu', ylabel='belief', title='Analytical posterior')
sns.despine()

plt.show()
