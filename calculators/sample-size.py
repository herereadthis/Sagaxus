"""
asdf
"""
from __future__ import division
from scipy.stats import norm
import math

from scipy.stats import norm

if __name__ == '__main__':
    title_card = 'This calculator will determine the sample size needed to detect a change in conversion.'

    alpha_default = 0.05
    beta_default = 0.8
    uplift_default = 10

    p1_input = 'What is the current conversion rate (p < 1)? '
    p1 = float(input(p1_input))
    alpha_input = 'what is the desired significance [{0}]? '.format(alpha_default)
    alpha = float(raw_input(alpha_input) or alpha_default)
    beta_input = 'what is the desired significance [{0}]? '.format(beta_default)
    beta = float(raw_input(beta_input) or beta_default)
    uplift_input = 'what is the desired uplift as a percentage [{0}]? '.format(uplift_default)
    uplift_percentage = float(raw_input(uplift_input) or uplift_default)
    uplift = 1 + uplift_percentage / 100
    p2 = p1 * uplift

    numerator = p1 * (1 - p1) + p2 * (1 - p2)
    denominator = math.pow((p1 - p2), 2)

    z_alpha = norm.ppf(1 - (alpha / 2))
    z_beta = norm.ppf(beta)

    z_factor = math.pow((z_alpha + z_beta), 2)

    sample_size = int(round(z_factor * numerator / denominator))

    print('null coversion: {0}'.format(p1))
    print('new coversion: {0}'.format(p2))
    print('sample size: {0}'.format(sample_size))
    print(z_alpha)
    print(z_beta)
    print(numerator)
    print(denominator)
