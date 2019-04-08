import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('temp/student-por.csv')
# foo = pd.DataFrame(df)

print(df.head(5))




# Histogram of grades
bins = np.arange(0, 20, 1)
plt.hist(df['G3'], bins=bins, color='b', edgecolor='k')
plt.xlim(0, 20)
plt.xticks(bins)
plt.xlabel('Grade')
plt.ylabel('Count')
plt.title('Distribution of Final Grades')

plt.show()