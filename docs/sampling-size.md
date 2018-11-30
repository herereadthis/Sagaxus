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
    > ![Margin of Error](./img/dd8573b2-eefb-4d3c-91c6-7bbb32c674d5.png)
  * Usually we don't know what the proportion is, but to maximize the margin of error, the proportion will be 50% to maximize the the formula
  * The maxima of *p(1 - p)* can be found by gettings its derivative: *1 - 2p = 0*
* Sample size:
  > ![Sample Size](./img/48326258-5a102580-e606-11e8-95b1-a6df859de965.png)
* Examples
  * What is the proportion of customers who buy an item after viewing a website on a certain day, with a 95% confidence level and 5% margin of error, if the website sees about 10,000 customers a day? If they are uncertain of their current conversion rate, then 384 customers.
    > ![Example 1](./img/ff3b6b07-32e1-4e83-9de6-cf2d3b09bb74.png)
  * If they know the conversion rate is 5%, then the sample size is 73.
    > ![Example 2](./img/09c9b0c3-cd0a-4888-831c-fcd5bd25c044.png)
* **Margin of Error, rule of thumb** - A sample of *n* people will have have a margin of error:
  > ![margin of error rule of thumb](./img/ffc64dd1-c3a4-490d-b5a1-7deb5c88ad9f.png)

## Central Limit Theorem, Examples

* See [Baseline Primer](./baseline-primer.md) page for description of CLT
* CLT
  > ![clt](./img/48669537-a5c64180-ead4-11e8-9885-ededb2b0302f.png)
* Mean
  > ![Expected Value Sum, Sample](./img/48675521-dbe0e100-eb27-11e8-8fef-85909fae57d5.png)
* Variance
  > ![Variance Sum, Sample](./img/48675533-fc10a000-eb27-11e8-8ed0-e67c6aa32ed2.png)
* Standard Deviation
  > ![Standard Deviation, sum, sample](./img/d40e14ea-3186-4877-937e-c32daac1597a.png)
* Out of 100 coin flips, what is the probability of more than 55 heads?
  * **Standardization** - For a random variable *X* that has a normal distribution, the standardization is:
  > ![Z](./img/5f680ec1-bf14-47c5-aec0-d0a7b31f39b6.png)
  * Let *X<sub>j</sub>* be the result of the *j<sup>th</sup>* flip, and *X<sub>j</sub>* = 1 for heads and *X<sub>j</sub>* = 0 for tails
  * The sum of all the heads for 100 flips will then be *S = X<sub>1</sub> + X<sub>1</sub> + X<sub>2</sub> + ... + X<sub>100</sub>*
  * Each coin flip is a Bernoulli Trial
    * Expected Value: *E(X) = p* = 0.5
    * Variance: *Var(X)* = (1 -*p*)*p* = 0.5 * 0.5 = 0.25
    * Standard Deviation of *X* is square root of its variance: 0.5
    * Expected Value of Sum of 100 coin flips *E(S)* = 0.5 * 100 = 50
    * *Var(S) = n&sigma;<sup>2</sup>* = 100 * 0.5<sup>2</sup> = 25*
    * Standard Deviation of *S* is square root of its variance: 5
    > ![55 coin example](./img/e61b6506-ba9c-4133-aff7-f1e82fa0bb7b.png)
    * Another way to think of this problem is 55 is 1 standard deviation over the mean. What is the left tail over 1 standard deviation?

## How big should the sampling size be?

1. Run the test for *n* (e.g. 1000) observations
2. Run the test until a significant difference is observed

Suppose observations are made on a test after 200 and stopped after 500 observations.

