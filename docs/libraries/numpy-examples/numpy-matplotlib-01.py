import numpy as np 
from matplotlib import pyplot as plt 

x = np.arange(1,11) 
y = 2 * x + 5 

# output: [ 1  2  3  4  5  6  7  8  9 10]
print(x)
#output: [ 7  9 11 13 15 17 19 21 23 25]
print(y)

# set title
plt.title('Matplotlib demo') 

# set label for x-axis
plt.xlabel('x axis caption') 

# set label for y-axis
plt.ylabel('y axis caption') 

# plot style: o=circle, b=blue
plt.plot(x,y, ',b') 
plt.show()