
# Exponential Distribution

The exponential distribution describes the time between events of a Poisson process.

> ![exponential distribution](./img/66a23887-dc19-4af7-84d3-d41ad019ffa8.png)<!--
  F(x)=1 -e^{-\lambda x}, x \ge 0
  -->

* Elaspsed time becomes the random variable.
* If the number of births within a time interval can be modelled as a Poisson distribution, then the time between births is an exponential distribution.
* The exponential distibution is used to test product reliability
* It can also be used to build Markov chains
* Other examples:
  * How much time will go by before a hurricane hits the East Coast?
  * How long will a car transmission last before it breaks?
* <strong>Exponential distributions are <em>Memoryless.</em></strong> - it does not care what came before.
  * If you are waiting for an event to occur, the length of time waiting neither increases nor decreases the probability of the event happening.
  * Suppose the probability of a taxi arriving in the next five minutes is <em>p</p>. If no taxi arrives, the probablity of a taxi arriving in the next five minutes is still <em>p</p>

* Expected Value equals standard deviation
  > ![expected exponential](./img/44526e2d-f368-43d9-9164-7bd7270b9463.png)<!--
    E(X) = \frac{1}{\lambda} = \sigma
    -->
* Variance
  > ![variance exponential](./img/f3e39dd4-2bfe-4c1c-bd4a-e119f1b743af.png)<!--
    \sigma^2 = \frac{1}{\lambda^2}
    -->

## Sources
* [Online equation editor](https://www.codecogs.com/latex/eqneditor.php)
* [Exponential Distribution / Negative Exponential: Definition, Examples](https://www.statisticshowto.datasciencecentral.com/exponential-distribution/)
* [Exponential Distribution](https://www.statlect.com/probability-distributions/exponential-distribution)
