# Bayesian Programming

Notes from Probabilistic Programming and Bayesian Methods for Hackers

* Measure probability in terms of the believability of an event. How confident are we the event will occur?


## Example

* Suppose the number of text messages are recorded every day for a period of time. Can we detect a change in behavior (e.g. texts increase or decrease over time at some point)
* For day <em>i</em> with count <em>C<sub>i</sub></em>, we can say <em>C<sub>i</sub> = Poisson(&lambda;)</em>
* For all the days <strong><em>t</em></strong> during the observation period, choose some day <strong>&tau;</strong> such that <strong>&lambda;</strong> before <strong>&tau;</strong> is lower than <strong>&tau;</strong> after <strong>&tau;</strong>. Let this day be called the <em>switchpoint</em>
  > ![poisson switchpoint](./img/36816d8a-5c19-4525-93c1-c81988b65fc9.png)<!--
  {\lambda = \begin{cases}\lambda_1 & t < \tau\\\lambda_2 & t \ge\tau\end{cases}}
  -->
* If no change occurred, then both lambdas are equal, and the posterior distributions for each should be equal.