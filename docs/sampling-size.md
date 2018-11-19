# Sampling Size

How many samples from a population do you need to see whether they possess a particular property, within a margin of error?

* **Critical Value** - the area under a normal distribution curve.
  * There is an 80% probability a result will fall within 1.28 standard deviations of the mean. So 1.28 is the critical value of *z* that corresponds to central area of 0.80.
  * *&alpha;* is the tail area. For a 0.80 central area, then there are 0.10 tail areas on either side of the curve.
  * Z-table, 2 tails
    * e.g., *P(|Z| < 1)* = 0.68 - the probability that that normal random variable is within 1 standard deviation of its mean.
  
    | confidence % | critical value | &alpha;/2             |
    |--------------|----------------|-----------------------|
    | 68.27%       | **1.000**      | *z<sub>0.159</sub>*   |
    | 80%          | 1.282          | *z<sub>0.1</sub>*     |
    | 90%          | 1.645          | *z<sub>0.05</sub>*    |
    | 95%          | 1.960          | *z<sub>0.025</sub>*   |
    | 95.45%       | **2.000**      | *z<sub>0.02275</sub>* |
    | 96%          | 2.054          | *z<sub>0.02</sub>*    |
    | 98%          | 2.326          | *z<sub>0.01</sub>*    |
    | 99.73%       | **3.000**      | *z<sub>0.00135</sub>* |
    | 99.8%        | 3.090          | *z<sub>0.001</sub>*   |
    | 99.9%        | 3.291          | *z<sub>0.0005</sub>*  |
    | 99.99%       | 3.891          | *z<sub>0.00005</sub>* |

* Margin of Error formula
  * where Z<sub>&alpha;/2</sub> is the critical value,
  * *p* is the proportion,
  * *n* is sample size,
  * *&sigma;* is standard deviation
    > ![interval estimation](./img/48491707-2a277480-e7f6-11e8-8632-19a6d0daf3b2.png)
  * For a binomial distribution, the standard deviation is the square root of the proportion times the inverse proportion
    > ![Margin of Error](./img/48325466-b1f95d00-e603-11e8-92cd-7502e202f77a.png)
  * Usually we don't know what the proportion is, but to maximize the margin of error, the proportion will be 50% to maximize the the formula
* Sample size:
  > ![Sample Size](./img/48326258-5a102580-e606-11e8-95b1-a6df859de965.png)
* Examples
  * What is the proportion of customers who buy an item after viewing a website on a certain day, with a 95% confidence level and 5% margin of error, if the website sees about 10,000 customers a day? If they are uncertain of their current conversion rate, then 384 customers.
    > ![Example 1](./img/ff3b6b07-32e1-4e83-9de6-cf2d3b09bb74.png)
  * If they know the conversion rate is 5%, then the sample size is 73.
    > ![Example 2](./img/09c9b0c3-cd0a-4888-831c-fcd5bd25c044.png)

## Central Limit Theorem, Examples

* CLT
  > ![clt](./img/48669537-a5c64180-ead4-11e8-9885-ededb2b0302f.png)
* Mean
  > ![Expected Value Sum, Sample](./img/48675521-dbe0e100-eb27-11e8-8fef-85909fae57d5.png)
* Variance
  > ![Variance Sum, Sample](./img/48675533-fc10a000-eb27-11e8-8ed0-e67c6aa32ed2.png)
* Standard Deviation
  > ![Standard Deviation, sum, sample](./img/48675542-1d718c00-eb28-11e8-9da9-2e556ed992b2.png)
* Out of 100 coin flips, what is the probability of more than 55 heads?
  * Let *X<sub>j</sub>* be the result of the *j<sup>th</sup>* flip, and *X<sub>j</sub>* = 1 for heads and *X<sub>j</sub>* = 0 for tails
  * The sum of all the heads for 100 flips will then be *S = X<sub>1</sub> + X<sub>1</sub> + X<sub>2</sub> + ... + X<sub>100</sub>*
  * Each coin flip is a Bernoulli Trial
    * Expected Value: *E(X) = p* = 0.5
    * Variance: *Var(X)* = (1 -*p*)*p* = 0.5 * 0.5 = 0.25
    * Standard Deviation of *X* is square root of its variance: 0.5
    * Expected Value of Sum of 100 coin flips *E(S)* = 0.5 * 100 = 50
    * *Var(S) = n&sigma;<sup>2</sup>* = 100 * 0.5<sup>2</sup> = 25*
    * Standard Deviation of *S* is square root of its variance: 5


## Sources

* [Critical Values of *z*](http://www.math.armstrong.edu/statsonline/5/5.3.2.html)
* [Online equation editor](http://www.sciweavers.org/free-online-latex-equation-editor)
  * interval estimateion: `\mu =  \overline{x}  \pm ME = \overline{x}  \pm z_{ \alpha/ 2}\frac{ \sigma }{ \sqrt{n} }`
  * Margin of Error: `Z_{ \alpha / 2}  \sqrt{\frac{p(1 - p)}{n}}  \leq ME`
  * Sample Size: `n = \frac{p(1-p)}{(\frac{ME}{Z_{ \alpha / 2}})^2}`
  * Example 1: `\frac{0.5 * 0.5}{(\frac{0.05}{1.96})^2}  \approx  384`
  * Example 2: `\frac{0.95 * 0.05}{(\frac{0.05}{1.96})^2}  \approx  73
`
