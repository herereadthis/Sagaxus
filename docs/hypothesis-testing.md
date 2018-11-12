# Hypothesis Testing

* **Hypothesis** - a premise or claim that we want to test.
* **Null Hypothesis (*H<sub>0</sub>*)** - Currently accepted value for a parameter.
* **Alternate Hypothesis (*H<sub>1</sub>*)** - Claim to be tested, aka "research hypothesis"
* The null and alternative hypothesis are mathematical opposites. Together, they must allow for all possible answers
* A candy machine makes chocolate bars that weight 5g on average. A work claims the machine no longer makes 5g bars.
  * *H<sub>0</sub>*: *&mu; = 5g*
  * *H<sub>1</sub>*: *&mu; &ne; 5g*
* In hypothesis testing, we assume the null hypothesis is true
  * If evidence proves otherwise, then we will ***reject*** the null hypothesis
  * If there isn't evidence to prove otherwise, then we will ***fail to reject*** the null hypothesis
  * Analogy to US courts: you are presumed to be innocent. It is up to the evidence to prove guilt. You don't have to prove innocence (aka null hypothesis)
* The **test statistic** is calculated from the sample data, and is used to decided.
* **Statistically significant** - where do we draw the line to make a decision?
* **Confidence Level (*c*)** - how confident are we in our decision?
* **Significance Level (*&alpha; = 1 - c*)** complement to confidence level


## Tests of population mean

* The test statistic *z* in terms of the sample mean is
  > ![z](https://user-images.githubusercontent.com/638189/48364012-43ed7e00-e675-11e8-89e0-679c221853f8.png)
* The test statistic *t* in term of the sample mean is
  > ![t](https://user-images.githubusercontent.com/638189/48366729-b6159100-e67c-11e8-92bc-1c74a3c2ec1d.png)
  where *&sigma;<sub>x</sub>* is the standard deviation of the sample
* The test statistic *z* in terms of sample proportion is
  > ![proportion](https://user-images.githubusercontent.com/638189/48368969-258e7f00-e683-11e8-8fde-7939a1cf4d43.png)
  where *p<sub>0</sub>* is the true population proportion and *p* is the hypothesized proportion

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
  * Example: suppose 12% of apples harvested last year were rotten. From this year's sample of 214 apples, 30 are rotten (14%). With a 95% confidence level, can reject the null hypothesis that the proportion of rotten apples is below 12%?
    > ![apple example](https://user-images.githubusercontent.com/638189/48370363-1e697000-e687-11e8-8a41-0f5a2b54458f.png)
    * Since the test statistic is not greater than *-z<sub>0.5</sub>* = 1.649, we cannot reject the null hypothesis.
* **Two-Tailed Proportion Test**
  * expressed as *p = p<sub>0</sub>* where *p* is the true population proportion and *p<sub>0</sub>* is hypothesized lower bound.
  * Suppose a coin flip gives 12 heads from 20 flips (60%). At a 0.5 significance level, can we reject the null hypothesis that that the coin toss is fair (50%)?
    > ![coin flip example](https://user-images.githubusercontent.com/638189/48370729-22e25880-e688-11e8-86cb-870122e840f2.png)
    * Since the test statistic falls within then critical values of *-z<sub>0.025</sub* = -1.96 and *z<sub>0.025</sub* = 1.96, we cannot reject the null hypothesis.

## Sources:

* [Hypothesis Testing, R Tutorial](http://www.r-tutor.com/elementary-statistics/hypothesis-testing)
* [HTML Math Symbols, Math Entities, and ASCII Math Character Code Reference](https://www.toptal.com/designers/htmlarrows/math/)
* [Online equation editor](http://www.sciweavers.org/free-online-latex-equation-editor)
  * z: `z = \frac{ \overline{x} -  \mu_{0}}{  \sigma/\sqrt{n} }`
  * t: `t = \frac{ \overline{x} -  \mu_{0}}{  \sigma_{x}/\sqrt{n} }`
  * proportion: `z = \frac{ \overline{p} - p_{0}}{   \sqrt{p_{0}(1 - p_{0})/n}  }`
  * Sampling Standard Deviation: `\sigma_{ \overline{x} } =  \frac{ \sigma }{ \sqrt{n} }`
  * Light bulb example: `\frac{9900 - 10000}{120 /  \sqrt{30} } = -4.456`
  * cookie example: `\frac{2.1 - 2}{0.25 /  \sqrt{35} } = 2.366`
  * Penguin example: `\frac{15.4 - 14.6}{2.5 /  \sqrt{35} } = 1.893`
  * voter example: `\frac{ \frac{85}{148} - 0.6}{   \sqrt{0.6(1 - 0.6)/148}  } =  \frac{  0.57\overline{432} - 0.6}{   \sqrt{0.6 * 0.4/148}  } = -0.638`
  * apple example: `\frac{ \frac{30}{214} - 0.12}{   \sqrt{0.12(1 - 0.12)/214}  } =  \frac{  0.1402 - 0.12}{   \sqrt{0.12 * 0.88/214}  } = 0.909`
  * coin flip example: `\frac{ \frac{12}{20} - 0.5}{   \sqrt{0.5(1 - 0.5)/20}  } =  \frac{  0.6 - 0.5}{   \sqrt{0.25/20}  } = 0.894`
* [Intro to Hypothesis testing in Statistics](https://www.youtube.com/watch?v=VK-rnA3-41c)
* [Hypothesis testing and p-values](https://www.youtube.com/watch?v=-FtlH4svqx4)
* [Introductin to Hypothesis testing](https://www.youtube.com/watch?v=qsMZ4Zi5Csk)
