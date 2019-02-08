# SciPy

This isn't comprehensive, just a list of useful methods

## `stats.bernoulli`

* Think of Bernoulli trials as coin flips where 1 is heads, 0 is tails
* The probability of heads is <em>&theta;</em>
* Methods
  `rvs(p, loc=0, size=1, random_state=None)` - mostly interested in <em>&theta;</em> and size

```python
from scipy import stats

# generate 1000 coin flips for a fair coin
foo = stats.bernoulli.rvs(0.5, 1000)
```

### scipy.stats.norm

* Do stuff with the normal distribution
* `.rvs()` - generate random values
  * `size` - number of samples
  * `loc` - mean
  * `scale` - standard deviation
  * `random_state` seed for pseudo random number generator

```python
import scipy.stats
data = scipy.stats.norm.rvs(size=100000, loc=0, scale=1.5, random_state=123)
```

### scipy.stats.rv_histogram

* Generate stats given by a histogram.
