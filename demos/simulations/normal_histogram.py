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

ax = plt.subplot()
sns.distplot(data, kde=False, ax=ax)
title = 'Histogram of observed data'
_ = ax.set(title=title, xlabel='x', ylabel='# observations')

plt.show()
