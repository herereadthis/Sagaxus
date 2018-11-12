### Bernoulli Trials, Binomial Distributions

An experiment that only has two possible results, *success* and *failure*, can be called a Bernoulli Trial if:
* The results are mutually exclusive,
* The probability of these two results do not change each time the experiment is done
* Tehen the probability of success is *p*, then the probability of failure is *(1 - p)*, which is often called *q*
* The Bernoulli random variable is defined as
    > ![Bernoulli Random Variable](https://user-images.githubusercontent.com/638189/48320500-e0b60a00-e5e8-11e8-8fc1-f1b316c3fe83.png)
* `X` follows a Bernoulli distribution with parameter `p` is `X ~ Ber(p)`
* Probability function:
    > ![Failure Probability Function](https://user-images.githubusercontent.com/638189/48320567-85d0e280-e5e9-11e8-8ad2-cac44548e809.png)
    > ![Success Probability Function](https://user-images.githubusercontent.com/638189/48320591-adc04600-e5e9-11e8-9b75-8e1a3732a2a0.png)
* Distribution Function:
    > ![Distribution Function](https://user-images.githubusercontent.com/638189/48320683-769e6480-e5ea-11e8-8a15-d22a9ae925a9.png)
* Bernoulli trials follow a **Binomial Distribution** If *n* trials with a *p* probability, then `X ~ B(n,p)`
    > ![Binomial Distribution](https://user-images.githubusercontent.com/638189/48320873-10b2dc80-e5ec-11e8-9e1f-86632948918b.png)
* [Standard Deviation](https://math.stackexchange.com/questions/1716156/sd-of-a-bernoulli-trial) of a Bernoulli Trial
    > ![Bernoulli Standard Deviation](https://user-images.githubusercontent.com/638189/48321218-e282cc00-e5ee-11e8-8976-1e58630e981e.png)

## Examples:
* The outcome of a coin flip is a Bernoulli random variable, and assume each outcome is equally possible. The probability that a coin flip lands heads is *0.5*, while tails is *1 - 0.5*
  * Outcome of 5 heads in 5 flips is *0.5<sup>5</sup>* - each coin toss is independent of the others
  * Outcome of exactly 3 heads in 5 flips?
      > ![coin flip example](https://user-images.githubusercontent.com/638189/48321096-e95d0f00-e5ed-11e8-960f-5df95aa2cddf.png)
* An airline has sold 50 tickets for a flight. The probability of a passenger not showing up is 0.05. *X = number of passengers that don't show up)*
  * In other words = *X ~ B(50, 0.95)*
  * What is the probability that all 80 passengers show up?
      > ![plane ticket example 1](https://user-images.githubusercontent.com/638189/48321686-db10f200-e5f1-11e8-95ef-f36bb5c375d9.png)
  * What is the probability that at lease one passenger does not show up?
    * `P(X < 80) = 1 - P(X = 80) = 0.003847 = 99.6%


## Sources
* [Online equation editor](http://www.sciweavers.org/free-online-latex-equation-editor)
  * Bernoulli random variable: `X =\begin{cases}1 & success\\0 & failure\end{cases}`
  * Failure Probability: `P(X = 0) = 1 - p`
  * Success Probability: `P(X = 1) = p`
  * Distribution Function: `F(x) =\begin{cases}0 & x < 0\\1 - p & 0  \leq x < 1\\1 & x  \geq 1\end{cases}`
  * Binomial Distribution: `P(X = x) = (\frac{n}{x})p^x(1 - p)^{n - x}`
  * Bernoulli Standard Deviation: `\sigma =  \sqrt{p(1-p)} `
  * Coin flip example: `(\frac{5}{3})0.5^3(1 - 0.5)^{5 - 3} = (\frac{5}{3})0.5^3(0.5)^{2} = 0.05208 \overline{3} `
  * Plane ticket example: `(\frac{50}{50})0.95^{50}(1 - 0.95)^{50 - 50} = 0.95^{50}(0.05) = 0.003847`
* [Some probabilistic models](http://www.est.uc3m.es/esp/nueva_docencia/getafe/economia/estadistica_I/doc_generica/Chapt1_Part-C_Print.pdf)
* [What is the difference and relationship between the binomial and Bernoulli distributions?](https://math.stackexchange.com/questions/838107/what-is-the-difference-and-relationship-between-the-binomial-and-bernoulli-distr)
* [SD of a bernoulli trial?](https://math.stackexchange.com/questions/1716156/sd-of-a-bernoulli-trial)
