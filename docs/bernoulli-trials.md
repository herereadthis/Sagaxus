### Bernoulli Trials, Binomial Distributions

An experiment that only has two possible results - *success* and *failure* - is a **Bernoulli Trial** if:
* The results are mutually exclusive,
* The probability of these two results do not change each time the experiment is done
* **Bernoulli Distribution** - a distribution for a random variable defined as
    > ![Bernoulli Random Variable](./img/9885ccd3-9602-431f-a028-4a3ede2d189e.png)
* `X` follows a Bernoulli distribution with parameter `p` is `X ~ Ber(p)`
* Probability function:
  > ![Failure Probability Function](./img/b687c0d1-f61c-49e7-bda5-e74f9d3d773f.png)
  > ![Success Probability Function](./img/9f2cb1c2-bb2a-4ac1-8089-7996f6ab8c94.png)
  * The probability of failure *1 - p* is sometimes called *q*
* Cumulative Distribution Function:
    > ![Distribution Function](./img/78111350-ec3e-46c6-9fd3-a44cb923da9f.png)<!--
      F(x) =\begin{cases}0 & x < 0\\1 - p & 0  \leq x < 1\\1 & x  \geq 1\end{cases}
      -->
* **Binomial Coefficient** - the number of ways of picking *k* unordered outcomes from *n* possibilities, or "*n* choose *k*"
  > ![Binomial Coefficient](./img/f1166446-ab18-4655-93a3-7b8ab9d1bc5e.png)
  * For example, <sub>4</sub>C<sub>2</sub> = 6
  * From a set of 4 numbers {1, 2, 3, 4} choosing 2 unordered numbers  will yield 6 subsets {1,2}, {1,3}, {1,4}, {2,3}, {2,4}, {3,4}
* **Binomial Distribution** is the model for *n* independent Bernoulli trials with a *p* probability, then `X ~ Bin(n,p)`
  * Therefore *Bin(1,p) = Ber(p)*
  > ![Binomial Distribution](./img/ee2f4eba-449d-4790-bdbf-9d53da126aa6.png)<!--
    {P(X = k) =
    \begin{pmatrix}n \\k \end{pmatrix}p^{k}(1-p)^{n-k} =
    \big({\frac{n!}{k!(n - k)!}}\big)p^{k}(1-p)^{n-k}}
    -->
* **Mean** of a Bernoulli Trial is its probability *&mu; = p*
* **Expected Value** of a Bernoulli Trial is *E(X) = 0(1-p) + 1(p) = p*
* **Expected Value** of a Binomial distribution is *E(X) = np*
* [Variance of](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/MIT18_05S14_Reading5a.pdf) a Bernoulli Trial
  > ![bernoulli Variance](./img/5037bb01-1d16-40e5-b6e6-52921370204a.png)
  * Proof

    |        Values *X*        |           0           |          1          |
    |:------------------------:|:---------------------:|:-------------------:|
    |        pmf *p(x)*        |        *(1-p)*        |         *p*         |
    | *(X - &mu;)<sup>2</sup>* | *(0 - p)<sup>2</sup>* | *(1-p)<sup>2</sup>* |

  * *Var(X) = (1 − p)p<sup>2</sup> + p(1 − p)<sup>2</sup> = (1 − p)p(1 − p + p) = (1 − p)p.*
* [Standard Deviation](https://math.stackexchange.com/questions/1716156/sd-of-a-bernoulli-trial) of a Bernoulli Trial
  > ![Bernoulli Standard Deviation](./img/d35efa90-8c71-44a5-a4eb-85bb8e291928.png)

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
    |-------|-------:|------------------------|-------------------------------------|--------------------------------------|--------------------------------------|-------------------------------------|------------------------|
    | pmf   | *p(a)* | *(1 - p)<sup>5</sup>* | *5p<sup>1</sup>(1 - p)<sup>4</sup>* | *10p<sup>2</sup>(1 - p)<sup>3</sup>* | *10p<sup>3</sup>(1 - p)<sup>1</sup>* | *5p<sup>4</sup>(1 - p)* | *p<sup>5</sup>* |
    | pmf   | *p(a)* | 0.03125                | 0.15625                             | 0.3125                               | 0.3125                               | 0.15625                             |  0.03125               |
    | cdf   | *F(a)* | 0.03125                | 0.1875                              |                                  0.5 |                               0.8125 |                             0.99875 |                      1 |                   1 |

### What is the probability that passengers show up on a plane?

* The plane has 50 seats.
* All seats have been sold.
* For every passenger, there is a 5% chance they do not board.
 * In other words = *X = Bin(50, 0.95)*

* What is the probability that all 50 passengers show up?
  * 50 independent success, or 0.95<sup>50</sup> = 7.694%
* What is the probability that exactly 49 passengers show up?
  > ![plane ticket example 1](./img/4b653c69-4a4c-4222-b6d0-2e53fe534425.png)
* What is the probability at least 48 passengers show up?
  * *P(X &ge; 48) = 1 - P(X = 50) - P(X = 49) = 72.06%


## Sources
* [Online equation editor](http://www.sciweavers.org/free-online-latex-equation-editor)
  * Bernoulli random variable: `X =\begin{cases}1 & success\\0 & failure\end{cases}`
  * Failure Probability: `P(X = 0) = 1 - p`
  * Success Probability: `P(X = 1) = p`
  * Binomial Coefficient: `_nC_k =  \begin{pmatrix}n \\k \end{pmatrix} = \frac{n!}{k!(n - k)!}`
  * Bernoulli Variance: `Var(X) = p(1 - p)`
  * Bernoulli Standard Deviation: `\sigma =  \sqrt{p(1-p)}`
  * Coin flip example: `(\frac{5}{3})0.5^3(1 - 0.5)^{5 - 3} = (\frac{5}{3})0.5^3(0.5)^{2} = 0.05208 \overline{3} `
  * Plane ticket example 1: `P(X = 49) = \begin{pmatrix}50 \\49 \end{pmatrix}0.95^{49}(1-0.95)^{50-49} = 50 *0.95^{49}*0.05 = 0.2025`
* [Binomial Coefficient](http://mathworld.wolfram.com/BinomialCoefficient.html)
* [Some probabilistic models](http://www.est.uc3m.es/esp/nueva_docencia/getafe/economia/estadistica_I/doc_generica/Chapt1_Part-C_Print.pdf)
* [What is the difference and relationship between the binomial and Bernoulli distributions?](https://math.stackexchange.com/questions/838107/what-is-the-difference-and-relationship-between-the-binomial-and-bernoulli-distr)
* [SD of a bernoulli trial?](https://math.stackexchange.com/questions/1716156/sd-of-a-bernoulli-trial)
* [Variance of Discrete Random Variables](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/MIT18_05S14_Reading5a.pdf)
* [Markdown Tables Generator](https://www.tablesgenerator.com/markdown_tables)
