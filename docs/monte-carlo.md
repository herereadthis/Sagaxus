# Monte Carlo

* Suppose we drew a circle with a radius of 1, and the center is at 0,0. If we didn't know the value of <strong>&pi;</strong> can we find the area of the circle?
* Generate a bunch of random tuples (x,y) such that <em>-1 &le; x &le; 1</em> and <em>-1 &le; y &le; 1</em> Then we can use the ratio of the coordinates that fall inside the circle versus the number of tuples generated to estimat <strong>&pi;</strong>

## Monte Carlo Example

* Suppose there are two samples, control and treatment
  * Control has 35 conversions from 200 users
  * Treatment has 50 conversions from 200 users
* What is the probability that treatment is better than control?
* We can simulate random variables using `.rvs`

```python
from __future__ import division
from scipy.stats import beta
import numpy as np
import matplotlib.pyplot as plt

simulations = 100000
# prior
p_success, p_sample = 40, 200
p_miss = p_sample - p_success
# control
c_success, c_sample  = 18, 100
c_miss = c_sample - c_success
# treatment
t_success, t_sample = 28, 100
t_miss = t_sample - t_success

control = np.array(beta.rvs(c_success + p_success, c_miss + p_miss, size=simulations))
treatment = np.array(beta.rvs(t_success + p_success, t_miss + p_miss, size=simulations))
mc_treatment_wins = sum((treatment - control) > 0)
treatment_better_prob = mc_treatment_wins/simulations
print(treatment_better_prob)
# 0.97

treatment_better_ratio = treatment / control
plt.hist(treatment_better_ratio, bins=50, edgecolor='black')
plt.show()

x = np.sort(treatment_better_ratio)
y = np.arange(len(x))/float(len(x))
plt.plot(x,y)
plt.show()
```

* Here is the [equiavelent in R](https://www.countbayesie.com/blog/2015/4/25/bayesian-ab-testing)

```r
n.trials <- 100000
prior.alpha <- 40
prior.beta <- 160
a.samples <- rbeta(n.trials,18+prior.alpha,82+prior.beta)
b.samples <- rbeta(n.trials,28+prior.alpha,72+prior.beta)
p.b_superior <- sum(b.samples > a.samples)/n.trials
```


## Sources

* Use monte carlo to find the probability one beta distribution is better than another: [6 Neat Tricks with Monte Carlo Simulations](https://www.countbayesie.com/blog/2015/3/3/6-amazing-trick-with-monte-carlo-simulations)
* [Bayesian A/B Testing: A Hypothesis Test that Makes Sense](https://www.countbayesie.com/blog/2015/4/25/bayesian-ab-testing)
* [how to implement these 5 powerful probability distributions in Python](https://bigdata-madesimple.com/how-to-implement-these-5-powerful-probability-distributions-in-python/)
* [Python histogram outline](https://stackoverflow.com/questions/42741687/python-histogram-outline)
* [How to plot empirical cdf in matplotlib in Python?](https://stackoverflow.com/questions/3209362/how-to-plot-empirical-cdf-in-matplotlib-in-python)
* [Markov Chain Monte Carlo for Bayesian Inference - The Metropolis Algorithm](https://www.quantstart.com/articles/Markov-Chain-Monte-Carlo-for-Bayesian-Inference-The-Metropolis-Algorithm)
* [A Zero-Math Introduction to Markov Chain Monte Carlo Methods](https://towardsdatascience.com/a-zero-math-introduction-to-markov-chain-monte-carlo-methods-dcba889e0c50)
* [Markov Chain Monte Carlo Without all the Bullshit](https://jeremykun.com/2015/04/06/markov-chain-monte-carlo-without-all-the-bullshit/)
