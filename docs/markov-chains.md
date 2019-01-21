# Markov Chains

## Define Transition and Stochastic Matrices

* [Suppose in a small town there are three restaurants](https://www.math.ucdavis.edu/~daddel/linear_algebra_appl/Applications/MarkovChain/MarkovChain_9_18/node1.html). For dinner, people have the option of staying at home, the Chinese or Mexican restaurant, or eating at the pizzeria. In other words, on any given night, a household does only 1 of 4 dining options
  * If a household eats at home, then on the next day they have a 20% chance eating Chinese, 25% Mexican, and 30% pizzeria.
  * If a household eats at the Chinese restaurant, they have a 25% chance of staying home the next night, 25% chance Mexican, and 30% pizzeria.
  * If a household eats at a Mexican restaurant, they will eat at home 25% of the time on the next night, 20% Chinese, and 10% pizzeria.
  * If a household eats at the pizzeria, on the next night they have a 30% chance of staying at home for dinner, 30% Chinese, and 10% Mexican.
* After a very long period of time, what is the percentage of households who go to the pizzeria for dinner?
* <strong>[Markov Chain](https://www.math.ucdavis.edu/~daddel/linear_algebra_appl/Applications/MarkovChain/MarkovChain_9_18/node1.html)</strong>
  * There is a physical or mathematical system that has <strong><em>k</em></strong> possible states.
  * At any one time, the system is in one and only one of those <strong><em>k</em></strong> states.
  * For any observation at the <strong><em>n<sup>x</sup></em></strong> period, the probability of the system being in some state only depends on which state the system was in during the <strong><em>n<sup>x-1</sup></em></strong> period.
* For the restaurant example, there are are only <strong><em>k = 4</em></strong> states.
* Let <strong><em>a<sub>ij</sub></em></strong> be the probability of the system to be in state <strong><em>i</em></strong> after it was in state <strong><em>j</em></strong>
* <strong>Transition Matrix</strong> of the Markov Chain - a matrix <strong><em>A = (a<sub>ij</sub>)</em></strong>
  > ![Restaurant transistion matrix](./img/6e186b3f-0b6b-48b5-8220-7a7caf0adb9b.png)<!--
    A =
    \begin{bmatrix}
    .25 & .20 & .25 & .30 \\
    .20 & .30 & .25 & .30 \\
    .25 & .20 & .40 & .10 \\
    .30 & .30 & .10 & .30
    \end{bmatrix}
    -->
* Or represented as a table

<table>
  <tr>
    <td colspan="2" rowspan="2"></td>
    <td colspan="4" align="center">Tomorrow night</td>
  </tr>
  <tr>
    <td>Home</td>
    <td>Chinese</td>
    <td>Mexican</td>
    <td>Pizzeria</td>
  </tr>
  <tr>
    <td rowspan="4" valign="middle">Tonight</td>
    <td>Home</td>
    <td>.25</td>
    <td>.20</td>
    <td>.25</td>
    <td>.30</td>
  </tr>
  <tr>
    <td>Chinese</td>
    <td>.20</td>
    <td>.30</td>
    <td>.25</td>
    <td>.30</td>
  </tr>
  <tr>
    <td>Mexican</td>
    <td>.25</td>
    <td>.20</td>
    <td>.40</td>
    <td>.10</td>
  </tr>
  <tr>
    <td>Pizzeria</td>
    <td>.30</td>
    <td>.30</td>
    <td>.10</td>
    <td>.30</td>
  </tr>
</table>

* <strong>Stochastic Matrix</strong> - a square matrix where:
  * <strong>Right Stochastic</strong> - the sum of each row is 1
  * <strong>Left Stochastic</strong> - the sum of each column is 1
  * <strong>Doubly Stochastic</strong> - sums of rows and columns add up to 1

## Solving for the System

* What is the probability of the system being in the <strong><em>i<sup>th</sup></em></strong> state at the <strong><em>n<sup>th</sup></em></strong> observation?
* <strong>State Vector</strong> - a <strong><em>1 &times; k</em></strong> matrix for the observation period <strong><em>n</em></strong> where <strong><em>x<sub>i</sub></em></strong> represents the probability the system in the <strong><em>i<sup>th</sup></em></strong> state.
  > ![State Vector](./img/fe90c46f-3f0e-42aa-90f1-74fbe18eec39.png)<!--
    x^{n} = \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_k \end{bmatrix}
    -->
  * The sum of all the values in the state ector has to be 1.
* Since the point of a Markov chain is that over many observations the probability of being in any state is independent of where you started, let the initial state be at home for the above example.
  > ![Initial State](./img/41342246-5b74-4190-81ae-691a80d843f4.png)<!--
    x^{0} = \begin{bmatrix} 1 \\ 0 \\ 0\\ 0 \end{bmatrix}
    -->
* Given this initial state, what are the probabilites of dining choice the next night?
  > ![x1 state](./img/87cc8a0e-e22f-4520-b12e-2790735eccd0.png)<!--
    {x^1 = Ax^0 =
    \begin{bmatrix}
    .25 & .20 & .25 & .30 \\
    .20 & .30 & .25 & .30 \\
    .25 & .20 & .40 & .10 \\
    .30 & .30 & .10 & .30
    \end{bmatrix}
    \begin{bmatrix} 1 \\ 0 \\ 0\\ 0 \end{bmatrix} =
    \begin{bmatrix} .25 \\ .20 \\ .25\\ .30 \end{bmatrix}}
    -->
* And the next night?
  > ![x2 state](./img/5d1708d1-1a19-4e96-bff6-2c19509ec8a4.png)<!--
    {x^2 = Ax^1 =
    \begin{bmatrix}
    .25 & .20 & .25 & .30 \\
    .20 & .30 & .25 & .30 \\
    .25 & .20 & .40 & .10 \\
    .30 & .30 & .10 & .30
    \end{bmatrix}
    \begin{bmatrix} .25 \\ .20 \\ .25\\ .30 \end{bmatrix} =
    \begin{bmatrix} .25500 \\ .26250 \\ .23250 \\ .25000 \end{bmatrix}}
    -->


## Sources

* [Markov Chains](https://www.math.ucdavis.edu/~daddel/linear_algebra_appl/Applications/MarkovChain/MarkovChain_9_18/node1.html)
