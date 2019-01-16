'''
Create a sine wave with numpy and matplotlib
'''
import numpy as np 
import matplotlib.pyplot as plt  

# Compute the x and y coordinates for points on a sine curve 
x = np.arange(0, 3 * np.pi, 0.1) 
y = np.sin(x) 
plt.title('sine wave form') 

plt.plot(x, y, ':r') 
plt.show() 