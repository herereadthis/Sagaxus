"""
Calculate outcomes from Binomial distributions
"""

from scipy.stats import norm

if __name__ == '__main__':
    alpha_input = 'what is the significance level alpha? '
    alpha = input(alpha_input)

    z_score = norm.ppf((1 - alpha))
    print(z_score)
