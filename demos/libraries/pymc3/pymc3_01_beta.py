'''
Get posterior distribution using PyMC3 when prior is a beta and data is binom.
Taken from: https://www.quantstart.com/articles/Markov-Chain-Monte-Carlo-for-
Bayesian-Inference-The-Metropolis-Algorithm
'''
import matplotlib.pyplot as plt
import numpy as np
import pymc3
import scipy.stats as stats

# Parameter values for prior and analytic posterior
trials, successes = (50, 10)
alpha_prior, beta_prior = (12, 12)
alpha_posterior = alpha_prior + successes
beta_posterior = beta_prior + trials - successes

# number of iterations of Metropolis algorithm for MCMC
iterations = 100000

# Use PyMC3 to construct a model context
basic_model = pymc3.Model()
with basic_model:
    # Let theta be the paramater to be determined by the prior beta distribution
    theta = pymc3.Beta('theta', alpha=alpha_prior, beta=beta_prior)

    # Define the Bernoulli likelihood function
    y = pymc3.Binomial('y', n=trials, p=theta, observed=successes)

    '''
    The guide recommends start = pymc3.find_MAP() Maximum A Posteriori (MAP) 
    optimisation as the initial value for MCMC
    However, pymc3.sample() "automatically initializes NUTS in a better way."
    '''
    start = pymc3.sample()

    # Use the Metropolis algorithm (as opposed to NUTS or HMC, etc.)
    step = pymc3.Metropolis()

    # Calculate the trace
    trace = pymc3.sample(iterations, step, start, random_seed=1, progressbar=True)

# Plot the analytic prior and posterior beta distributions
x = np.linspace(0, 1, 100)
plt.plot(
    x,
    stats.beta.pdf(x, alpha_prior, beta_prior),
    linestyle='--',
    label=r'$Prior (\alpha={0},\ \beta={1})$'.format(alpha_prior, beta_prior),
    color='#333399'
)
plt.plot(
    x,
    stats.beta.pdf(x, alpha_posterior, beta_posterior), 
    linestyle='-',
    label=r'$Posterior (\alpha={0},\ \beta={1})$'.format(alpha_posterior, beta_posterior),
    color='#9999FF'
)

# Plot the posterior histogram from MCMC analysis
bins=50
plt.hist(
    trace['theta'],
    bins,
    histtype='step',
    normed=True, 
    label='Posterior (MCMC)',
    color='#FF6600'
)

# Update the graph labels
plt.grid(color='#DDDDDD')
plt.legend(title='Parameters', loc='best')
plt.xlabel('$\\theta$, Fairness')
plt.ylabel('Density')
plt.xlim(0,1)
plt.ylim(0,8)
plt.show()

# Show the trace plot
pymc3.traceplot(trace)
plt.show()
