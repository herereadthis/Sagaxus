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


### [Monopoly as MCMC](https://stats.stackexchange.com/q/12680)

* Imagine all properties of a Monoply board game as different possible states.
* When transitioning to any other probability, you have various probabilities of moving around based on your dice rolls.
* Eventually, it is possible to return to where you start. Also if your monopoly game lasts forever, the probability of being on any property won't depend on where you started.
* Now, instead of rolling dice, create some program which simulates random numbers and you move around the board based on your results.
* The monopoly board = Markov Chain
* The simulated dice rolls: Markov Chain

### Why not just a ton of Monte Carlo simulations and skip the Markov chain?

* Ultimately, the goal is to find the area under a tricky curve (i.e., integrate complicated posterior distribution). We could theoretically generate a million values and just find the ratio of samples that lie under versus above the curve.
* The way MCMC would work is to generate a value, and then generate another value.
  * Based on the probability of the new value occurring, then accept it if is more likely to occur than the previous value, or rejected it (the exact criteria of acceptance or rejection is based on the specific algorithm), and continue to generate new values.
  * (If rejected, generate a new value and compare that value to the last accepted value.)
  * This process will approximate the curve and we won't have to generate as many values as a plain Monte Carlo system.
  * This process of acceptance/rejection [makes it a Markov Chain]((https://stats.stackexchange.com/q/108)) because we are only evaluating the current state/value, and comparing it to the next state/value.

### As code


If <strong><em>x</em></strong> is entire state of the below computer program (ignoring the thing that generates the random numbers) then it would be MCMC

```
Initialize x
repeat {
    Generate pseudorandom change to x
    Output x
}
```


<!--

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

-->


<!--
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
* Suppose the weather is either sunny, rainy, or cloudy.
  * If today is sunny, then the probability of tomorrow being sunny is 70%, cloudy 20%, and rainy 10%. For all other days, see the matrix below:
<table>
  <thead>
    <tr>
      <th></th>
      <th>Sunny</th>
      <th>Cloudy</th>
      <th>Rainy</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Sunny</td>
      <td>0.7</td>
      <td>0.2</td>
      <td>0.1</td>
    </tr>
    <tr>
      <td>Cloudy</td>
      <td>0.2</td>
      <td>0.6</td>
      <td>0.2</td>
    </tr>
    <tr>
      <td>Rainy</td>
      <td>0.3</td>
      <td>0.3</td>
      <td>0.4</td>
    </tr>
  </tbody>
</table>
  * Imagine these probabilities as a graph, where the weather is vertex and the connections between weather are edges
  * <strong>State</strong> - what the weather is on a certain day, i.e., the vertex.
  * <strong>Stationary Distribution<strong> - Let the day-to-day weather patterns happen over a very long period of time. Then the probability of weather type on a day in the distant future is independent of the weather today.
  * For a Markov chain to work:
    * The graph must be <strong>connected</strong> - there is a path from every vertex to every other vertex
    * The graph must be <strong>Strongly connected</strong> - there is a path from every vertext to every other vertex when considering direction
    * <strong>Persistence</strong> - Hence, over time, the probability of returning to where you started is 1.

* This one has Python code to do multivariate testing with Markov Chain Monte Carlo. Definitely worth studying [A/B Testing with Hierarchical Models in Python](https://blog.dominodatalab.com/ab-testing-with-hierarchical-models-in-python/)
* This seems like a very good resource to understand MCMC, but it is beyond my level of understanding currently:  [Stat 3701 Lecture Notes: Bayesian Inference via Markov Chain Monte Carlo (MCMC)](http://www.stat.umn.edu/geyer/3701/notes/mcmc-bayes.html)
* This one is okay, not as good: [An Introduction to MCMC
methods and Bayesian Statistics](https://www.ukdataservice.ac.uk/media/307220/presentation4.pdf)

-->

## Sources

* [Markov Chain Monte Carlo for Bayesian Inference - The Metropolis Algorithm](https://www.quantstart.com/articles/Markov-Chain-Monte-Carlo-for-Bayesian-Inference-The-Metropolis-Algorithm)
* Don't bother with this one: [A Zero-Math Introduction to Markov Chain Monte Carlo Methods](https://towardsdatascience.com/a-zero-math-introduction-to-markov-chain-monte-carlo-methods-dcba889e0c50) - this one is explains Markov Chains and Monte Carlo well, but devotes no more than couple sentences to MCMC because the author doesn't get it himself.
* [Markov Chain Monte Carlo Without all the Bullshit](https://jeremykun.com/2015/04/06/markov-chain-monte-carlo-without-all-the-bullshit/)
* [How would you explain Markov Chain Monte Carlo (MCMC) to a layperson?](https://stats.stackexchange.com/questions/165/) - the first response isn&squo;t good, but the rest are great.
