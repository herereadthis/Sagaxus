import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
import util_functions as uf

grade_col = 'Grade'

df = pd.read_csv('temp/student-por.csv')
df = df.rename(columns={'G3': grade_col, 'Medu': 'mother_edu', 'Fedu': 'father_edu', 'Dalc': 'workday_alc'})

print('\nDataframe columns')
for col in df.columns: 
    print(col)

# if you want to print the first 5 rows
# print(df.head(5))

# uncomment describe the columns (get brief stats)
# print(df.describe())

# just describe the grades
print('\nGrade stats')
print(df[grade_col].describe())

# get counts for values
print('\nGrade counts')
print(df[grade_col].value_counts())
print('\n')

# correlation of coeffient
# this only handles correlation between numerical values
r1 = df.corr()[grade_col].sort_values()
# print(r1)

# 
'''
What about categorical values, like sex?
One-hot encoding: turn categories into one column tables.
For example the table for sex would be two rows, 0 for female, 1 for male
'''
# get the category variables
category_df = df.select_dtypes('object')
# one-hot encode the variables
dummy_df = pd.get_dummies(category_df)
# add back grade column to dummy dataframe
dummy_df['Grade'] = df[grade_col]
# find correlations (absolute value)
r2 = dummy_df.corr()['Grade'].sort_values(ascending=False)

formatted_data = uf.format_dataframe(df, 
                                     target_col=grade_col,
                                     drop_num_cols=['G1', 'G2', 'school'],
                                     drop_cat_cols=['higher_no'])

X_train, X_test, y_train, y_test = formatted_data

# Rename variables in train and teste
X_train = X_train.rename(columns={'higher_yes': 'higher_edu'})

X_test = X_test.rename(columns={'higher_yes': 'higher_edu'})

print(X_train.head())
print(X_train.shape)
print(X_test.shape)

def evaluate_predictions(predictions, true):
    mae = np.mean(abs(predictions-true))
    rmse = np.sqrt(np.mean((predictions - true) ** 2))
    return mae, rmse


median_prediction = df[grade_col].median()
median_predictions = [median_prediction for i in range(len(X_test))]
true = X_test[grade_col]

mb_mae = uf.get_mae(median_predictions, true)
mb_rmse = uf.get_rmse(median_predictions, true)
print('MAE: {:.4f}'.format(mb_mae))
print('RMSE: {:.4f}'.format(mb_rmse))

