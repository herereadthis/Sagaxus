# Beta Distribution

* The beta distribution is mostly considered within the context of Bayesian statistics.
* Levels of distributions
  * Bernoulli Trials: probability of success/ failure, e.g., one coin flip
  * Binomial Distribution: proportion of success, e.g, number of heads, given <em>n</em> coin flips
  * Beta Distribution: probability of success given proportion of success, e.g., probability of fair coin, given <em>&alpha;</em> heads and <em>&beta;</em> tails.

### Baseball

* A player's batting average is the proportion of hits to total number of plate appearances.
  * Anything above .300 is very good, anything below .215 is terrible
  * At the beginning a season the batting average is meaningless if you ignore prior knowledge
    * A player scoring a hit from 2 plate appearance has .500 average
    * A player striking out in first 1 appearances has a .000 average
    * Suppose last season a player had 80 hits and 220 outs for a total of 300 at-bats
    * The batting average of this player is a [beta distribution](http://varianceexplained.org/statistics/beta_distribution_and_baseball/) *beta(80,220)*

* **Beta Distribution** - beta(a, b) 2-parameter distribution with range [0,1]
  > ![Beta distribution](./img/56786ea0-b970-49d0-9a4a-b5fc2c891c13.png)<!--
    {f(\theta) = \frac{(a+b-1)!}{(a-1)!(b-1)!}\theta^{a-1}(1-\theta)^{b-1}}
    -->
* *a* and *b* are called **hyperparameters**, they are different than the hypothesis parameter *&theta;*
* That fraction area is called a normalizing constant
  > ![normalizing constant](./img/c5d1c8a8-d6a1-4629-ac87-0321d01de1f6.png)<!--
    {c = \frac{(a+b-1)!}{(a-1)!(b-1)!}, c\theta^{a-1}(1-\theta)^{b-1}}
    -->
* Beta mean
  > ![beta mean](./img/cc95317e-c7b9-4418-8e3b-63d6d0d53000.png)<!--
    {E(X) = \mu = \frac{\alpha}{\alpha + \beta}}
    -->
* What is the probability of getting 8 heads and 4 tails from a coin flip?
  * n = 8 + 4 = 12
  * This is a binomial distribution
  > ![Binomial Distribution](./img/ee2f4eba-449d-4790-bdbf-9d53da126aa6.png)
  * The posterior pdf for a binomial distribution is also a binomial distribution since we are still dealing with bernoulli trials
  * If we solve for the posterior with *&theta;* from 0 to 1, the answer must be 1 - that is the normalizing constant
  > ![Beta Posterior](./img/c7b2de3b-bc90-46df-a92e-678e4a4fc2c4.png)
  * We had 8 heads and 4 tails before
    * 8 = a - 1, a = 9
    * 4 = b - 1, b = 5
  * **likelihood** What is the probability of getting *k* successes out of *n* samples?
  * The posterior for a coin with 8 heads and 5 tails is therefore a *beta(9,5)* distribution

<table>
    <tr>
        <th>hypothesis</th>
        <th>prior</th>
        <th>likelihood</th>
        <th>Bayes Numerator</th>
        <th>Posterior</th>
    </tr>
    <tr>
        <td><img
            alt="\theta"
            src="./img/6384aa3f-acfd-436a-bea7-6961839deb07.png" /></td>
        <td><img
            alt="1 \cdot d\theta"
            src="./img/c912ead2-ee1a-4f4d-a2fc-a99c16601a0d.png" /></td>
        <td><img
            alt="\begin{pmatrix}12 \\8 \end{pmatrix}\theta^{8}(1-\theta)^{4}"
            src="./img/7a76e220-b451-40af-9088-79d4a6d33979.png" /></td>
        <td><img
            alt="\begin{pmatrix}12 \\8 \end{pmatrix}\theta^{8}(1-\theta)^{4}d\theta"
            src="./img/e35d1363-2c11-4af1-ab47-06792c2e9ce7.png" /></td>
        <td><img
            alt="c_2\theta^{8}(1-\theta)^{4}d\theta"
            src="./img/59af6c9d-847f-48a1-b8e0-20da5bd7763a.png" /></td>
    </tr>
</table>

* what about tossing the coin again, getting *n* heads and *m* tails?
* What about tossing the coin *N* times again, getting *x* heads (successes)?


<table>
    <tr>
        <th>hypothesis</th>
        <th>prior</th>
        <th>likelihood</th>
        <th>Bayes Numerator</th>
        <th>Posterior</th>
    </tr>
    <tr>
        <td><em>&theta;</em></td>
        <td><em>x</em></td>
        <td><em>beta(a, b)</em></td>
        <td><em>Bin(n + m, &theta;)</em></td>
        <td><em>beta(a + n,b+m)</em></td>
    </tr>
    <tr>
        <td><img
            alt="\theta"
            src="./img/6384aa3f-acfd-436a-bea7-6961839deb07.png" /></td>
        <td><img
            alt="x"
            src="./img/c2eb2bdd-4e87-4c24-a1bb-e75fe74e4d97.png" /></td>
        <td><img
            alt="c_1\theta^{a-1}(1-\theta)^{b-1}d\theta"
            src="./img/df86bc72-42a7-45cb-8684-72c04ee31b8b.png" /></td>
        <td><img
            alt="c_2\theta^{x}(1-\theta)^{N-x}"
            src="./img/ad18c07b-0d54-44e7-8fda-f6c2ff054959.png" /></td>
        <td><img
            alt="c_3\theta^{a+x-1}(1-\theta)^{b+N-x-1}"
            src="./img/6f973f55-8bfe-4212-9dbe-2b134ba630bc.png" /></td>
    </tr>
</table>

* Prior Constant
> ![c1](./img/e2e7e975-71d0-4a3c-b865-b47531751055.png)<!--
  c_1 = \frac{(a+b-1)!}{(a-1)!(b-1)!} -->
* Likelihood Constant
  > ![c2](./img/6f15ce85-f7c5-40ba-be15-bc4f2c547e88.png)<!--
  c_2 = \begin{pmatrix}N \\x \end{pmatrix} = \frac{N!}{x!(N-x)!} -->
* Posterior Constant
  > ![c3](./img/b2e3b028-aa45-465e-840c-be212c0256d8.png)<!--
  c_3 = \frac{(a+b+N-1)!}{(a+x-1)!(b+N-x-1)!} -->

* [Expected Value](http://pj.freefaculty.org/guides/stat/Distributions/DistributionWriteups/Beta/Beta.pdf)
  > ![beta mean](./img/5d6b37fc-580a-4a9f-a792-efdef29d3811.png)
* Variance
  > ![beta variance](./img/e02cd9d5-1f08-47fa-aaf7-df630154d91f.png)
* Mode peak of the curve
  > ![beta mode](./img/f2b2fc98-70aa-45dc-8932-4481bb377b43.png)
  * notice that the peak of the curve approaches the expected value as the hyperparamters get larger

### Conjuate Priors

* **Conjugate Prior** - if the posterior is the same probability distribution family as the the prior, then they are conjugate distributions
  * If the likelihood function is binomial and the the prior distribution is beta, then the posterior is also beta
* *No more integrals of integrals*

### Inferential Statistics

[Try to infer these things](https://www.probabilisticworld.com/frequentist-bayesian-approaches-inferential-statistics/):

* **Parameter estimation** - some value that determines the properties of the distribution, such as \mu or \sigma
* **Data Prediction** - use information about sample to predict a random selection
* **Model comparison** - selecting a model which best explains the observed data, something that postulates the relationship between factors and the data


## Sources

* [Online equation editor](https://www.codecogs.com/latex/eqneditor.php)
  * get beta
    * beta distribution: ``
    * normalizing constant: `{c = \frac{(a+b-1)!}{(a-1)!(b-1)!}, c\theta^{a-1}(1-\theta)^{b-1}}`
    * beta posterior: `c_2\int_0^1 \theta^{a-1}(1-\theta)^{b-1}d\theta`
    * beta mean: `E(\theta) = \mu = \frac{a}{a+b}`
    * beta variance: `\sigma^2  = \frac{a\cdot b}{(a+b)^2(a + b + 1)}`
    * beta mode: `\gamma  = \frac{a-1}{a+b-2}`
* [Beta Distributions](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/MIT18_05S14_Reading14a.pdf)
* [Beta Distribution](http://pj.freefaculty.org/guides/stat/Distributions/DistributionWriteups/Beta/Beta.pdf)
* [Understanding the beta distribution (using baseball statistics)](http://varianceexplained.org/statistics/beta_distribution_and_baseball/)
