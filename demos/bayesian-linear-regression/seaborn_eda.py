import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv('temp/student-por.csv')

# Make one plot for each different location
sns.kdeplot(df.ix[df['address'] == 'U', 'G3'], 
            label = 'Urban', shade = True)
sns.kdeplot(df.ix[df['address'] == 'R', 'G3'], 
            label = 'Rural', shade = True)
# Add labeling
plt.xlabel('Grade')
plt.ylabel('Density')
plt.title('Density Plot of Final Grades by Location')

plt.show()