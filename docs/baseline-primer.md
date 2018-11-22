# Baseline Primer

Establish terms so we know we are talking about the same thing when we say a word.

## Probability

* **Probability** - *P* - the likelihood that an event will occur
  * If *p* = 0, the event will not occur.
  * If *p* = 1, the event will occur.
  * The probability of *A* happening is *P(A)*
  * The probability of *A* happening, given that *B* has occurred is *P(A|B)*
    > ![conditional probability](https://user-images.githubusercontent.com/638189/48657458-1a2eb100-e9ff-11e8-8a1e-797fd5740ab7.png)
  * Rewritten is the multiplication rule:
    > ![multiplication rule](https://user-images.githubusercontent.com/638189/48657485-6548c400-e9ff-11e8-9104-eeee08786db4.png)
* Example: What is the probability that you draw from a pack of cards 2 diamonds in a row?
  * Reworded: What is the probability that the second card drawn from a pack of cards is a diamond *P(D<sub>2</sub>|D<sub>1</sub>)*, given that the first card drawn was a diamond *P(D<sub>1</sub>)*?
  * If 1 card has been drawn from a pack of cards, the probability that diamond is drawn from the remaining cards is:
   * *P(D<sub>2</sub>|D<sub>1</sub>)* = 12/51
  * The probability of drawing a diamond as the first card is 1/4.
  * *P(D<sub>2</sub> &cap; D<sub>1</sub>) = *P(D<sub>2</sub>|D<sub>1</sub>)  * P(D<sub>1</sub>)* = 12/51 * 1/4 = 3/51
* **Mutually Exclusive** - two events cannot occur at the same time.
  * *A* is independent of *B* if *P(A|B) = P(A)*
* **Bayes' Theorem**
  > ![Bayes' Theorem](./img/48657490-7d204800-e9ff-11e8-94ab-b5aec7a3cd00.png)
  * Proof (divide both sides by *P(A)*:
    *P(B|A) * P(A) = P(A &cap; B) = P(A|B) * P(B)*
  * Let *H<sub>1</sub>* be the probability that the first coin toss is heads, and let *H<sub>2</sub>* be the probability that all 3 coin tosses are heads.
    * Then *P(H<sub>1</sub>|H<sub>A</sub>)* = 1, while *P(H<sub>A</sub>|H<sub>1</sub>)* = 1/4
  * **Sally Clark**
    * What is the probability that a mother's first 2 babies dies of SIDS? Are these events dependent or independent?
    * Given that a mother's first baby died of SIDS, what is the probability that her second baby will also die of SIDS?
    * Professor Sir Roy Meadow incorrectly concluded that these were 2 independent events, and famously said it was a "1 in 73 million" chance.
    * This false statistic lead to her false conviction in November 2009.
    * She was release on January 2003, but died in March 2007 from alcohol poisoning.

## Discrete Random Variables


* **Random Variable** - a variable with a value that determined by a chance event.
* A discrete sample space *&Omega;* is a finite set of outcomes {*&omega;<sub>1</sub>, &omega;<sub>2</sub>...*}. The probability of an outcome *&omega;* is *P(&omega;)*.
* **Discrete Probability Distribution** - a distribution that can be represented by a table. For example, there are only 4 outcomes from flipping a coin 2 times.

    | Number of Heads, x | Probability P(x) |
    |--------------------|------------------|
    | 0                  | 0.25             |
    | 1                  | 0.5              |
    | 2                  | 0.25             |
* **Probability Mass Function pmf** - the function for a discrete random variable
  * *p(a) = P(X = a)*, where 0 &le; *p(a)* &le; 1
* **Cumulative Distribution Function cdf** - the function that gives the total probabilities from minus infinity to *a*
  * *F(a) = P(X ≤ a)*
* Example: let the sample space *&Omega;* be 2 dice rolls, and let a random variable *M* be the maximum of 2 dice rolls. In other words M(1,4) = 4.

  | value |    *a* | 1    | 2    | 3    | 4     | 5     | 6     |
  |-------|-------:|------|------|------|-------|-------|-------|
  | pdf   | *p(a)* | 1/36 | 3/36 | 5/36 |  7/36 |  9/36 | 11/36 |
  | cdf   | *F(a)* | 1/36 | 4/36 | 9/36 | 16/36 | 25/36 | 36/36 |

  * *F(a)* only increases. If *a &le; b*, then *F(a) &le; F(b)*
  * 0 &le; *F(a)* &le; 1
* **Bernoulli Distributions** - See page on [Bernoulli Trials](https://github.com/herereadthis/sagaxus/blob/master/docs/bernoulli-trials.md)
* **Binomial Distributions** - See above

  * **Discrete Variable** - variables that can only be certain values, within a range. For example, the number of heads from *n* coin flips is a whole number between 0 and *n*. It cannot be fractions.
    * Discrete Variables can be **finite** or **infinite**. While coin flips that result with heads can be infinite, but selecting aces from a pack of cards is finite.
  * **Continuous Variable** - variables that be any value within a range. For example the height of a person selected from a population is continuous.
* **Probability Distribution** a table or equation that can describe every outcome and its probability of occurance.


## Discrete Mean and Variance

* **Discrete Mean** - the mean of a discete random variable X is also known as the **expected value** of X, E(X)
  > ![discrete mean](https://user-images.githubusercontent.com/638189/48657507-96c18f80-e9ff-11e8-90fe-00d8fb4e94bb.png)
  * Expected Value is the sum of every outcome times is probability.
  * For a variable *X* with mean *&mu;<sub>x</sub>* and a variable *Y* with mean *&mu;<sub>y</sub>*:
    * *&mu;<sub>x + y</sub>* = *&mu;<sub>x</sub>* + *&mu;<sub>y</sub>*
    * *&mu;<sub>x - y</sub>* = *&mu;<sub>x</sub>* - *&mu;<sub>y</sub>*
* **Discrete Variance** - a measure of how much the probability mass is spread out around the discrete mean.
  > ![Discrete variance](https://user-images.githubusercontent.com/638189/48657511-ae991380-e9ff-11e8-8355-608e84687093.png)
  * Where *X* is a random variable with a mean *E(X) = &mu;*
  * Variance is taking the weighted average of the squared distance to the mean. Squaring makes sure we are averaging non-negative values (the spread to the right doesn't cancel the spread to the left). Using expectation means we weigh the high-probability values more.
    * *&sigma;* has the same units as *X*
    * *Var(X)* has the same units as the square of *X*. If X is measured in inches, then *Var(X)* is inches squared.
* **Discrete Standard Deviation** - *&sigma;* - the square root of the variance
  > ![discrete standard deviation](https://user-images.githubusercontent.com/638189/48657514-ca041e80-e9ff-11e8-9e38-622a8af05922.png)
  * Because *&sigma;* and *X* have the same units, the standard deviation is measure of the spread.
* **Discrete Independence** - two random variables *X* and *Y* are independent if the probably of both of them happening is the product of their probabilities
  * *P(X = a, Y = b) = P(X = a) * P(X = b)*
  * *X* and *Y* are independent if *Var(X + Y)= Var(X) + Var(Y)*
  * For constants *a* and *b*, *Var(aX + b) = a<sup>2</sup>Var(X)*.
  * *Var(X) = E(X<sup>2</sup>) − E(X)<sup>2</sup>*

## Continuous Random Variables

* A random variable X is **continuous** if there is a function *f(x)* such that for any *c &le; d*, the probability density function is:
  > ![continuous pdf](https://user-images.githubusercontent.com/638189/48657522-e99b4700-e9ff-11e8-98a2-d0c6386005d0.png)
  * The pdf is always non negative *f(x) &ge; 0*
  * and the pdf across all ranges will equal 1
  > ![infinity pdf](https://user-images.githubusercontent.com/638189/48522569-2a9c2b80-e847-11e8-9962-081dc473b52a.png)
  * You have to integrate *f(x)* to get the probability
* **Median** - the value *x* for X where *P(X &le; x) = 0.5*
  * That is, *X* has equal probability of being above or below the median
* **Continuous Probability** - a distribution that is expressed as an equation called a **Probability Density Function**
    * a random variable *y* is a function of *x* such that *y = f(x)*
    * 0 &le; *y* &le; 1 for all values of *x*
    * The area of the curve created by the function is equal to 1
    * The probability that *y* occurs within the interval of *a* and *b* is equal to the area of the function curve from *a* to *b*
* **Cumulative Distribution Function cdf** - analogous to cmf
  * *F(x) = P(X &le; x)*
  * 0 &le; *F(x)* &le; 1
* **Uniform Distribution** - all outcomes in the range have equal probobability, aka same probability density
  * Parameters: *a, b*
  * Range: *[a, b]*
  * Notation: *U(a, b)*
  * Density: *f(x) = 1/(b - a)* for *a &le; x &le; b*
  * Distribution: *F(x) = (x - a)/(b - a)* for *a &le; x &le; b*
  * an example of uniform distribution is throwing darts at a dartboard and getting the angle drawn from a vertical line to the center to the dart
* **Exponential Distribution** - the probability of and outcome gets larger as *x* increases
  * Parameter: *&lambda;*
  * Range: [0, &infin;)
  * Notation: exp(&lambda;)
  * Density: *f(x) = &lambda;e<sup>-&lambda;x</sup>* for *0 &le; x*
  * Distribution: *F(x) = 1 - e<sup>-&lambda;x</sup>* for *x &ge; 0*
  * Example: waiting for a taxi to arrive. The longer you wait, the more likely it will arrive

### Normal Distribution

* Also known as a **Gaussian** Distribution, named after Carl Friedrich Gauss
* Parameters: *&mu;, &sigma;*
* Range: (-&infin;, &infin;)
* Notation: *N(&mu;,&sigma;<sup>2</sup>)*
* Density:
  > ![normal density](https://user-images.githubusercontent.com/638189/48657610-7bf01a80-ea01-11e8-850c-54c07d3b309a.png)
* **Standard normal distribution Z** - a normal distribution where *&mu;* = 0 and *&sigma;* = 1
* Let *X* be a random variable with *&mu;* mean and *&sigma;* standard deviation. Then:
  > ![Z](./img/5f680ec1-bf14-47c5-aec0-d0a7b31f39b6.png)
* [The probability that a value](http://courses.atlas.illinois.edu/spring2016/STAT/ST) *z* is between the mean and *Z*
  * *f(z) = &phi;(z) - 1/2* (probability density function pdf)
  * *P(-1 &le; Z &le; 1)* &asymp; 0.6827
  * *P(-2 &le; Z &le; 2)* &asymp; 0.9545
  * *P(-3 &le; Z &le; 3)* &asymp; 0.9973

## Expected Value, Variance, and Standard Deviation for Continuous Random Variables

* **Expected Value** - measures central tendency
  * *&mu; = E(X)*
  > ![expected value, continuous](https://user-images.githubusercontent.com/638189/48657589-f8362e00-ea00-11e8-8755-40993607cbcc.png)
* Expected Value of a standard normal distribution N(0,1) where *&mu; = 0* and *&sigma; = 1*
  > ![Expected Value standard](https://user-images.githubusercontent.com/638189/48657681-ce7e0680-ea02-11e8-8ea5-ac521c74e5fe.png)
* Example: let *X ~ U(0,1)* - for a range [0,1] and a density *f(x) = 1*
  > ![expected value uniform continuous](https://user-images.githubusercontent.com/638189/48657440-b4422980-e9fe-11e8-88ea-73c4f72b9674.png)
  * The range of Z is (-&infin;,&infin;)
* **Standard Deviation &sigma;** - measures spread or scale
* **Variance** - square of the standard deviation
  *&sigma;<sup>2</sup> = Var(X)*
  * The formula is the same as for discrete random variables *Var(X) = E((x - &mu;)<sup>2</sup>)*


## Central Limit Theorem

* **Law of Large Numbers** - the frequency of an event will converge on the probability of the event as the number of trials increase.
  * The average of many independent samples is close to the average of the population.
  > ![law of large numbers](https://user-images.githubusercontent.com/638189/48669423-6eef2c00-ead2-11e8-8fb2-559bbd693ab3.png)
* **Central Limit Theorem** - as more averages of independent samples is gathered, the distribution approaches a normal distribution
* **Standardization** - For a random variable *X* that has a normal distribution, the standardization is:
  > ![Z](./img/5f680ec1-bf14-47c5-aec0-d0a7b31f39b6.png)
  * *Z* has a mean of 0 and standard deviation 1
* Let *S<sub>n</sub>* the the sum of *X<sub>1</sub>, X<sub>1</sub>, ... , X<sub>n</sub>* random variables each with a mean &mu; and a standard deviation *&sigma;*. Then the weighted average of the random variables is:
  > ![clt](https://user-images.githubusercontent.com/638189/48669537-a5c64180-ead4-11e8-9885-ededb2b0302f.png)
* Mean
  > ![Expected Value Sum, Sample](https://user-images.githubusercontent.com/638189/48675521-dbe0e100-eb27-11e8-8fef-85909fae57d5.png)
* Variance
  > ![Variance Sum, Sample](https://user-images.githubusercontent.com/638189/48675533-fc10a000-eb27-11e8-8ed0-e67c6aa32ed2.png)
* Standard Deviation
  > ![Standard Deviation, sum, sample](./img/d40e14ea-3186-4877-937e-c32daac1597a.png)
* CLT: For large *n*,
  > ![large n](https://user-images.githubusercontent.com/638189/48675580-9e308800-eb28-11e8-9f9a-6dc3e99fe996.png)

### CLT Examples
  * See [Sampling Size page](https://github.com/herereadthis/sagaxus/blob/master/docs/sampling-size.md) for examples


## Sources

* Graph generator: [http://courses.atlas.illinois.edu/spring2016/STAT/STAT200/pnormal.html](http://courses.atlas.illinois.edu/spring2016/STAT/ST)
* [HTML Math Symbols, Math Entities, and ASCII Math Character Code Reference](https://www.toptal.com/designers/htmlarrows/math/)
* [Rules of Probability](https://stattrek.com/probability/probability-rules.aspx?Tutorial=AP)
* [Online equation editor](http://www.sciweavers.org/free-online-latex-equation-editor)
  * conditional probability: `P(A|B) = \frac{P(A \cap B)}{P(B)}`
  * multiplication rule: `P(A \cap B) = P(A|B) * P(B)`
  * Bayes' Theorem: `P(B|A) = \frac{P(A|B)*P(B)}{P(A)}`
  * discrete mean: `E(X) = \mu_{x} = \sum_{i=1}^n {x_{i} * P(x_{i}) }`
  * discrete variance: `Var(X) = E((X- \mu )^{2}) = \sum_{i=1}^n p({x_{i})(x_{i}- \mu )^{2} }`
  * discrete standard deviation: `\sigma = \sqrt{Var(X)}`
  * continuous pdf: `P(c \leq d) = \int_c^d f(x)dx`
  * infinity pdf: `P( -\infty   \leq X \leq \infty) =  \int_{-\infty}^\infty f(x) dx = 1`
  * Z: `Z = \frac{X -  \mu }{ \sigma }`
  * Normal density: `f(x) = \phi(z) = \frac{1}{\sigma \sqrt{2 \pi } }e^{\frac{-(x - \mu)^2}{2\sigma^2}}`
  * expected value, continuous: `E(X) =  \int_a^b xf(x)dx`
  * expected value, standard: `E(z) = \phi(z) = \frac{1}{ \sqrt{2 \pi } }e^{-z^2/2} \Big|_{-\infty}^{\infty} = 0`
  * expected value uniform continuous: `E(X) = \int_{0}^{1}xdx = \frac{x^2}{2}  \Big|_0^1 = \frac{1}{2}`
  * law of large numbers: `\lim_{n \rightarrow \infty} P(\left |  \overline{X} - \mu  \right | < a) = 1 `
  * Clt: ` \overline{X}_{n} = \frac{S_{n}}{n} = \frac{X_{1} + ... + X_{n}}{n} =  \big(\sum_{i=1}^nX_{i}\big)/n`
  * Expected Value Sum, Sample: `E(S_{n}) = n\mu, E( \overline{X}_{n}) =\mu`
  * Variance, Sum, Sample: `Var(S_{n}) = n\sigma^2, Var( \overline{X}_{n}) =\frac{\sigma^2}{n}`
  * Standard Deviation Sum, sample: `\sigma_{S_{n}} =\sqrt{n}\sigma, \sigma_{\overline{X}_{n}} =\frac{\sigma}{\sqrt{n}}`
  * large n: `\overline{Xn} \approx N(\mu, \frac{\sigma^2}{n}), S_n \approx N(n\mu, n\sigma^2), Zn \approx N(0,1))`
* [Better Online equation editor](https://www.codecogs.com/latex/eqneditor.php)
* [Markdown Tables Generator](https://www.tablesgenerator.com/markdown_tables)
* [Intruction to probability and statistics](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/)
* [Variance of Discrete Random Variables](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/MIT18_05S14_Reading5a.pdf)