<table>
    <tr>
      <th>Phase</th>
      <th>Scenario 1</th>
      <th>Scenario 2</th>
      <th>Scenario 3</th>
      <th>Scenario 4</th>
    </tr>
    <tr>
      <td>200 observations</td>
      <td>Don't reject <em>H<sub>0</sub></em></td>
      <td>Don't reject <em>H<sub>0</sub></em></td>
      <td bgColor="#CCFFCC">Reject <em>H<sub>0</sub></em></td>
      <td bgColor="#CCFFCC">Reject <em>H<sub>0</sub></em></td>
    </tr>
    <tr>
      <td>500 observations</td>
      <td>Don't reject <em>H<sub>0</sub></em></td>
      <td bgColor="#CCFFCC">Reject <em>H<sub>0</sub></em></td>
      <td>Don't reject <em>H<sub>0</sub></em></td>
      <td bgColor="#CCFFCC">Reject <em>H<sub>0</sub></em></td>
    </tr>
    <tr>
      <td>End Result</td>
      <td>Don't reject <em>H<sub>0</sub></em></td>
      <td bgColor="#CCFFCC">Reject <em>H<sub>0</sub></em></td>
      <td>Don't reject <em>H<sub>0</sub></em></td>
      <td bgColor="#CCFFCC">Reject <em>H<sub>0</sub></em></td>
    </tr>
</table>


Suppose the test is stopped after something significant happens.


<table>
    <tr>
      <th>Phase</th>
      <th>Scenario 1</th>
      <th>Scenario 2</th>
      <th>Scenario 3</th>
      <th>Scenario 4</th>
    </tr>
    <tr>
      <td>200 observations</td>
      <td>Don't reject <em>H<sub>0</sub></em></td>
      <td>Don't reject <em>H<sub>0</sub></em></td>
      <td bgColor="#CCFFCC">Reject <em>H<sub>0</sub></em></td>
      <td bgColor="#CCFFCC">Reject <em>H<sub>0</sub></em></td>
    </tr>
    <tr>
      <td>End Result</td>
      <td>Don't reject <em>H<sub>0</sub></em></td>
      <td bgColor="#CCFFCC">Reject <em>H<sub>0</sub></em></td>
      <td>Stop</td>
      <td>Stop</td>
    </tr>
    <tr>
      <td>500 observations</td>
      <td>Don't reject <em>H<sub>0</sub></em></td>
      <td bgColor="#CCFFCC">Reject <em>H<sub>0</sub></em></td>
      <td bgColor="#CCFFCC">Reject <em>H<sub>0</sub></em></td>
      <td bgColor="#CCFFCC">Reject <em>H<sub>0</sub></em></td>
    </tr>
</table>




<table>
  <tr>
    <td>Type I Error <em>&alpha;</em></td>
    <td>Probability of rejecting <em>H<sub>0</sub></em> even though it's true</td>
  </tr>
  <tr>
    <td>Type II Error <em>&beta;</em></td>
    <td>Probability of not rejecting <em>H<sub>0</sub></em> even though it's false</td>
  </tr>
  <tr>
    <td>1 - <em>&beta;</em></td>
    <td><strong>Power</strong> - probability of rejecting <em>H<sub>0</sub></em> when it's false</td>
  </tr>
  <tr>
    <td><em>&sigma;<sup>2</sup><sub>0</sub></em> and em>&sigma;<sup>2</sup><sub>A</sub></em></td>
    <td>Variances of <em>H<sub>0</sub></em> and <em>H<sub>A</sub></em></td>
  </tr>
  <tr>
    <td><em>&mu;<sub>0</sub></em> and <em>&mu;<sub>A</sub></em></td>
    <td>Means of <em>H<sub>0</sub></em> and <em>H<sub>A</sub></em></td>
  </tr>
  <tr>
    <td><em>n<sub>0</sub></em> and <em>n<sub>A</sub></em></td>
    <td>Sample sizes of <em>H<sub>0</sub></em> and <em>H<sub>A</sub></em></td>
  </tr>
</table>


## power analysis for two independent proportions

## Power Analysis for 2 Independent Proportions

