import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

grade_column = 'G3'

df = pd.read_csv('temp/student-por.csv')

for col in df.columns: 
    print(col)

print(df.head(5))

# uncomment describe the columns (get brief stats)
# print(df.describe())

# just describe the grades
print('\nGrade stats')
print(df[grade_column].describe())

# get counts for values
print('\nGrade counts')
print(df[grade_column].value_counts())
print('\n')

# correlation of coeffient
# this only handles correlation between numerical values
r1 = df.corr()[grade_column].sort_values()
print(r1)

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
dummy_df['Grade'] = df[grade_column]
# find correlations (absolute value)
r2 =  dummy_df.corr()['Grade'].sort_values(ascending=False)

def format_data(df, target_col=grade_column):
    '''
    do both numerical and categorical, and get the most correlated
    '''
    labels = df[target_col]
    df = pd.get_dummies(df)
    most_correlated = df.corr().abs()[target_col].sort_values(ascending=False)
    most_correlated = most_correlated[:12]
    df = df.ix[:, most_correlated.index]
    X_train, X_test, y_train, y_test = train_test_split(df, 
                                                        labels,
                                                        test_size=0.25,
                                                        random_state=42)
    
    return X_train, X_test, y_train, y_test

X_train, X_test, y_train, y_test = format_data(df)
print(X_train.head())