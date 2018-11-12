# Sampling Size

How many samples from a population do you need to see whether they possess a particular property, within a margin of error?

* **Critical Value** - the area under a normal distribution curve.
  * There is an 80% probability a result will fall within 1.28 standard deviations of the mean. So 1.28 is the critical value of *z* that corresponds to central area of 0.80.
  * *&alpha;* is the tail area. For a 0.80 central area, then there are 0.10 tail areas on either side of the curve.
  * *z*<sub>0.10</sub> 1.28 is the critical value of *z* for a 0.80 probability.
  * *z*<sub>0.05</sub> 1.645 is the critical value of *z* for a 0.90 probability.
  * 95%: *z*<sub>0.025</sub> = 1.96
  * 95.4%: *z*<sub>0.023</sub> = 2.00
  * 96%: *z*<sub>0.02</sub> = 2.054
  * 98%: *z*<sub>0.01</sub> = 2.326
  * 99%: *z*<sub>0.005</sub> = 2.576
  * 99.5%: *z*<sub>0.0025</sub> = 2.807
  * 99.73%: *z*<sub>0.0013</sub> = 3.000
  * 99.8%: *z*<sub>0.001</sub> = 3.091
  * 99.9%: *z*<sub>0.0005</sub> = 3.291

* Margin of Error formula
  * where Z<sub>&alpha;/2</sub> is the critical value,
  * *p* is the proportion,
  * *n* is sample size
    > ![Margin of Error](https://user-images.githubusercontent.com/638189/48325466-b1f95d00-e603-11e8-92cd-7502e202f77a.png)
  * Usually we don't know what the proportion is, but to maximize the margin of error, the proportion will be 50% to maximize the the formula
* Sample size:
  > ![Sample Size](https://user-images.githubusercontent.com/638189/48326258-5a102580-e606-11e8-95b1-a6df859de965.png)
* Examples
  * What is the proportion of customers who buy an item after viewing a website on a certain day, with a 95% confidence level and 5% margin of error, if the website sees about 10,000 customers a day? If they are uncertain of their current conversion rate, then 384 customers.
    > ![Example 1](https://user-images.githubusercontent.com/638189/48326340-d145b980-e606-11e8-909a-2fa1658c1ef7.png)
  * If they know the conversion rate is 5%, then the sample size is 73.
    > ![Example 2](https://user-images.githubusercontent.com/638189/48326377-0f42dd80-e607-11e8-8c58-124a5ca2a3cb.png)



## Sources

* [Critical Values of *z*](http://www.math.armstrong.edu/statsonline/5/5.3.2.html)
* [Online equation editor](http://www.sciweavers.org/free-online-latex-equation-editor)
  * Margin of Error: `Z_{ \alpha / 2}  \sqrt{\frac{p(1 - p)}{n}}  \leq ME`
  * Sample Size: `n = \frac{p(1-p)}{(\frac{ME}{Z_{ \alpha / 2}})^2}`
  * Example 1: `\frac{0.5 * 0.5}{(\frac{0.05}{1.96})^2}  \approx  384`
  * Example 2: `\frac{0.95 * 0.05}{(\frac{0.05}{1.96})^2}  \approx  73
`
