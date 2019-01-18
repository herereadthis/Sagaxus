'''
Take this example from 
Bayesian Statistics: A Beginner's Guide
https://www.quantstart.com/articles/Bayesian-Statistics-A-Beginners-Guide
'''

import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

probability_heads = 0.5
line_color = '#99cc99'

if __name__ == "__main__":
    # A list of the number of coin flips, aka Bernoulli Trials
    tests = [0, 2, 10, 20, 50, 500]

    # Generate 500 coin flips. 1 is heads, 0 is tails
    data = stats.bernoulli.rvs(0.5, size=tests[-1])
    
    # Discretise the x-axis into 100 separate plotting points
    x = np.linspace(0, 1, 100)

    '''
    We start with a prior belief of probability of success = 0.5, by having a=1
    and b=1 for beta distribution. Then update prior beliefs from the 500 test
    run. Update with 0 new trials, then 2 trials, then 10 trials, etc.
    '''
    for i, trial_size in enumerate(tests):
        # get number of heads for this update
        heads = data[0:trial_size].sum()

        # Create an axes subplot for each update 
        # there are 6 updates, generate 2X3 subplots
        ax = plt.subplot(len(tests) / 2, 2, i + 1)
        ax.set_title('{} trials, {} heads'.format(trial_size, heads))

        # x-axis label
        plt.xlabel('$P(H)$, Probability of Heads')
        # y-axis label
        plt.ylabel('Density')
        if i == 0:
            plt.ylim([0.0, 2.0])
        plt.setp(ax.get_yticklabels(), visible=False)

        # Create a Beta distribution to show posterior belief of coin success.
        y = stats.beta.pdf(x, 1 + heads, 1 + trial_size - heads)
        plot_label = 'Observe {} tosses,\n {} heads'.format(trial_size, heads)
        plt.plot(x, y, label=plot_label, color=line_color)
        plt.fill_between(x, 0, y, color=line_color, alpha=0.3)

    # Expand plot to cover full width and height
    plt.tight_layout()
    # show plot
    plt.show()