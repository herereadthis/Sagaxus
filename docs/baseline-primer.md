# Baseline Primer

Establish terms so we know we are talking about the same thing when we say a word.

## Probability

* **Probability** - *P* - the likelihood that an event will occur
  * If *p* = 0, the event will not occur.
  * If *p* = 1, the event will occur.
* **Law of Large Numbers** - the frequency of an event will converge on the probability of the event as the number of trials increase.
* **Mutually Exclusive** - two events cannot occur at the same time.
* **Random Variable** - a variable with a vaule that determined by a chance event.
  * **Discrete Variable** - variables that can only be certain values, within a range. For example, the number of heads from *n* coin flips is a whole number between 0 and *n*. It cannot be fractions.
    * Discrete Variables can be **finite** or **infinite**. While coin flips that result with heads can be infinite, but selecting aces from a pack of cards is finite.
  * **Continuous Variable** - variables that be any value within a range. For example the height of a person selected from a population is continuous.
* **Probability Distribution** a table or equation that can describe every outcome and its probability of occurance.
  * **Discrete** - a distribution that can be represented by a table. For example, there are only 4 outcomes from flipping a coin 2 times.

    | Number of Heads, x | Probability P(x) |
    |--------------------|------------------|
    | 0                  | 0.25             |
    | 1                  | 0.5              |
    | 2                  | 0.25             |

  * **Continuous** - a distribution that is expressed as an equation called a **Probability Density Function**
    * a random variable *y* is a function of *x* such that *y = f(x)*
    * 0 &le; *y* &le; 1 for all values of *x*
    * The area of the curve created by the function is equal to 1
    * The probability that *y* occurs within the interval of *a* and *b* is equal to the area of the function curve from *a* to *b*

## Mean and Variance

* **Discrete Mean** - the mean of a discete random variable X is also known as the **expected value** of X, E(X)
  > ![discrete mean](https://user-images.githubusercontent.com/638189/48450361-dd9b5500-e773-11e8-8384-300a6c1fc2e0.png)
  * Expected Value is the sum of every outcome times is probability.
  * For a variable *X* with mean *&mu;<sub>x</sub>* and a variable *Y* with mean *&mu;<sub>y</sub>*:
    * *&mu;<sub>x + y</sub>* = *&mu;<sub>x</sub>* + *&mu;<sub>y</sub>*
    * *&mu;<sub>x - y</sub>* = *&mu;<sub>x</sub>* - *&mu;<sub>y</sub>*
* **Discrete Variance** - a measure of how much the probability mass is spread out around the discrete mean.
  > ![Discrete variance](https://user-images.githubusercontent.com/638189/48450704-48995b80-e775-11e8-8445-04a36a0f3d49.png)
  * Where *X* is a random variable with a mean *E(X) = &mu;*
  * Variance is taking the weighted average of the squared distance to the mean. Squaring makes sure we are averaging non-negative values (the spread to the right doesn't cancel the spread to the left). Using expectation means we weigh the high-probability values more.
    * *&sigma;* has the same units as *X*
    * *Var(X)* has the same units as the square of *X*. If X is measured in inches, then *Var(X)* is inches squared.
* **Discrete Standard Deviation** - *&sigma;* - the square root of the variance
  > ![discrete standard deviation](https://user-images.githubusercontent.com/638189/48450556-aa0cfa80-e774-11e8-9ab4-3fcc5548a61e.png)
  * Because *&sigma;* and *X* have the same units, the standard deviation is measure of the spread.
* **Discrete Independence** - two random variables *X* and *Y* are independent if the probably of both of them happening is the product of their probabilities
  * *P(X = a, Y = b) = P(X = a) * P(X = b)*
  * *X* and *Y* are independent if *Var(X + Y)= Var(X) + Var(Y)*
  * For constants *a* and *b*, *Var(aX + b) = a<sup>2</sup>Var(X)*.
  * *Var(X) = E(X<sup>2</sup>) − E(X)<sup>2</sup>*

## Sources

* [Rules of Probability](https://stattrek.com/probability/probability-rules.aspx?Tutorial=AP)
* [Online equation editor](http://www.sciweavers.org/free-online-latex-equation-editor)
  * discrete mean: `E(X) = \mu_{x} = \sum_{i=1}^n {x_{i} * P(x_{i}) }`
  * discrete variance: `Var(X) = E((X- \mu )^{2}) = \sum_{i=1}^n p({x_{i})(x_{i}- \mu )^{2} }`
  * discrete standard deviation: ` \sigma  =  \sqrt{Var(X)} `
* [Markdown Tables Generator](https://www.tablesgenerator.com/markdown_tables)
* [Intruction to probability and statistics](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/)
* [Variance of Discrete Random Variables](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/MIT18_05S14_Reading5a.pdf)
