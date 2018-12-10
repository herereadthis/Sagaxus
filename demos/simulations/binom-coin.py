
from __future__ import division
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import collections

# simulate N coin tosses to find out the probability of getting 3 heads

simulations = 100000
binom_sim = stats.binom.rvs(n=10,p=0.5,size=simulations)
binom_real = stats.binom.pmf(3,10,0.5)

values = list(collections.Counter(binom_sim).values())
keys = list(collections.Counter(binom_sim).keys())
print(values)
print(keys)
sim_prob = values[3] / simulations
print(sim_prob)
print(binom_real)




