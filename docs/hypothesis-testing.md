# Hypothesis Testing

* **Hypothesis** - a premise or claim that we want to test.
*
* The null and alternative hypothesis are mathematical opposites. Together, they must allow for all possible answers
* **Neyman-Pearson Paradigm** - If the data is well outside the what is expected under the null hypothesis, then reject the null hypothesis.
* **Difference from Bayesian updating**
  * The evidence of the data will be considered through the likelihood function, not prior beliefs.
  * Need a notion of data considered "extreme," or outside what is expected.
* **Null Hypothesis Significance Testing (NHST)** - compare an observed statistic against a hypothetical distribution aka test distribution
  * **Null Hypothesis (*H<sub>0</sub>*)** - Currently accepted value for a parameter.
  * **Alternate Hypothesis (*H<sub>A</sub>*)** - Claim to be tested, aka "research hypothesis"
  * **Test Statistic (*X*)** - is calculated from the sample data, and is used make a decision
  * **Null Distribution** - the probability distribution of *X* assuming *H<sub>0</sub>*
  * **Rejection Region** - where *X* would be in order to reject *H<sub>0</sub>* for *H<sub>A</sub>*
  * **Non-Rejection Region** - where *X* would be in order not to reject *H<sub>0</sub>* for *H<sub>A</sub>*
    - "Do not reject" is not the same as "accept!"
  * Example:
    * A candy machine makes chocolate bars that weight 5g on average. A work claims the machine no longer makes 5g bars.
      * *H<sub>0</sub>*: *&mu; = 5g*
      * *H<sub>A</sub>*: *&mu; &ne; 5g*
* Example: flip a coin 10 times. Let *&theta;* be the probability that a coin flip lands heads.
  * Null Hypothesis *H<sub>0</sub>*  - *&theta;* - 0.5, aka "the coin is fair"
  * Alternative Hypothesis *H<sub>A</sub>* - *&theta;* &ne; 0.5, aka "the coin is rigged"
  * *p*(*x*|*&theta;* = 0.5) ~ *Bin*(10, 0.5) - Binomial distribution
  * **Standardization** - For a random variable *X* that has a normal distribution, the standardization is:
  > ![Z](./img/5f680ec1-bf14-47c5-aec0-d0a7b31f39b6.png)
    * Variance of sum is 10 * 0.5<sup>2</sup> = 2.5
    * *&sigma;* of sum is 1.15811
  * table for the null distribution

    <table>
      <tr>
        <th><em>x</em></th>
        <th>0</th>
        <th>1</th>
        <th>2</th>
        <th>3</th>
        <th>4</th>
        <th>5</th>
        <th>6</th>
        <th>7</th>
        <th>8</th>
        <th>9</th>
        <th>10</th>
      </tr>
      <tr>
        <td><em>p(x|H<sub>0</sub>)</em></td>
        <td>0.0010</td>
        <td>0.0098</td>
        <td>0.0439</td>
        <td>0.1172</td>
        <td>0.2051</td>
        <td>0.2461</td>
        <td>0.2051</td>
        <td>0.1172</td>
        <td>0.0439</td>
        <td>0.0098</td>
        <td>0.0010</td>
      </tr>
      <tr>
         <td><em>Z</em></td>
         <td>-3.1623</td>
         <td>-2.5298</td>
         <td>-1.8974</td>
         <td>-1.2649</td>
         <td>-0.6325</td>
         <td>0</td>
         <td>0.6325</td>
         <td>1.2649</td>
         <td>1.8974</td>
         <td>2.5298</td>
         <td>3.1623</td>
      </tr>
      <tr>
        <td><em>p</em></td>
        <td>0.0008</td>
        <td>0.0057</td>
        <td>0.0294</td>
        <td>0.1083</td>
        <td>0.2644</td>
        <td>0.5</td>
        <td>0.2644</td>
        <td>0.1083</td>
        <td>0.0294</td>
        <td>0.0057</td>
        <td>0.0008</td>
    </table>

  * Expected Value of 10 coin flips with 0.5 probability is *E(X) = np* = 10 * 0.5 = 5
  * Reject null hypothesis if heads is extremely fewer or greater than 5. *What counts as 'extremely?'*
* Types of Hypotheses
  * **Simple** - the distribution can be specified
  * **Composite** - the distribution cannot be fully specified

### Innocent until proven guilty

