'''
Create 2 subplots in one output
'''
import numpy as np 
import matplotlib.pyplot as plt  
   
# x-points are for 2 pi
x = np.arange(0, 2 * np.pi, 0.1) 

# subplot 1: sine wave
y_sin = np.sin(x) 
# subplot 2: cosine wave
y_cos = np.cos(x)  

# Create a subplot grid height: 2, width: 1, and active
plt.subplot(2, 1, 1)
plt.plot(x, y_sin, ':b') 
plt.title('Sine')  
   
# Second subplot for cosine wave
plt.subplot(2, 1, 2) 
plt.plot(x, y_cos, ':r') 
plt.title('Cosine')  
   
# Show the figure. 
plt.show()