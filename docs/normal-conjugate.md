# Normal Conjugate Priors

## The Normal Distribution

* **Normal Distribution** - a continous distribution with notation <em>N(&mu;,&sigma<sup>2</sup></em>, with mean <strong><em>&mu;</em></strong> and variance <strong><em>&sigma;<sup>2</sup></em></strong>
  > ![normal density](./img/fb256a18-8ac2-4e0c-8e41-5d14f780e8bf.png)<!--
    f(x) = \phi(z) = \frac{1}{\sigma \sqrt{2 \pi } }e^{\frac{-(x - \mu)^2}{2\sigma^2}}
    -->
* At <strong><em>x = &mu;</em></strong>, either side of the distibution is symmetrical.
* The mean, mode, and median of a normal distribution are the same.
* <strong><em>&mu; &isin; &#8477;</em></strong> (the mean is a real number)

** Example

* Suppose from a sample <strong><em>n = 30</em></strong> students
  * the mean grade was <strong><em>&#772; = 75</em></strong>
  * the standard deviation was <strong><em>&sigma; = 10</em></strong>
* These students are taken a course that has been taught in the past many times. The class varies each time, yielding a different mean and standard deviation for each class
  * The mean of all the class means is <strong><em>M = 70</em></strong>
  * The standard deviation for the class means is <strong><em>&tau; = 5</em></strong>
* To update our knowledge of <strong><em>&mu;</em></strong>, with the new test data <strong><em>X</em></strong>, we want to find <strong><em>p(&mu;|X)</em></strong>.
* Expressed as Bayes&rsquo; Theorem, where <strong><em>p(X|&mu;)</em></strong> is the likelihood and <strong><em>p(&mu;)</em></strong> is the prior knowledge of the class mean.
  > ![Bayes proportion](./img/fd64907c-9e08-43e2-a81e-d58e2df28a22.png)<!--
    p(\mu|X) \propto p(X|\mu) p(\mu)
    -->
  > ![Likelihood](./img/3840a96b-0e25-4b1e-9258-c19d822d85b1.png)<!--
    {p(X|\mu) = \prod_{i=1}^{n}\frac{1}{\sqrt{2\pi\sigma^2}}e^{\frac{-(x - \mu)^2}{2\sigma^2}}}
    -->
* <strong>Note:</strong> we don&rsquo;t know the true mean; we just have the means of the historical class means.
  * Let <strong><em>M</em></strong> be the mean of the class means and let <strong><em>&tau;</em></strong> be the standard deviation of the class means
  > ![prior](./img/28a1de0d-eb1d-46a7-8177-ad5bdb6e0c46.png)<!--
    p(\mu) = \frac{1}{\sqrt{2\pi\tau^2} }e^{\frac{-(\mu - M)^2}{2\tau^2}}
    -->

* [Bayesian Statistics: Normal-Normal Model](http://www2.bcs.rochester.edu/sites/jacobslab/cheat_sheet/bayes_Normal_Normal.pdf) - Robert Jacobs
* [The Conjugate Prior for the Normal Distribution](https://people.eecs.berkeley.edu/~jordan/courses/260-spring10/lectures/lecture5.pdf) - Michael I. Jordan
* [Conjugate Bayesian analysis of the Gaussian distribution](https://www.cs.ubc.ca/~murphyk/Papers/bayesGauss.pdf) - Kevin P. Murphy
* []