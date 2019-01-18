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