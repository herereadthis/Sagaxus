'''
Create a bar graph with two sets of data
Reference: sagaxus/docs/numpy.md
'''
import matplotlib.pyplot as plt 
x1 = [5,8,10] 
y1 = [12,16,6]  

x2 = [6,9,11] 
y2 = [6,15,7] 

plt.bar(x1, y1, color='c', align='center', edgecolor='k') 
plt.bar(x2, y2, color='m', align='center', edgecolor='k') 
plt.title('Bar graph') 
plt.ylabel('Y axis') 
plt.xlabel('X axis')  

plt.show()
