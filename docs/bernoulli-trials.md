### Bernoulli Trials, Binomial Distributions

An experiment that only has two possible results, *success* and *failure*, can be called a Bernoulli Trial if:
* The results are mutually exclusive,
* The probability of these two results do not change each time the experiment is done
* **Bernoulli Distribution** - a distribution for a random variable defined as
    > ![Bernoulli Random Variable](https://user-images.githubusercontent.com/638189/48320500-e0b60a00-e5e8-11e8-8fc1-f1b316c3fe83.png)
* `X` follows a Bernoulli distribution with parameter `p` is `X ~ Ber(p)`
* Probability function:
  > ![Failure Probability Function](https://user-images.githubusercontent.com/638189/48320567-85d0e280-e5e9-11e8-8ad2-cac44548e809.png)
  > ![Success Probability Function](https://user-images.githubusercontent.com/638189/48320591-adc04600-e5e9-11e8-9b75-8e1a3732a2a0.png)
  * The probability of failure *1 - p* is sometimes called *q*
* Cumulative Distribution Function:
    > ![Distribution Function](https://user-images.githubusercontent.com/638189/48320683-769e6480-e5ea-11e8-8a15-d22a9ae925a9.png)
* **Binomial Coefficient** - the number of ways of picking *k* unordered outcomes from *n* possibilities, or "*n* choose *k*"
  > ![Binomial Coefficient](https://user-images.githubusercontent.com/638189/48592760-f17fbc00-e917-11e8-93ad-525242f6d083.png)
  * For example, <sub>4</sub>C<sub>2</sub> = 6
  * From a set of 4 numbers {1, 2, 3, 4} choosing 2 unordered numbers  will yield 6 subsets {1,2}, {1,3}, {1,4}, {2,3}, {2,4}, {3,4}
* **Binomial Distribution** is the model for *n* independent Bernoulli trials with a *p* probability, then `X ~ Bin(n,p)`
  * Therefore *Bin(1,p) = Ber(p)*
  > ![Binomial Distribution](https://user-images.githubusercontent.com/638189/48593528-27726f80-e91b-11e8-8e9e-783779803c55.png)
* The mean of a Bernoulli Trial is its probability *&mu; = p*
* [Variance of](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/MIT18_05S14_Reading5a.pdf) a Bernoulli Trial
  > ![bernoulli Variance](https://user-images.githubusercontent.com/638189/48450932-19371e80-e776-11e8-936a-342b373f99b8.png)
  * Proof

    |        Values *X*        |           0           |          1          |
    |:------------------------:|:---------------------:|:-------------------:|
    |        pmf *p(x)*        |        *(1-p)*        |         *p*         |
    | *(X - &mu;)<sup>2</sup>* | *(0 - p)<sup>2</sup>* | *(1-p)<sup>2</sup>* |

  * *Var(X) = (1 − p)p<sup>2</sup> + p(1 − p)<sup>2</sup> = (1 − p)p(1 − p + p) = (1 − p)p.*
* [Standard Deviation](https://math.stackexchange.com/questions/1716156/sd-of-a-bernoulli-trial) of a Bernoulli Trial
  > ![Bernoulli Standard Deviation](https://user-images.githubusercontent.com/638189/48321218-e282cc00-e5ee-11e8-8976-1e58630e981e.png)

## Examples

### What the probabilities of flipping *k* heads in 5 coin flips?

* The probability for heads is success *p* = 0.5, so failure is *1 - p* = 0.5
* The probabilities of 0 heads is 5 failures, 0.5<sup>5</sup> = 0.03125
* Likewise the probability of 5 heads 0.5<sup>5</sup> = 0.03125
  * <sub>5</sub>C<sub>0</sub> = 5!/(0!*5!) = 1
  * <sub>5</sub>C<sub>1</sub> = 5!/(1!*4!) = 5
  * <sub>5</sub>C<sub>2</sub> = 5!/(2!*3!) = 10
  * <sub>5</sub>C<sub>3</sub> = 5!/(3!*2!) = 10
  * <sub>5</sub>C<sub>4</sub> = 5!/(4!*1!) = 5
  * <sub>5</sub>C<sub>5</sub> = 5!/(5!*0!) = 1

    | value |    *a* | 0                      | 1                                   | 2                                    | 3                                   | 4                                   | 5                      |
    |-------|-------:|------------------------|-------------------------------------|--------------------------------------|-------------------------------------|-------------------------------------|------------------------|
    | pmf   | *p(a)* | *1(1 - p)<sup>5</sup>* | *5p<sup>1</sup>(1 - p)<sup>4</sup>* | *10p<sup>2</sup>(1 - p)<sup>3</sup>* | *10<sup>2</sup>(1 - p)<sup>3</sup>* | *5p<sup>1</sup>(1 - <sup>p</sup>)4* | *1(1 - p)<sup>5</sup>* |
    | pmf   | *p(a)* | 0.03125                | 0.15625                             | 0.3125                               | 0.3125                              | 0.15625                             |  0.03125               |
    | cdf   | *F(a)* | 0.03125                | 0.1875                              |                                  0.5 |                              0.8125 |                             0.99875 |                      1 |                   1 |

### What is the probability that passengers show up on a plane?

* The plane has 50 seats.
* All seats have been sold.
* For every passenger, there is a 5% chance they do not board.
 * In other words = *X = Bin(50, 0.95)*

* What is the probability that all 50 passengers show up?
  * 50 independent success, or 0.95<sup>50</sup> = 7.694%
* What is the probability that exactly 49 passengers show up?
  > ![plane ticket example 1](https://user-images.githubusercontent.com/638189/48598046-f2701800-e92e-11e8-9873-ce8685125980.png)
* What is the probability at least 48 passengers show up?
  * *P(X &ge; 48) = 1 - P(X = 50) - P(X = 49) = 72.06%


## Sources
* [Online equation editor](http://www.sciweavers.org/free-online-latex-equation-editor)
  * Bernoulli random variable: `X =\begin{cases}1 & success\\0 & failure\end{cases}`
  * Failure Probability: `P(X = 0) = 1 - p`
  * Success Probability: `P(X = 1) = p`
  * Distribution Function: `F(x) =\begin{cases}0 & x < 0\\1 - p & 0  \leq x < 1\\1 & x  \geq 1\end{cases}`
  * Binomial Coefficient: `_nC_k =  \begin{pmatrix}n \\k \end{pmatrix} = \frac{n!}{k!(n - k)!}`
  * Binomial Distribution: `P(X = k) = \begin{pmatrix}n \\k \end{pmatrix}p^{k}(1-p)^{n-k}     =   \big({\frac{n!}{k!(n - k)!}}\big)p^{k}(1-p)^{n-k}`
  * Bernoulli Variance: `Var(X) = p(1 - p)`
  * Bernoulli Standard Deviation: `\sigma =  \sqrt{p(1-p)} `
  * Coin flip example: `(\frac{5}{3})0.5^3(1 - 0.5)^{5 - 3} = (\frac{5}{3})0.5^3(0.5)^{2} = 0.05208 \overline{3} `
  * Plane ticket example 1: `P(X = 49) = \begin{pmatrix}50 \\49 \end{pmatrix}0.95^{49}(1-0.95)^{50-49} = 50 *0.95^{49}*0.05 = 0.2025`
* [Binomial Coefficient](http://mathworld.wolfram.com/BinomialCoefficient.html)
* [Some probabilistic models](http://www.est.uc3m.es/esp/nueva_docencia/getafe/economia/estadistica_I/doc_generica/Chapt1_Part-C_Print.pdf)
* [What is the difference and relationship between the binomial and Bernoulli distributions?](https://math.stackexchange.com/questions/838107/what-is-the-difference-and-relationship-between-the-binomial-and-bernoulli-distr)
* [SD of a bernoulli trial?](https://math.stackexchange.com/questions/1716156/sd-of-a-bernoulli-trial)
* [Variance of Discrete Random Variables](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/MIT18_05S14_Reading5a.pdf)
* [Markdown Tables Generator](https://www.tablesgenerator.com/markdown_tables)
