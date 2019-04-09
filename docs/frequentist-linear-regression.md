# Frequentist Linear Regression

* The goal of linear regression is to model the relationship two series of data <strong><em>x</em></strong> and <strong><em>y</em></strong> for  where

* Let <strong><em>x</em></strong> and <strong><em>y</em></strong> be bivariate data <strong><em>(x<sub>i</sub>, y<sub>i</sub>)</em></strong> for <strong><em>i = 1,&hellip;,n</em></strong>.
* <strong>Linear Regression</strong> - find a relationship for bivariate data <strong><em>(x<sub>i</sub>, y<sub>i</sub>)</em></strong>  where <strong><em>y = f(x)</em></strong> is a good fit.
  * <strong>Independent/Predictor Variable</strong> - <strong><em>x<sub>i</sub></em></strong> is not random
  * <strong>Dependent/Response Variable</strong> - <strong><em>y<sub>i</sub></em></strong> is some function of <strong><em>x<sub>i</sub></em></strong>, and with random noise
* <strong>Lease Squares Fit</strong> - a line that fits the data. We want to find this line:
  > ![solve for y](./img/499f110f-7df9-4395-98ce-0cd625f9f650.png)<!--
    y = \beta_1x + \beta_0
    -->
* In Frequentist Linear Regression, the model is informed just by the data, and everything we need to know for the model will come from the data.
  * Plug in some new value for <strong><em>x</em></strong> with the above formula and we should get the mostly like result, given the data.

### Example

* Let <strong><em>y</em></strong> be the price of stamps every <strong><em>x</em></strong> year.
  ```python
  import numpy as np

  x = np.array([1963, 1968, 1971, 1974, 1975, 1978, 1981, 1985, 1988, 1991, 1995,
      1999, 2001, 2002, 2006, 2007, 2008, 2009, 2012, 2013, 2014])
  y = np.array([.05, .06, .08, .10, .13, .15, .20, .22, .25, .29, .32, .33, .34,
      .37, .39, .41, .42, .44, .45, .46, .49])
  ```
* Solve for `y = Ap`, where `A = [[x 1]]` and `p = [[m], [c]]`
  ```python
  A = np.vstack([x, np.ones(len(x))]).T
  # solve for p
  b1, b0 = np.linalg.lstsq(A, y, rcond=None)[0]
  ```
* the result is `y = 0.00879x - 17.23146` for `m` and `c`
* Full code available at [numpy_matplotlib_lstsq.py](../demos/libraries/numpy/numpy_matplotlib_lstsq.py)

<p align="center">
  <img src="./img/c87436b0-d130-4c13-940f-3c1cc936d07d.png" width="540" height='384' />
</p>


### Residuals

* <strong>Residuals (<strong><em>&epsilon;</em></strong>)</strong> -  the difference when comparing the actual data versus applying the formula for the best fit of the data, also known as the error.
  > ![residuals](./img/7946cdb3-5cb5-45e2-9881-85c9a0eb12d3.png)<!--
    y_i = \beta_1x + \beta_0 + \varepsilon_i, \quad i = 1,\ldots,n
    -->
* Finding residuals in Python:
  ```python
  # get errors for each estimated y versus data y
  residuals = [(y[index] - (b1*x_i + b0)) for index, x_i in enumerate(x)]
  # get the sum of the squares of residuals
  residuals_sum = np.linalg.lstsq(A, y, rcond=None)[1][0]
  ```
* The least squares fit (essentially) is trying to find solve the above formula such that the sum of the squares of the errors is as close to zero as possible.
  > ![least squares](./img/1a4d7494-15a3-47d5-a910-0dc642a1854a.png)<!--
    {\mathrm{RSS}(\beta) = \sum_{i=1}^n\varepsilon_i^2 =
    \sum_{i=1}^n(y_i-\beta_1x_i-\beta_0)^2}
    -->
* Assumptions about <strong><em>&epsilon;</em></strong>:
  * <strong><em>&epsilon;</em></strong> are independent variables with a mean <strong><em>0</em></strong> and standard deviation <strong><em>&sigma;</em></strong>
  * <strong><em>&epsilon;</em></strong> follows a normal distribution
* <strong>[Homoscedasticity](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/MIT18_05S14_Reading25.pdf)</strong> the values of <strong><em>&epsilon;</em></strong> have the same variance
* From the above example, graph the residuals and the sum of the squares of residuals to illustrate homoscedasticity.
<p align="center">
  <img src="./img/b4021850-3f4b-4058-9b50-12c379933a1b.png" width="540" height='384' />
</p>
* <strong>Heteroscedastic</strong> - the values of <strong><em>&epsilon;</em></strong> have different variance over <strong><em>x</em></strong>

### Summary: The Simple Linear Regression Model

