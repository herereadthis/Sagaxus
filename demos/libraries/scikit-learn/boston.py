from sklearn import linear_model
from sklearn import datasets
import pandas as pd
import numpy as np

data = datasets.load_boston()
target_col = 'MEDV'

# Print the boston housing prices description of each column
# print(data.DESCR)


# define the data/predictors as the pre-set feature names  
df = pd.DataFrame(data.data, columns=data.feature_names)
print(df.head(10))

# Put the target (housing value -- MEDV) in another DataFrame
target = pd.DataFrame(data.target, columns=[target_col])
print(target.head(10))

cols = np.append(data.feature_names, target_col)
# print(cols)
# print(data.data)

df2 = df
df2[target_col] = target

print(df2.head(10))

most_correlated = df2.corr().abs()[target_col].sort_values(ascending=False)

print(most_correlated)

# define predictors and responses
X = df
y = target[target_col]

lm = linear_model.LinearRegression()
model = lm.fit(X, y)

# Get R^2, the coeffient of Determination
# See docs/frequentist-statistics.md
r2 = lm.score(X, y)

print('\nR2: {:.4f}'.format(r2))

# Coeffients for all predictors
print(lm.coef_)
# Intercept of line
print(lm.intercept_)
