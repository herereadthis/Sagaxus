# Matplotlib: a Python 2D plotting library

## Plot styles

### Selected lines and markers (not comprehensive)

<table>
    <thead>
        <tr>
            <th>Symbol</th>
            <th>Appearance</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>`-`</td>
            <td>Solid line</td>
        </tr>
        <tr>
            <td>`--`</td>
            <td>Dashed line</td>
        </tr>
        <tr>
            <td>`-.`</td>
            <td>Dash-dot line</td>
        </tr>
        <tr>
            <td>`:`</td>
            <td>Dotted line</td>
        </tr>
        <tr>
            <td>`.`</td>
            <td>Point marker</td>
        </tr>
        <tr>
            <td>`+`</td>
            <td>Plus marker</td>
        </tr>
        <tr>
            <td>`D`</td>
            <td>Diamond marker</td>
        </tr>
        <tr>
            <td>`*`</td>
            <td>Star marker</td>
        </tr>
        <tr>
            <td>`o`</td>
            <td>Circle marker</td>
        </tr>
        <tr>
            <td>`s`</td>
            <td>Square marker</td>
        </tr>
    </tbody>
</table>

### Colors


<table>
    <thead>
        <tr>
            <th>Symbol</th>
            <th>Color</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>`b`</td>
            <td>Blue</td>
        </tr>
        <tr>
            <td>`g`</td>
            <td>Green</td>
        </tr>
        <tr>
            <td>`r`</td>
            <td>Red</td>
        </tr>
        <tr>
            <td>`c`</td>
            <td>Cyan</td>
        </tr>
        <tr>
            <td>`m`</td>
            <td>Magenta</td>
        </tr>
        <tr>
            <td>`y`</td>
            <td>Yellow</td>
        </tr>
        <tr>
            <td>`k`</td>
            <td>Black</td>
        </tr>
        <tr>
            <td>`w`</td>
            <td>White</td>
        </tr>
    </tbody>
</table>

```python
# plot style: o=circle, b=blue
plt.plot(x,y,"ob")
```

## Let&rsquo;s make a simple plot

* Full code example at [matplotlib_03_plot.py](../../demos/libraries/matplotlib/matplotlib_03_plot.py)

* Definitions:
  <strong>Figure</strong> - the whole thing
  <strong>Axes</strong> - the space where the stuff will be drawn
  <strong>Axis</strong> - the part that defines the range of x and y, along the edge. z also if more dimensions

* `pyplot.plot()` - plots curves
  * Remember: the plots are always expecting numpy arrays. Turn everything into a numpy array.
  * Expects an numpy array x-values and a numpy array of y-values
  * Notable params: `color`, `linestyle` (see above reference), `linewidth`, `label`
  * You need to specify `label` to get stuff to show in the legend
  * doing the `plot` method multiple times, you can plot lots of things onto the same axes

```python
import numpy as np
from matplotlib import pyplot as plt

'''
numpy.linspace creates an array to specify the number of intervals in a range. 
In this case, create a 100 intervals between 0 and 2
'''
x = np.linspace(0, 2, 100)

def linear(value):
    return value**1

def quadratic(value):
    return value**2

def cubic(value):
    return value**3

curves = [
    {'get_y': linear, 'color': 'b', 'linestyle': '-', 'label': 'Linear'},
    {'get_y': quadratic, 'color': 'r', 'linestyle': ':', 'label': 'Quadratic'},
    {'get_y': cubic, 'color': 'g', 'linestyle': '-.', 'label': 'Cubic'}
]

for curve in curves:
    plt.plot(
        x,
        curve['get_y'](x),
        color= curve['color'],
        linestyle=curve['linestyle'],
        linewidth=2,
        # label is what shows up in the legend
        label=curve['label']
    )
```

* Label the figure
  * `pyplot.xlabel()` - sets label for x-axis
  * `pyplot.ylabel()` - sets label for y-axis
  * `pyplot.title()` - sets label for title

```python
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('Simple Plot')
```

* Figure enhancements
  * `pyplot.legend()` creates the legend
  * `pyplot.grid()` puts a grid into the axes. It has a `color` kwarg.

```python
plt.legend()
plt.grid(color='#DDDDDD')
```

* Figure range
  * `pyplot.xlim()` sets the range for x-values visible in axes
  * `pyplot.ylim()` sets the range for y-values visible in axes

```python
plt.xlim(0, 2)
plt.ylim(0, 8)
```

* `pyplot.show()` does the rendering

```python
plt.show()
```