* In hypothesis testing, we assume the null hypothesis is true
  * *H<sub>0</sub>* - defendant is innocent
  * *H<sub>A</sub>* - defendant is guilty
  * If evidence proves otherwise, then we will ***reject*** the null hypothesis
  * If there isn't evidence to prove otherwise, then we will ***fail to reject*** the null hypothesis
  * Analogy to US courts: you are presumed to be innocent. It is up to the evidence to prove guilt. You don't have to prove innocence (aka null hypothesis)
* **Statistically significant** - where do we draw the line to make a decision?
* **Confidence Level (*c*)** - how confident are we in our decision?
* **Significance Level (*&alpha; = 1 - c*)** complement to confidence level

### Designing a hypothesis test
  * Pick the null hypothesis *H<sub>0</sub>*
  * Decide if *H<sub>A</sub>* is one- or two-sided
    * one-sided: probability that coin favors heads
    * two-sided: probability that coin is not fair
  * Pick a test statistic, e.g., sample mean, sample total
  * pick a significance level *&alpha;*
  * Determine the power


## Tests of population mean

* The test statistic *z* in terms of the sample mean is
  > ![z](https://user-images.githubusercontent.com/638189/48364012-43ed7e00-e675-11e8-89e0-679c221853f8.png)<!--
    z = \frac{ \overline{x} -  \mu_{0}}{  \sigma/\sqrt{n} } -->
* The test statistic *z* in terms of sample proportion is
  > ![proportion](https://user-images.githubusercontent.com/638189/48368969-258e7f00-e683-11e8-8fde-7939a1cf4d43.png)
  * where *p<sub>0</sub>* is the true population proportion and *p* is the hypothesized proportion
* one-tail test

  <table>
    <tr>
      <td><em>P(Z > z)</em></td>
      <td>Z-score</td>
    </tr>
    <tr>
      <td>0.1587</td>
      <td>1.0000</td>
    </tr>
    <tr>
      <td>0.1000</td>
      <td>1.2816</td>
    </tr>
    <tr>
      <td>0.0500</td>
      <td>1.6449</td>
    </tr>
    <tr>
      <td>0.0228</td>
      <td>2.0000</td>
    </tr>
    <tr>
      <td>0.0200</td>
      <td>2.0537</td>
    </tr>
    <tr>
      <td>0.0100</td>
      <td>2.3263</td>
    </tr>
    <tr>
      <td>0.0050</td>
      <td>2.5758</td>
    </tr>
  </table>

* **Lower Tail Test**
  * The hypothesized mean *&mu;<sub>o</sub>* is less than the true population mean *&mu;*.
  * Reject the null hypothesis if *z &le; -z<sub>&alpha;</sub>*, where *z<sub>&alpha;</sub>* is the *100(1 - &alpha;) percentile of the standard normal distribution.
  * Example: A light bulb manufacturer claims its products last more than 10,000 hours. From a sample of 30 bulbs, the average lifetime was 9,900 hours. Assume the standard deviation is 120 hours. Can we reject the manufacturer's claim with a 0.05 (5%) significance level?
    > ![light bulb example](https://user-images.githubusercontent.com/638189/48365044-bfe8c580-e677-11e8-8e38-15c2ddd90af2.png)
    * The null hypothesis is *&mu; > 10000* since the the claim is at least 10000
    * We know *z*<sub>0.05</sub> = 1.645
    * Reject the null hypothesis because -4.564 is less than the critical value of -1.649
* **Upper Tail Test**
  * The hypothesized mean *&mu;<sub>o</sub>* is greater than the true population mean *&mu;*.
  * Reject the null hypothesis if *z &ge; z<sub>&alpha;</sub>*.
  * Example: The food label for a bag of cookies says there is at most 2g saturated fat in a single cookie. From a sample of 35 cookies, the average amount of saturated fat is 2.1 grams. Assume the standard deviation of the population is 0.25 grams. Can we reject the null hypothesis with a 0.05 (5%) significance level?
    > ![cookie example](https://user-images.githubusercontent.com/638189/48365826-04756080-e67a-11e8-95a8-36093a2889ed.png)
    * The test statistic of 2.366 means we reject the claim
  * Example: IQ is a N(100, 15<sup>2</sup>) distribution
    * From a sample of 9 students, the average IQ is 112. Can we reject *H<sub>0</sub>* at a *&alpha;* = 0.05 significance level?
    > ![iq example](./img/dbd1e14b-6631-478f-b30d-0aa9482b25d7.png)
    * *p = P(Z &ge; 2.4)* = 0.0082
    * Since *p &le; &alpha;* we reject null hypothesis.
  * Example: a population has a mean *&mu;* variance *&theta;<sup>2</sup>* = 4.
    * let the sample data be [-1, 1, 2, 3, 6]
    * Let *H<sub>0</sub> = 0*
    * Let *H<sub>A</sub> > 0*
    * At *&alpha; = 0.05*, can we reject *H<sub>0</sub>*?
    * *x&#x0304;* = 2.2. Use *z* test because the data is a normal distribution
    > ![upper data example](./img/44f3fb3e-1fed-4251-93d2-6f937cd1397c.png)
    * *p = P(Z > z) = P(Z > 2.460) = 0.0070 and *z<sub>0.05</sub>* = 1.645. Reject null hypothesis
* **Two-Tailed Test**
  * The null hypothesis is saying the hypothesized mean is equal to the true mean
  * Reject the null hypothesis if *z &le; -z<sub>&alpha;/2</sub>* or *z &ge; z<sub>&alpha;/2</sub>*, where *z<sub>&alpha;/2</sub>* is the *100(1 - &alpha;/2) percentile of the standard normal distribution.
    * In other words, we have to split the significance level to either side of the distribution curve
  * Example: suppose the average weight of a penguin is 15.4kg. In an sample of 35 penguins, the average penguin weight is 14.6kg, and the population standard deviation is 2.5kg. Can we reject the null hypothesis with a 0.05 significance level?
    > ![penguin example](https://user-images.githubusercontent.com/638189/48366430-e3157400-e67b-11e8-98f7-11a2235499c5.png)
    * Since the critical value for *z<sub>0.05/2</sub* = *z<sub>0.025</sub* = 1.96, the null hypothesis is accepted. We cannot say the weight of the penguins is different
* **Lower Tail Proportion Test**
  * expressed as *p &ge; p<sub>0</sub>* where *p* is the true population proportion and *p<sub>0</sub>* is hypothesized lower bound.
  * Example: suppose 60% of citizens voted in the last election. From a telephone survey of 148 people, 85 people said they voted (aka 57%). At a 0.5 significance level, can we reject the null hypothesis that proportion of voters is above 60%?
    > ![voter example](https://user-images.githubusercontent.com/638189/48369211-e57bcc00-e683-11e8-95de-6e4c2dd63da9.png)
    * since *-z<sub>0.5</sub>* = 1.649, and the test statistic -0.6376 is not less than that, we cannot reject the null hypothesis.
* **Upper Tail Proportion Test**
  * expressed as *p &le; p<sub>0</sub>* where *p* is the true population proportion and *p<sub>0</sub>* is hypothesized lower bound.
  * Example: suppose 12% of apples harvested last year were rotten. From this year's sample of 214 apples, 30 are rotten (14%). With a 5% significance level (*&alpha; = 0.05*), can reject the null hypothesis that the proportion of rotten apples is below 12%?
    > ![apple example](https://user-images.githubusercontent.com/638189/48370363-1e697000-e687-11e8-8a41-0f5a2b54458f.png)
    * Since the test statistic is not greater than *-z<sub>0.5</sub>* = 1.649, we cannot reject the null hypothesis.
* **Two-Tailed Proportion Test**
  * expressed as *p = p<sub>0</sub>* where *p* is the true population proportion and *p<sub>0</sub>* is hypothesized lower bound.
  * Suppose a coin flip gives 12 heads from 20 flips (60%). At a 0.5 significance level, can we reject the null hypothesis that that the coin toss is fair (50%)?
    > ![coin flip example](https://user-images.githubusercontent.com/638189/48370729-22e25880-e688-11e8-86cb-870122e840f2.png)
    * Since the test statistic falls within then critical values of *-z<sub>0.025</sub* = -1.96 and *z<sub>0.025</sub* = 1.96, we cannot reject the null hypothesis.

## Two Population proportions

* **Standard Deviation *&sigma;*** - a measure of the variability of a random variable
* **Standard Error** - how precise the estimate is
  * It can be thought of as how precise the mean of the sample is, vs. the true mean of the population
  * increasing the sample size provides a more specific measure of the true *&sigma;*
* Sample Mean
  > ![sample mean](./img/39585ffb-e1b3-4311-bb43-ab1622edd995.png)
* Variance of Sample Mean
  > ![sample Variance](./img/281093f1-719b-4b9c-a385-694be8b12a0a.png)
* Standard error is square root of variance of sample mean
  > ![Standard error](./img/3a6a65ad-eda6-4562-be0f-6c43945434a0.png)
  * Note that as the size of the sample *n* increases, the standard error decreases!
* Recall the standard deviation of a binomial distribution
  > ![Bernoulli Standard Deviation](./img/d35efa90-8c71-44a5-a4eb-85bb8e291928.png)
* Therefore the standard error of sample from a binomial distribution is
  > ![binomial standard error](./img/78d1bde7-8549-4bc6-b24e-f0bec2431972.png)
* **Spread** the standard error in the distribution of differences between sample proportions.
  > ![standard error difference](./img/8d081ecf-a26a-4211-aa6f-d8b4f2f1d9c0.png)
* Difference of means: *p<sub>1</sub> - p<sub>2</sub>*
* We do not have have the true proportions, so we we have to infer *p<sub>1</sub>* and *p<sub>2</sub>* from the samples, *p&#x0302;<sub>1</sub>* and *p&#x0302;<sub>2</sub>*
  * let *x<sub>1</sub>* and *x<sub>2</sub>* be the successes in each of the sample populations. then the **pooled proportion** is:
  > ![pooled proportion](./img/d58d8c6d-ed51-4dc6-9d67-ae51bd121621.png)
* Use the pooled proportion to estimate the standard error
  > ![pooled standard error](./img/bc06a723-2acc-4e10-bd28-118a22b1f39a.png)
* Then the Z-test statistic is
  > ![z-test 2 populations](./img/da021219-12e9-4ffe-b7e0-33eb2a9b3674.png)
* Since the null hypothesis *H<sub>0</sub>* says the two proportions should be the same, aka *p&#x0302;<sub>1</sub>* - *p&#x0302;<sub>2</sub>* = 0, we can simplify to
  > ![z-test 2 population simplified](./img/9177006b-fdb6-4326-8867-d388ea94c5c5.png)

### Example

* the BigBoxRetail company has been accused of not properly giving their employees health insurance.
  * The claim is only 46% of employees at BigBoxRetail have health insurance, vs. the standard Retail Company average of 66% coverage.
  * From a sample of 50 employees at BigBoxRetail, 23 are covered.
  * From a sample of 70 employees at other Retail companies, 23 are covered.
  * Do employees at BigBoxRetail have less coverage, with 5% level of significance (*&alpha;* = 0.05)?
  * Calculate Test statistic
    > ![retail test statistic](./img/fb095eb9-0924-4a21-9ce7-9b7c6a690b13.png)
  * Calculate pooled proportion
  > ![retail pooled proportion](./img/c0024136-ca16-4153-83f8-382fe2d3ba3d.png)
  * Calculate standard error
  > ![retail standard error](./img/de9e5c80-f3b7-40df-a2df-d15ee4630e0f.png)
  * Calculate Z-score
  > ![retail z score](./img/6708cbaf-a76c-4901-b376-2e04596304b8.png)
  * *p*-value: *P(Z < -1.6749)* &approx; 0.0470 or 4.7%
  * Analysis: If the *H<sub>0</sub> is true, then there is a 4.7% chance that that the difference of means is less than 0.1543. This is unlikely with *&alpha;* = 0.05

## Sources:

* [Hypothesis Testing, R Tutorial](http://www.r-tutor.com/elementary-statistics/hypothesis-testing)
* [HTML Math Symbols, Math Entities, and ASCII Math Character Code Reference](https://www.toptal.com/designers/htmlarrows/math/)
* [Online equation editor](http://www.sciweavers.org/free-online-latex-equation-editor)
  * proportion: `z = \frac{ \overline{p} - p_{0}}{   \sqrt{p_{0}(1 - p_{0})/n}  }`
  * Sampling Standard Deviation: `\sigma_{ \overline{x} } =  \frac{ \sigma }{ \sqrt{n} }`
  * Light bulb example: `\frac{9900 - 10000}{120 /  \sqrt{30} } = -4.456`
  * cookie example: `\frac{2.1 - 2}{0.25 /  \sqrt{35} } = 2.366`
  * IQ example: `z = \frac{112 - 100}{15\sqrt{9}} = 2.4 \approx N(0,1)`
  * Upper data example: `z = \frac{\overline{x} - \mu_{0}}{\sigma/\sqrt{n}} = \frac{2.2 - 0}{2/\sqrt{5}} = 2.2497`
  * Penguin example: `\frac{15.4 - 14.6}{2.5 /  \sqrt{35} } = 1.893`
  * voter example: `\frac{ \frac{85}{148} - 0.6}{   \sqrt{0.6(1 - 0.6)/148}  } =  \frac{  0.57\overline{432} - 0.6}{   \sqrt{0.6 * 0.4/148}  } = -0.638`
  * apple example: `\frac{ \frac{30}{214} - 0.12}{   \sqrt{0.12(1 - 0.12)/214}  } =  \frac{  0.1402 - 0.12}{   \sqrt{0.12 * 0.88/214}  } = 0.909`
  * coin flip example: `\frac{ \frac{12}{20} - 0.5}{   \sqrt{0.5(1 - 0.5)/20}  } =  \frac{  0.6 - 0.5}{   \sqrt{0.25/20}  } = 0.894`
  * sample mean - `\overline{X} = \frac{1}{n}\sum_{i=1}^{n}X_{i}`
  * sample Variance - `Var(\overline{X}) = Var\left ( \frac{1}{n}\sum_{i=1}^{n}X_{i} \right )  = \frac{\sigma^{2}}{n}`
  * standard error: `\sigma^{\overline{X}} = \frac{\sigma}{ \sqrt{n} }`
  * Bernoulli Standard Deviation: `\sigma =  \sqrt{p(1-p)}`
  * binomial standard error: ` \sigma^{\overline{X}} =\sqrt{\frac{p(1-p)}{n}}`
  * standard error difference: `\sqrt{\frac{p_1(1-p_1)}{n_1}+\frac{p_2(1-p_2)}{n_2}}`
  * pooled proportion: `\widehat{p} = \frac{x_1+x_2}{n_1+n_2} `
  * pooled standard error: `\sqrt{\frac{\widehat{p}(1-\widehat{p})}{n_1}+\frac{\widehat{p}(1-\widehat{p})}{n_2}}`
  * z-test 2 populations: `Z= \frac{X - \mu}{\sigma} = \frac{(\widehat{p}_1-\widehat{p}_2) - (p_1-p_2)}{\sqrt{\frac{\widehat{p}(1-\widehat{p})}{n_1}+\frac{\widehat{p}(1-\widehat{p})}{n_2}}}  `
  * z-test 2 population simplified: `Z= \frac{\widehat{p}_1-\widehat{p}_2}{\sqrt{\widehat{p}(1-\widehat{p}) \left ( \frac{1}{n_1} + \frac{1}{n_2} \right )  }}`
  * retail example:
    * pooled proportion: `\widehat{p} = \frac{x_1+x_2}{n_1+n_2} = \frac{23+43}{50+70} = 0.55`
    * test statistic: `X = \widehat{p}_1-\widehat{p}_2 = \frac{23}{50}-\frac{43}{70} \approx -0.1543`
    * stadard error: `\sigma = \sqrt{0.55*0.45 \left ( \frac{1}{50} + \frac{1}{70} \right ) } \approx 0.0921`
    * z-score: `Z = \frac{-0.1543}{0.0921} \approx -1.6749`
* [Intro to Hypothesis testing in Statistics](https://www.youtube.com/watch?v=VK-rnA3-41c)
* [Hypothesis testing and p-values](https://www.youtube.com/watch?v=-FtlH4svqx4)
* [Introductin to Hypothesis testing](https://www.youtube.com/watch?v=qsMZ4Zi5Csk)
* [Null Hypothesis Significance Testing I](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/MIT18_05S14_Reading17b.pdf)
* [What is the difference between the standard error of the mean and standard deviation?](https://www.investopedia.com/ask/answers/042415/what-difference-between-standard-error-means-and-standard-deviation.asp)
* [Standard deviation versus standard error](http://thestatsgeek.com/2013/06/30/standard-deviation-versus-standard-error/)
* [Hypothesis Test for Difference in Two Population Proportions](https://courses.lumenlearning.com/wmopen-concepts-statistics/chapter/hypothesis-test-for-difference-in-two-population-proportions-3-of-6/)
