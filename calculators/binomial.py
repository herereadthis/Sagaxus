"""
Calculate outcomes from Binomial distributions
"""

from scipy.stats import binom

if __name__ == '__main__':
    probability_input = 'what is the probability, in decimals? '
    probability = float(input(probability_input))

    if probability > 1 or probability <= 0:
        raise ValueError('probability must be decimal between 0 and 1.')

    population_input = 'what is the size of the set or population? '
    population = int(input(population_input))

    if population < 2:
        raise ValueError('Population must be greater than 1.')

    iterate_input = 'Do you want to run all success amounts? [y]/n '
    iterate = str(input(iterate_input)).lower() or 'y'

    if iterate == 'y':
        iterate = True
    else: 
        iterate = False

    if iterate == False:
        success_input = 'how many success to obtain from the population? ' 
        success = int(input(success_input))

        if success > population:
            raise ValueError('Number of successes must be less than the size of population.')

        binom_result = binom.pmf(success, population, probability)
        print(binom_result)
    else:
        for x_value in range(0, population + 1):
            binom_result = binom.pmf(x_value, population, probability)
            print_output = '{0}: {1}'.format(x_value, binom_result)
            print(print_output)
