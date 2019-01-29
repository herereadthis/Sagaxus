'''
Plot Beta distributions
Inspired from http://www.astroml.org/book_figures/chapter3/fig_beta_distribution.html
'''
import numpy as np
import scipy.stats as stats
from matplotlib import pyplot as plt

beta_distributions = [
    {
        'alpha': 1,
        'beta': 1,
        'linestyle': '-',
        'color': 'b'
    },
    {
        'alpha': 3,
        'beta': 7,
        'linestyle': '--',
        'color': 'g'
    },
    {
        'alpha': 5,
        'beta': 5,
        'linestyle': ':',
        'color': 'r'
    },
    {
        'alpha': 4,
        'beta': 6,
        'linestyle': '-.',
        'color': 'c'
    }
]

x = np.linspace(0, 1, 1002)[1:-1]

fig, ax = plt.subplots(figsize=(5, 3.75))

for params in beta_distributions:
    alpha = params['alpha']
    beta = params['beta']
    linestyle = params['linestyle']
    color = params['color']
    label = r'$\alpha={0:.1f},\ \beta={0:.1f}$'.format(alpha, beta)
    distribution = stats.beta(alpha, beta)

    plt.plot(
        x,
        distribution.pdf(x),
        linestyle=linestyle,
        color=color,
        label=label
    )


plt.xlim(0, 1)
plt.ylim(0, 3)

plt.xlabel('$x$')
plt.ylabel(r'$p(x|\alpha,\beta)$')
plt.title('Beta Distribution')

plt.legend(loc=0)
plt.show()