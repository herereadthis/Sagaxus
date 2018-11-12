# A/B Testing, Part 1



* Evaluate ideas quickly using controlled (randomized) experiments, single-factor or factorial designs
* A/B tests are also known as:
  * Split tests,
  * Control/Treatment tests
  * MultiVariable Tests (MVT)
  * Parallel Flights
* Establish a causal relationship between changes and their influence on user-observable behavior.
* Controlled experiments generate large amounts of data, which must be analyzed
* Controlled experiments have great return-on-investment (ROI) and building the appropriate infrastructure can accelerate innovation.

## Introduction

In the 1700s a British ship's captain noticed sailors on Mediterranean naval ships had fewer occurances of scurvy. They had citrus fruit in thei rations. The captain gave half his crew citrus (Treatment group) and did not change the diet of the other half (Control group).

The personalized recommendation on Amazon's shopping cart is also a result of A/B testing. Its creator, Greg Linden, tried to promote it but a senior vice president ordered to halt work on it because it would distract people from checking out. However, the controlled experiment "feature on by such a wide margin that not having it live was costing Amazon a noticeable chunk of change."

Other examples:

* adding a spot for "Coupon Codes" in checkout loses revenue: people wonder if they are paying too much because there are discount codes that exist but they do not have
* Customer feedback asking whether something is helpful, with a star-rating turn out to be useless for getting responses becuase most ratings are either 1 or 5. So just simplify it to "helpful" or "not helpful"
* Behavior-Based Searching - sometimes search algorithms are terrible, so instead of showing search results, show what people typically bought after makig a search, aka "People who search for X bought item Y" BBS increased Amazon's revenue by 3%.
* In the simplest kind of experiment, live users are randomly assigned one of two varients:
  * **Control** - existing version
  * **Treatment** - new version being evaluated
* Metrics of interest: runtime performance, implicit/explicit user behaviors, survey data
* Evaluate whether there is a statistically significant difference between two variants on metrics of interest
* Retain or reject the (null) hypothesis that no difference exists between the two versions
* Evaluating segments of users to understand subpopulations
* **Overall Evaluation  Criterion (OEC)** the most important thing being measured

## Controlled Experiements

* The simplest controlled experiment is an A/B Test - users are exposed to one of two variants. If designed and executed properly, the only thing that is consistently different between the Control and the Treatment is the change, and if there are any differences in the OEC, then we can establish causality
  * **Overall Evaluation Criterion (OEC)** - a quantitative measure of the experiment's objective, aka *Outcome*, *Evaluation Metric*, *Performance metric*, *Fitness Function*
  * **Factor** - (Variable) a controllable experimental variable that might influence the OEC. Factors are assigned *values*, aks *levels* or *versions*
  * **Variant** - a particular user experience, either the control or one of the treatments
  * **Experimental Unit** - (Item) the entity that metrics are calculated on, it's typically the "user."
  * **Null Hypothesis** - H<sub>0</sub> the idea that the OECs for the varients are not noticeable or significant
  * **Confidence Level** - the probability of failing to reject the null hypothesis when it is true
  * **Power** - probably of correctly rejecting the null hypothesis when it is false
  * **A/A Test** - (null test) expose two sets of users to the same experience. Then the null hypothesis should be rejected 5% of the time if you have a 95% confidence level.
  * **Standard Deviation** - measure of variability **&sigma;**
  * **Standard Error** - standard deviation of the sampling distribution
    ```
    σˆ = estimated standard deviatiom
    n = number of independent observation
    σˆ / √n
    ```
* Factors that impact the test:
  * **Confidence Level** - often set to 95%, which implies we will reject the null hypothesis 5% of the time (claim there is a difference when there is none). Increasing confidence level reduces power
  * **Power** - often set to 80-95%. If there is a difference, power is probability that we identify the difference.
    * *Type II Error* - don't reject the null hypothesis even though it is false - (claim there is no difference even though there is)
  * **Standard Error** - the smaller the std-err, the more powerful the test
    * Increasing the sampling size reduces teh the Std-Err
    * Use OEC components that have smaller standard deviation &sigma;
      * Conversion probability (0-100%) has lower standard deviation than number of purchase units, which has lower standard deviation than revenue
    * Don't count users who weren't exposed to the variants (those users who never got to the tested page) - they are just noise
    * *Effect* - the difference in OEC (mean of Treatment minus mean of Control) Type III errors happen more often when the effects are small
* Standard deviation
  * subtract the mean from every value, then square each result, then get the mean of those results.
    > ![Standard Deviation](https://user-images.githubusercontent.com/638189/48319308-62526b80-e5da-11e8-8253-aeb9665de9bf.png)
* *T-Test*, used in A/B testing (single factor hypothesis tests)
  > ![T-test](https://user-images.githubusercontent.com/638189/48319320-82822a80-e5da-11e8-9ec6-1e22be7ce55c.png)
* Calculation for minimum sample size, with 95% confidence level, 80% power
  > ![Minimum Sample Size](https://user-images.githubusercontent.com/638189/48319372-32f02e80-e5db-11e8-9269-3b3c76be8bc2.png)
* Demo: e-commerce site:
  * 5% of users who visit will buy something, (which means 95% spend $0)
  * Those who buy something spend about $75
  * The average user spends $3.75
  * Assume the standard deviation of purchase amount is $30
  * To run an A/B test and want to detect a 5% change in revenue, you need 409,600 users to achieve 80% power
    > ![5% revenue change, sample size equation](https://user-images.githubusercontent.com/638189/48319384-51562a00-e5db-11e8-9f62-6626a1c7c4e6.png)
  * What about running an A/B Test to look for a 5% change in conversion rate?
    * Conversion rate can be thought of as Bernoulli trials (either buy or don't buy)
    * Using the formula for standard deviation for a binomial distribution (see below), the result is 122,000 users. *Measuring conversion requires far fewer trials than revenue.*

## Sources

* [Controlled experiments on the web: survey and practical guide](https://www.exp-platform.com/Documents/controlledExperimentDMKD.pdf)
* [Online equation editor](http://www.sciweavers.org/free-online-latex-equation-editor)
  * Standard Deviation: `\sigma = \sqrt{ \frac{1}{N}  \sum_{i=1}^{N} (x_{i} -  \mu )^{2} }`
  * T-test: `t = \frac{ \overline{ O_{b} } -  \overline{ O_{a} } }{ \widehat{  \sigma_{d} } }`
  * Min Sample Size: `n = \frac{ 16\sigma^2  }{ \Delta^{2} }`
  * Min Sample Size, example: `\frac{ 16 * 30^2  }{ (3.75 * 0.05)^{2}  } = 409600`