Define the ["simple linear regression model"](https://newonlinecourses.science.psu.edu/stat501/node/253/) a.k.a. **LINE**

1. The expected value of <em>y<sub>i</sub></em> is a **linear function** of <em>x<sub>i</sub></em>
2. The errors <em>&epsilon;<sub>i</sub></em> are <strong>independent</strong>.
3. <em>&epsilon;<sub>i</sub></em> follows a <strong>normal distribution</strong>.
4. <em>&epsilon;<sub>i</sub></em> has equal variance (homoscedasticity).

### Coeffient of Determination, <em>R<sup>2</sup></em>

We will never know the true value of the variance <em>&sigma;<sup>2</sup></em> for the errors, because it is a population parameter. However, [recall that the sample variance for a population](./frequentist-statistics.md#student-t-distribution)  with unknown standard deviation follows a student&rsquo;s t-distribution.

> ![sample variance](./img/3d1c5ddb-cd37-41d8-a84a-3f3a32198636.png)

Important question: how much of variance of <em>y</em> is described by the variance of <em>x</em>?
* We can indirectly answer that by finding how much of the variance of  <em>y</em> is not describe by <em>x</em>? That&rsquo;s just the residual sum of squares
* (The variance of <em>y</em> comes from how far all the values of y is from the mean of y.)
* In other words,
  > ![r](./img/fad7f90d-b38f-4fcd-97da-267388481bb8.png)<!--
    R^2 =
    1 - \frac{SS_{residuals}}{SS_{total}} =
    \frac{\sum_{i}\varepsilon_i^2}{\sum_{i}(y_i - \overline{y})^2}
    -->
* <em>R<sup>2</sup></em> is always between 0 and 1.
* If <em>R<sup>2</sup> = 1</em> then the line perfectly describes the data.
* If <em>R<sup>2</sup> = 0</em> then the line is exactly horizontal.
* &ldquo;<em>R<sup>2</sup> &times; 100%</em> of the variation in <em>y</em> is reduced by taking into account predictor <em>x</em>.&rdquo;
  * We say <em>reduced by</em> instead of <em>explained by</em> because the latter implies causality

Let the correlation coefficient <em>R</em> be:
> ![R](./img/249ff7f8-6106-45e2-9a60-6510052cc32f.png)

* If the slope coefficient <em>&beta;<sub>1</sub></em> is positive, then <em>R</em> is positive, and vice versa.
* <em>R</em> is a unitless number. This fact is important because it makes comparing <em>x</em> and <em>y</em> possible even if they are different units.


### Matrix formula

* Write out all the formulas for <strong><em>y</em></strong>:
  > ![y formulas](./img/dde3545f-2885-431e-a931-19f62b142c09.png)<!--
    \newline y_1 = \beta_1x + \beta_0 + \varepsilon_1
    \newline y_2 = \beta_1x + \beta_0 + \varepsilon_2
    \newline \text{ \,} \vdots
    \newline y_n = \beta_1x + \beta_0 + \varepsilon_n
    -->
* Re-write the above formulas [as a matrix equation](https://newonlinecourses.science.psu.edu/stat501/node/382/):
  > ![y matrix](./img/f7d2a7ef-2e5b-4039-a3bb-091e298e8bac.png)<!--
    \begin{bmatrix}y_1\\ y_2\\ \vdots\\ y_n \end{bmatrix} =
    \begin{bmatrix}1 & x_1\\ 1 & x_2\\ \vdots & \vdots \\ 1 & x_n \end{bmatrix}
    \begin{bmatrix}\beta_0\\ \beta_1\end{bmatrix} +
    \begin{bmatrix}\varepsilon_1\\ \varepsilon_2\\ \vdots\\ \varepsilon_n \end{bmatrix}
    -->
* Sibebar: suppose the value of <strong><em>y</em></strong> depends on 2 predictors, <strong><em>x<sub>1</sub></em></strong> and <strong><em>x<sub>2</sub></em></strong>. Then we would try to solve
  > ![two predictors](./img/d596195c-ea94-4b18-8399-7b52bd3a1524.png)<!--
    {y_i = \beta_2x_2 + \beta_1x_1 + \beta_0 + \varepsilon_i,
    \quad i = 1,\ldots,n}
    -->
  * In which case, the matrix would be:
  > ![parabolic matrix](./img/a7e91df8-6231-4090-b43c-5bb7531c4ffa.png)<!--
    \begin{bmatrix}y_1\\ y_2\\ \vdots\\ y_n \end{bmatrix} =
    \begin{bmatrix}1 & x_1 & x_1\\ 1 & x_2 & x_2\\ \vdots & \vdots & \vdots \\ 1 & x_n & x_n \end{bmatrix}
    \begin{bmatrix}\beta_0\\ \beta_1\\ \beta_2\end{bmatrix} +
    \begin{bmatrix}\varepsilon_1\\ \varepsilon_2\\ \vdots\\ \varepsilon_n \end{bmatrix}
    -->

* let the response matrix be <strong><em>y</em></strong>, let the predictor matrix be <strong><em>X</em></strong>, and let the error matrix be <strong><em>&epsilon;</em></strong>. Then:
  > ![linear regression function](./img/f6c1a470-65a3-4b4b-917e-b37b787c89c9.png)<!--
    \mathit{\mathbf{y}} = \mathit{\mathbf{X}}\beta + \varepsilon
    -->
  * <strong><em>X</em></strong> is an <strong><em>n &times; 2</em></strong> matrix
  * <strong><em>Y</em></strong> is an <strong><em>n &times; 1</em></strong> column vector
  * <strong><em>&beta;</em></strong> is an <strong><em>2 &times; 1</em></strong> column vector
  * <strong><em>&epsilon;</em></strong> is an <strong><em>n &times; 1</em></strong> column vector
* Then, for any given <strong><em>y</em></strong>:
  > ![solve transpose](./img/90a1dee8-ff6f-458e-b2b8-54f7a9c1febb.png)<!--
    y_i = \beta^2\mathbf{x}_i^{T} + \varepsilon_i
    -->


## Sources

* [Linear Regression](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/MIT18_05S14_Reading25.pdf) - MIT introduction to statistics
* [Find the sum of the residuals of a least-squares regression](https://kite.com/python/examples/360/numpy-find-the-sum-of-the-residuals-of-a-least-squares-regression)
* [numpy.linalg.lstsq](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.linalg.lstsq.html) - scipy.org reference
* [5.4 - A Matrix Formulation of the Multiple Regression Model](https://newonlinecourses.science.psu.edu/stat501/node/382/)
* [1.3 - The Simple Linear Regression Model](https://newonlinecourses.science.psu.edu/stat501/node/253/)

