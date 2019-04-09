import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

grade_column = 'G3'

df = pd.read_csv('temp/student-por.csv')

# Histogram of grades
bins = np.arange(0, 20, 1)
plt.hist(df[grade_column], bins=bins, color='b', edgecolor='k')
plt.xlim(0, 20)
plt.xticks(bins)
plt.xlabel('Grade')
plt.ylabel('Count')
plt.title('Distribution of Final Grades')

plt.show()