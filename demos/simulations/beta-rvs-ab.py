from __future__ import division
from scipy.stats import beta
import numpy as np
import matplotlib.pyplot as plt

simulations = 100000
# prior
p_success, p_sample = 40, 200
p_miss = p_sample - p_success
# control
c_success, c_sample  = 18, 100
c_miss = c_sample - c_success
# treatment
t_success, t_sample = 28, 100
t_miss = t_sample - t_success

control = np.array(beta.rvs(c_success + p_success, c_miss + p_miss, size=simulations))
treatment = np.array(beta.rvs(t_success + p_success, t_miss + p_miss, size=simulations))
mc_treatment_wins = sum((treatment - control) > 0)
treatment_better_prob = mc_treatment_wins/simulations
print(treatment_better_prob)
# 0.97

treatment_better_ratio = treatment / control
plt.hist(treatment_better_ratio, bins=50, edgecolor='black')
plt.show()

x = np.sort(treatment_better_ratio)
y = np.arange(len(x))/float(len(x))
plt.plot(x,y)
plt.show()
