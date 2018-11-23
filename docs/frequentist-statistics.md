# Frequentist Statistics

* Everyone uses Bayes' Theorem when the the prior *P(H)* is known
* If there is no prior, then we draw inferences from the likelihood function.
* **Frequentist** - the idea that probabilities present long-term frequencies of repeatable random experiments.
  * Don't use probabilities to quantify degree of belief in hypotheses, so no pdf
* Difference
  * Bayesian statistics will put probability distributions on hypotheses and data. Probability is belief
  * Frequentist statistics will put probability on the experimental data. Probability comes from experiments
* **Point Statistic** - a single value computed from data, such as mean or maximum
* **Interval Statistic** - interval computed from data, such as range
* **Set Statistic** - a set computed from data. Suppose we have bunch of dice, and each dice has different n sides. Data can be the value of the roll of 1 die picked at random. The Set is determined from the value. If it is 20, obviously the 6-sided die is not part of the set.
* **Sampling Distribution** - the probability distribution of the statistic
* **Point Estimate** - using statistics to get paramater *&theta;*

### Errors

* **Type I Error** - reject the null hypothesis but we should not
* **Type II Error** - don't reject the null hypothesis but we should

<table>
  <tr>
    <td colspan='2' rowspan='2'></td>
    <td colspan='2' align='center'>True State of nature</td>
  </tr>
  <tr>
    <td>H<sub>0</sub></td>
    <td>H<sub>A</sub></td>
  </tr>
  <tr>
    <td rowspan='2'>Decision</td>
    <td>Reject H<sub>0</sub></td>
    <td>Type I error</td>
    <td>Correct Decision</td>
  </tr>
  <tr>
    <td>&ldquo;Don&rsquo;t reject &rdquo; H<sub>0</sub></td>
    <td>Correct Decision</td>
    <td>Type II error</td>
  </tr>
</table>

### Significance and Power

<table>
  <tr>
    <td><em>P(reject H<sub>0</sub>|H<sub>0</sub>)<em></td>
    <td><em>P(reject H<sub>0</sub>|H<sub>A</sub>)<em></td>
  </tr>
  <tr>
    <td><em>P(do not reject H<sub>0</sub>|H<sub>0</sub>)<em></td>
    <td><em>P(do not reject H<sub>0</sub>|H<sub>A</sub>)<em></td>
  </tr>
</table>

* **Significance** - *P(reject H<sub>0</sub>|H<sub>0</sub>)* the probability we incorrectly reject H<sub>0</sub>
  * *P(Type I error)*
  * In other words, the probability the test statistic falls within rejection region even though H<sub>0</sub> is true
  * A significance level of 0.05 doe snot mean the test makes mistakes 5% of the time. It means if *H<sub>0</sub>* is true, then there is a 5% probability that the test will reject it.
* **Power** - *P(reject H<sub>0</sub>|H<sub>A</sub>)* the probability that correctly reject H<sub>0</sub>
 * 1 - *P(Type II error)*
 * Power if *H<sub>A</sub>* is true, what is the probability of rejecting the null hypothesis?
* Ideally: a hypothesis test should have a small significance level and a high power level
* Example: a new drug vs. placebo
  * *H<sub>0</sub>* drug is not better than placebo
  * *H<sub>A</sub>* drug is better than placebo
  * Power - probability that test will say drug is better, if it is truly better
  * Significance - probability tha tthe test wil say drug is better, but it isn't

### Critical Values

* Z
* Probability value is on the other side of *H<sub>0</sub>*

### *p*-Values

* Assuming the null hypothesis, what is the probability of seeing data at least as extreme as the experimental data.

## Sources
  * [Are you a Bayesian or a Frequentist?](https://www.behind-the-enemy-lines.com/2008/01/are-you-bayesian-or-frequentist-or.html)
