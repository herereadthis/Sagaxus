"""
Calculate Z-score from 2 populations
"""
from __future__ import division
from scipy.stats import norm
import math

from scipy.stats import norm

if __name__ == '__main__':
    title_card = 'This calculator will find the z of 2 populations assumed to have a binomial distribution.'

    n1_input = 'What is the size of sample 1? '   
    n1 = int(input(n1_input))
    x1_input = 'How many success in sample 1? '
    x1 = int(input(x1_input))

    n2_input = 'What is the size of sample 2? '   
    n2 = input(n2_input) 
    x2_input = 'How many success in sample 2? '
    x2 = input(x2_input)

    conversion1 = (x1/n1)
    print('     conversion 1: {0}'.format(conversion1))
    conversion2 = (x2/n2)
    print('     conversion 2: {0}'.format(conversion2))
    test_statistic = conversion1 - conversion2
    print('   test statistic: {0}'.format(test_statistic))
    pooled_proportion = (x1 + x2)/(n1 + n2) 
    print('pooled proportion: {0}'.format(pooled_proportion))
    pq = pooled_proportion * (1 - pooled_proportion)
    standard_error = math.sqrt(pq * ((1/n1) + (1/n2)))
    print('   standard error: {0}'.format(standard_error))
    z_score = test_statistic/standard_error

    print('          z-score: {0}'.format(z_score))
    p_value = norm.cdf(z_score)
    print('          p-value: {0}'.format(p_value))

