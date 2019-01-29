'''
Plot Beta distributions
Inspired from http://www.astroml.org/book_figures/chapter3/fig_beta_distribution.html
'''
import numpy as np
import scipy.stats as stats
from matplotlib import pyplot as plt

beta_distributions = [
    {
        'alpha': 9,
        'beta': 5,
        'linestyle': '-',
        'color': 'g'
    },
    {
        'alpha': 9,
        'beta': 6,
        'linestyle': '--',
        'color': 'r'
    },
    {
        'alpha': 10,
        'beta': 5,
        'linestyle': ':',
        'color': 'b'
    }
]

x = np.linspace(0, 1, 1002)[1:-1]

fig, ax = plt.subplots(figsize=(9, 6), dpi=80, facecolor='w', edgecolor='k')

plt.grid(color='#DDDDDD')

for params in beta_distributions:
    alpha = params['alpha']
    beta = params['beta']
    linestyle = params['linestyle']
    color = params['color']
    label = r'$\alpha={0:.1f},\ \beta={1:.1f}$'.format(alpha, beta)
    distribution = stats.beta(alpha, beta)

    plt.plot(
        x,
        distribution.pdf(x),
        linestyle=linestyle,
        linewidth=2,
        color=color,
        label=label
    )


plt.xlim(0, 1)
plt.ylim(0, 3.5)

plt.xlabel('$x$')
plt.ylabel(r'$p(x|\alpha,\beta)$')
plt.title('Beta Distribution')

plt.legend(loc=0)
plt.show()