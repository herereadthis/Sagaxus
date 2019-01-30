'''
Create a basic plot of curves
'''
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
    {
        'get_y': linear,
        'color': 'b',
        'linestyle': '-',
        'label': 'Linear'
    },
    {
        'get_y': quadratic,
        'color': 'r',
        'linestyle': ':',
        'label': 'Quadratic'
    },
    {
        'get_y': cubic,
        'color': 'g',
        'linestyle': '-.',
        'label': 'Cubic'
    }
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

# pyplot.xlabel() sets label for x-axis
plt.xlabel('x label')
# pyplot.ylabel() sets label for y-axis
plt.ylabel('y label')
# pyplot.title() sets label for title
plt.title("Simple Plot")

# pyplot.legend() creates the legend
plt.legend()
# pyplot.grid() puts a grid into the axes
plt.grid(color='#DDDDDD')

# pyplot.xlim() sets the range for x-values visible in axes
plt.xlim(0, 2)
# pyplot.ylim() sets the range for y-values visible in axes
plt.ylim(0, 8)

# pyplot.show() does the rendering
plt.show()
