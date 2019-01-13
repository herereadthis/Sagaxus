# PyMC

## PyMC2

There are <em>parent</em> and <em>child</em> variables
* <em>Parent</em> variables influence another variable.
* <em>Child</em> variables are affected by other variables.
* A variable can be both <em>parent</em> and <em>child</em>.

```python
import pymc as pm

parameter = pm.Exponential('poisson_param', 1)
# data_generator is influenced by parameter, so parameter is a parent and data_generator is a child varable.
data_generator = pm.Poisson('data_generator', parameter)
'''
data_plus_one is influenced by data_generator, so data_generator is both a parent and child variable.
All three variables are PyMC variables.
'''
data_plus_one = data_generator + 1
```

You can access a variable's parent and children using `parents` and `children` attributes.

```python
print('children of parameter: {}'.format(parameter.children))
print('parents of data_generator: {}'.format(data_generator.parents))
print('children of data_generator: {}'.format(data_generator.children))
```

All PyMC variables also have a `value` attribute which gives the current (could be random) internal value of the variable.
  * If the variable is a child variable, its value changes given the parents&rsquo; value.

```python
print('parameter.value: {}'.format(parameter.value))
print('data_generator.value: {}'.format(data_generator.value))
print('data_plus_one.value: {}'.format(data_plus_one.value))
```

There are two types of PyMC programming variables:
* <em>Stochastic</em> - variables that are not deterministic. It&rsquo;s random, even if you knew all the values of the variables&rsquo; parents.
  * Examples: instances of `Poisson`, `DiscreteUniform`, and `Exponential` classes
* <em>Deterministic</em> - variables that are not random if you know the variables&rsquo; parents.

To initialize  a stochastic variable, you need a `name` argument, plus any other variables that are class-specific. Example below:
 * (0, 4) are the `DiscreteUniform`-specific bounds of the random variable.
 * `discrete_uniform_var` is the `name`, which is used to get the posterior distribution later.

```python
import pymc3 as pm
my_variable = pm.DiscreteUniform('discrete_uniform_var', 0, 4)
```

Use the `size` argument to create multivariate arrays. You need to do this for problems which use multiple variables.
* Multivariate arrays will behave like numpy arrays

```python
import pymc as pm
# instead of doing this:
beta_1 = pm.Uniform('beta_1', 0, 1)
beta_2 = pm.Uniform('beta_2', 0, 1)
# do this:
betas = pm.Unifrom('betas', 0, 1, size=2)
```

## PyMC3




## Sources

* [Chapter 2: A little more on PyMC3](https://nbviewer.jupyter.org/github/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/blob/master/Chapter2_MorePyMC/Ch2_MorePyMC_PyMC3.ipynb)
