"""
Calculate outcomes from Binomial distributions
"""

from scipy.stats import norm

if __name__ == '__main__':
    zscore_input = 'what is the z-score? '
    zscore = input(zscore_input)

    p1 = norm.cdf(zscore)
    p3 = 2 * (1 - norm.cdf(zscore))

    cumulative_output = 'Cumulative: {0}'.format(p1)
    complementary_output = 'Complement: {0}'.format(1 - p1)
    two_tail_output = '2-tail:     {0}'.format(p3)
    print(cumulative_output)
    print(complementary_output)
    print(two_tail_output)
    cdf_footnote = 'Cumulative: probability that a statistic is less than Z'
    comp_footnote = 'Complement: probability that a statistic is greater than Z'
    two_tail_footnote = '2-tail: probability that a statistic exists outside of Z'
    print(cdf_footnote)
    print(comp_footnote)
    print(two_tail_footnote)
