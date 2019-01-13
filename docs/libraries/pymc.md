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
import pymc as pm
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

In PyMC3 handle all the variables in the model within the context of the `Model()` object.
* Any variables created within a given `Model`'s context will be assigned to that model.
* You can name the `Model` anything you want; naming it `model` is okay.
* You cannot instantiate PyMC variables outside of the context of a model.

```python
import pymc3 as pm

with pm.Model() as model:
    parameter = pm.Exponential('poisson_param', 1.0)
    data_generator = pm.Poisson('data_generator', parameter)

with model:
    data_plus_one = data_generator + 1
```

It's possible to examine a varabile outside of the model context once it has been defined

```python
print(data_plus_one.tag.test_value)
```

You can create a different model object with the same name as a previously used one

```
with pm.Model() as model:
    theta = pm.Exponential('theta', 2.0)
    data_generator = pm.Poisson('data_generator', theta)
```

You can also create separate models

```python
with pm.Model() as ab_testing:
    p_A = pm.Uniform('P(A)', 0, 1)
    p_b = pm.Uniform('P(B)', 0, 1)
```

All PyMC3 have an initial value `test_value`
* It will not change as a result if sampling

```python
print('parameter.tag.test_value = {}'.format(paramater.tag.test_value))
# you will get the same value again.
print('parameter.tag.test_value = {}'.format(paramater.tag.test_value))
```

Use `testval` initialize a variable with a specific initial value.
* This is useful if you have an unsable prior which requires a better starting point.

```python
with pm.Model() as model:
    parameter = pm.Exponential('poisson_param, 1.0, testval = 0.5)

print('parameter.tag.test_value = {}'.format(paramater.tag.test_value))
# parameter.tag.test_value = 0.5
```

There are two types of PyMC3 programming variables:
* <em>Stochastic</em> - variables that are not deterministic. It&rsquo;s random, even if you knew all the values of the variables&rsquo; parameters and components.
  * Examples: instances of `Poisson`, `DiscreteUniform`, and `Exponential` classes
* <em>Deterministic</em> - variables that are not random if you know the variables&rsquo; parameters and components.

Initialize a stochastic variable with a `name` argument, plus any additional parameters specific to the class. Example below:
* (0, 4) are the `DiscreteUniform`-specific bounds of the random variable.
* `discrete_uniform_var` is the `name`, which is used to get the posterior distribution later.

```python
import pymc3 as pm
my_variable = pm.DiscreteUniform('discrete_uniform_var', 0, 4)
```

Use the `shape` keyword to create multivariate arrays. You need to do this for problems which use multiple variables.
* Multivariate arrays will behave like numpy arrays
* if you do a `tag.test_value` on the array, you get a numpy array.

```python
import pymc3 as pm
# instead of doing this:
beta_1 = pm.Uniform('beta_1', 0, 1)
beta_2 = pm.Uniform('beta_2', 0, 1)
# do this:
betas = pm.Unifrom('betas', 0, 1, shape=2)
```

Create a deterministic variables by using the `Deterministic` class

```python
some_determistic_variable = pm.Deterministic('deterministic_varaible', <some_function_of_variables>)
```

If you use elementary operations like addding or exponentials, you implicitly create deterministic variables.
* but to make sure the variable is tracked by sampling, use the constructor.

```python
with pm.Model() as model:
    lambda_1 = pm.Exponential('lambda_1', 1.0)
    lambda_2 = pm.Exponential('lambda_2', 1.0)
    tau = pm.DiscreteUniform('tau', lower=0, upper=10)

new_deterministic_variable = lambda_1 + lambda_2
```

## Sources

* [Chapter 2: A little more on PyMC3](https://nbviewer.jupyter.org/github/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/blob/master/Chapter2_MorePyMC/Ch2_MorePyMC_PyMC3.ipynb)
