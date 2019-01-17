'''
Create a histogram
'''
import numpy as np 
   
foo_data = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27]) 
# np.histogram(foo_data, bins = [0,20,40,60,80,100]) 
# np.histogram gives back a tuple: the count in each bin, and the bins
histogram_data = np.histogram(foo_data, bins = [0,20,40,60,80,100]) 


hist = histogram_data[0]
bins = histogram_data[1]

print(hist)
print(bins)