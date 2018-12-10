from __future__ import division
from scipy.stats import beta
import numpy as np

simulations = 100000
control_success, control_sample  = 30, 200
control_miss = control_sample - control_success
treatment_success, treatment_sample = 50, 200
treatment_miss = treatment_sample - treatment_success

control = np.array(beta.rvs(control_success, control_sample, size=simulations))
treatment = np.array(beta.rvs(treatment_success, treatment_sample, size=simulations))
mc_treatment_wins = sum((treatment - control) > 0)
treatment_better_prob = mc_treatment_wins/simulations
print(treatment_better_prob)