* We want to determine the size of two samples with binomial distributions such that there is a &delta; difference between the two.
* For example, if sample 1 has probability of 0.1 and we want to [detect a 10% difference](https://signalvnoise.com/posts/3004-ab-testing-tech-note-determining-sample-size) between sample 2, then sample 2 should have a probability of 0.11
  * **Sensitivity** - the size of the difference
  * **Power Analysis** - a tool to determine the minimum sample size required to be reasonably confident that a meaningful difference can be detected between two values
  * **Independent** - these two samples, A and B don't depend on each other
  * **Proportins** - dealing with binomial distributions
> ![power analysis sample size](./img/e024f979-3713-4e78-b8ba-95dbfb9d3244.png)
* Example
  * With a current conversion rate of 10%, we want to detect a 10% difference
  * The treatment should at least have a 0.10 * (1 + 0.1) = 0.11 conversion rate
  * Want a power of 80% (*&beta;* = 0.8) and a 5% significance level (*&alpha;* = 0.05), [we get](https://select-statistics.co.uk/calculators/sample-size-calculator-two-proportions/):
  > ![power analysis example](./img/3e032b44-760b-4512-80db-da8620a4e918.png)

> ![rule of thumb](./img/6021db58-dfd6-4627-b348-fe20164912d7.png)

> ![delta](./img/0dab0e25-4f83-4fb6-80fa-539958a732af.png)

> ![sample size, 2 population means](./img/739f753e-8b54-49c7-95c2-6c481d2aa628.png)

## Sources

* [Critical Values of *z*](http://www.math.armstrong.edu/statsonline/5/5.3.2.html)
* [Online equation editor](http://www.sciweavers.org/free-online-latex-equation-editor)
  * interval estimateion: `\mu =  \overline{x}  \pm ME = \overline{x}  \pm z_{ \alpha/ 2}\frac{ \sigma }{ \sqrt{n} }`
  * Margin of Error: `Z_{ \alpha / 2}  \sqrt{\frac{p(1 - p)}{n}}  \leq ME`
  * Sample Size: `n = \frac{p(1-p)}{(\frac{ME}{Z_{ \alpha / 2}})^2}`
  * Example 1: `\frac{0.5 * 0.5}{(\frac{0.05}{1.96})^2}  \approx  384`
  * Example 2: `\frac{0.95 * 0.05}{(\frac{0.05}{1.96})^2}  \approx  73`
  * 55 coin example `P(S > 55) = P\left ( \frac{S-50}{5} > \frac{55-50}{5} \right ) \approx P(Z > 1) = 0.16`
  * margin of error rule of thumb: `ME = 1\pm\sqrt{n}`
  * rule of thumb: `n = \frac{16}{\Delta^{2}}`
  * delta: `\Delta = \frac{\mu_{0} - \mu_{1}}{\sigma} = \frac{\delta}{\sigma}`
  * sample size, 2 population means: `  n= \frac{2(z_{1-\alpha/2}+z_{1-\beta})^{2}}{\left (  \frac{\mu_{0} - \mu_{1}}{\sigma}  \right )^{2}}`
  * power analysis sample size: `n = (Z_{\alpha/2}+Z_{1-\beta})^{2}* \frac{p_1(1-p_1)+p_2(1-p_2) }{(p_1-p_2)^2}`
  * power analysis example: `n = (1.96+0.84)^{2}\frac{0.1879}{(0.01)^2}  = 14748`
* [How Not To Run an A/B Test](https://www.evanmiller.org/how-not-to-run-an-ab-test.html)
* [Sample Size](http://vanbelle.org/chapters%5Cwebchapter2.pdf)
* [A/B Testing Tech Note: determining sample size](https://signalvnoise.com/posts/3004-ab-testing-tech-note-determining-sample-size)
* [Comparing Two Proportions – Sample Size](https://select-statistics.co.uk/calculators/sample-size-calculator-two-proportions/)
