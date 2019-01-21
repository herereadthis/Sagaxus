# Markov Chain Monte Carlo (MCMC)

## What is the point?

* It's easy when the likelihood function is a binomial distribution and the prior is a Beta distibution. The posterior is also a Beta distribution. The prior is a <strong>conjugate prior</strong>
* Not all models can use conjugate priors, so calculating the posterior will have to approximated.
  * Example: <strong>Bayesian Hierachal Modeling</strong> - a statistical model with multiple levels and is basically intractable using analytical methods
* <strong>Markov Chain Monte Carlo (MCMC) - a family of algorithms that help approximate the posterior distribution from Bayesian Statistics.
* Recall Bayes&rsquo; Theorem for continuous priors:
  > ![Continuous bayes](./img/ad81b4e0-f495-4ba3-be45-301752496402.png)<!--
    {f(\theta|x)d\theta =
    \frac{p(x|\theta)f(\theta)d\theta}{\int_a^b p(x|\theta)f(\theta)d(\theta)}}
    -->
  * Sometimes it&rsquo;s too difficult to solve for the denominator.
* If a model has many parameters, integrals will have to be solved over multiple dimensions, which leads to:
  * <strong>Curse of Dimensionality</strong> - as integral dimensions increase, the volume space becomes so vast that any data becomes insignificant, e.g., we would need a whole lot more data.
  <!--
* Basic idea:
  * Sample the posterior distribution by combining a random search (Monte Carlo) with
  * A mechanism for moving around that is memoryless (Markov Chain)
  -->

## Non-math introduction (approach #1)

* [Use MCMC methods to approximate the posterior distribution](A Zero-Math Introduction to Markov Chain Monte Carlo Methods) of a parameter by random sampling in a probablistic space
  * <em>Parameter</em> - the value of the probability of something happening
  * <em>Distribution</em> - a mathematical representation of every possible value of the parameter and how likely they are, i.e., a probability of probabilties
  * In Bayesian terminology, it describes our beliefs about the parameter.

### Height example:

* Suppose we believe the average height of a human follows a normal distribution with a mean <strong>&mu;</strong>=74 inches. This is the <em>prior distribution</em>.
* Supposed we collected data, and observed a range of heights between 60 - 72 inches. If the data can be represented as a curve of what the average human height might be, then it is the <em>likelihood distribution</em>*
* Combine the prior and likelihood to get the <em>posterior distribution</em>.
* But what if the prior and likelihood aren't easy bell curve


### Monte Carlo

* Suppose we drew a circle with a radius of 1, and the center is at 0,0. If we didn't know the value of <strong>&pi;</strong> can we find the area of the circle?
* Generate a bunch of random tuples (x,y) such that <em>-1 &le; x &le; 1</em> and <em>-1 &le; y &le; 1</em> Then we can use the ratio of the coordinates that fall inside the circle versus the number of tuples generated to estimat <strong>&pi;</strong>

### Markov Chain

* <strong>Markov Chain</strong> - sequences of events that are probabilistically related to each other.
  * Each event comes from a set of outcomes
  * Each outcome determines which outcome occurs next
  * Each outcome occurs according to a set of probabilties
* <strong>Memoryless</strong> - everything you need to know to predict the next outcome can be determined by looking at the current state. The history of events provides no new information.
* Although the first few characters appear as if they were determined by where you started, the distribution of outcomes will eventually settle into a pattern.
* Interdependent events, if confined to probabilities, will eventually conform to an average.

### combine the two

* MCMC method picks a random parameter value to begin.
* Next, generate a random value.
* If that randomly generated value is more likely to explain the data, given prior beliefs, then it is added to the chain of parameter values, with a certain probability based on how much better.
* Over time, generate a histogram over which values occur most, and that histogram will approximate the posterior distribution.

## Non-bullshit explanation (approach #2)

* [MCMC attempts to draw from a distribution efficiently](https://jeremykun.com/2015/04/06/markov-chain-monte-carlo-without-all-the-bullshit/).
* Suppose there is a black box which estimates the probablity of what baby name you will choose for your child.
  * Pick a name randomly and the black box will give you the probability of you choosing that name for your child.
  * Some names will have higher probability of being the chosen name, some names will have very very low probablity of being the chosen name.
  * Suppose the process of choosing names randomly was a uniform process. Then the generating of names is very inefficient.
* Suppose there is a finite set <em>X</em> and suppose there is a distribution <em>D</em> over that set.
  * There a black box that will give the probability function <em>p(x)</em> which gives the probability of drawing <em>x &isin; X</em> according to <em>D</em>
  * Create an efficient algorithm <em>A</em> that generates an element within the set X so that the probability of getting <em>x</em> is approximately <em>p(x)</em>*
  * In other words, generate random values that are more likely to occur according its chances of occurring.





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

* This one has Python code to do multivariate testing with Markov Chain Monte Carlo. Definitely worth studying [A/B Testing with Hierarchical Models in Python](https://blog.dominodatalab.com/ab-testing-with-hierarchical-models-in-python/)
* This seems like a very good resource to understand MCMC, but it is beyond my level of understanding currently:  [Stat 3701 Lecture Notes: Bayesian Inference via Markov Chain Monte Carlo (MCMC)](http://www.stat.umn.edu/geyer/3701/notes/mcmc-bayes.html)
* This one is okay, not as good: [An Introduction to MCMC
methods and Bayesian Statistics](https://www.ukdataservice.ac.uk/media/307220/presentation4.pdf)

## Sources

* Use monte carlo to find the probability one beta distribution is better than another: [6 Neat Tricks with Monte Carlo Simulations](https://www.countbayesie.com/blog/2015/3/3/6-amazing-trick-with-monte-carlo-simulations)
* [Bayesian A/B Testing: A Hypothesis Test that Makes Sense](https://www.countbayesie.com/blog/2015/4/25/bayesian-ab-testing)
* [how to implement these 5 powerful probability distributions in Python](https://bigdata-madesimple.com/how-to-implement-these-5-powerful-probability-distributions-in-python/)
* [Python histogram outline](https://stackoverflow.com/questions/42741687/python-histogram-outline)
* [How to plot empirical cdf in matplotlib in Python?](https://stackoverflow.com/questions/3209362/how-to-plot-empirical-cdf-in-matplotlib-in-python)
* [Markov Chain Monte Carlo for Bayesian Inference - The Metropolis Algorithm](https://www.quantstart.com/articles/Markov-Chain-Monte-Carlo-for-Bayesian-Inference-The-Metropolis-Algorithm)
* [A Zero-Math Introduction to Markov Chain Monte Carlo Methods](https://towardsdatascience.com/a-zero-math-introduction-to-markov-chain-monte-carlo-methods-dcba889e0c50)
* [Markov Chain Monte Carlo Without all the Bullshit](https://jeremykun.com/2015/04/06/markov-chain-monte-carlo-without-all-the-bullshit/)
