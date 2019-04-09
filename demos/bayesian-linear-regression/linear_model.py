import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

grade_col = 'Grade'

df = pd.read_csv('temp/student-por.csv')
df = df.rename(columns={'G3': grade_col, 'Medu': 'mother_edu', 'Fedu': 'father_edu', 'Dalc': 'workday_alc'})


def format_data(df, target_col=grade_col, drop_num_cols=[], drop_cat_cols=[]):
    '''
    do both numerical and categorical, and get the most correlated
    '''
    labels = df[target_col]
    df = df.drop(columns=drop_num_cols)
    df = pd.get_dummies(df)
    most_correlated = df.corr().abs()[target_col].sort_values(ascending=False)
    most_correlated = most_correlated[:8]
    df = df.ix[:, most_correlated.index]
    df = df.drop(columns=drop_cat_cols)
    X_train, X_test, y_train, y_test = train_test_split(df, 
                                                        labels,
                                                        test_size=0.25,
                                                        random_state=42)
    
    return X_train, X_test, y_train, y_test

X_train, X_test, y_train, y_test = format_data(df, 
                                            target_col=grade_col,
                                            drop_num_cols=['G1', 'G2', 'school'],
                                            drop_cat_cols=['higher_no'])

# Rename variables in train and teste
X_train = X_train.rename(columns={'higher_yes': 'higher_edu'})

X_test = X_test.rename(columns={'higher_yes': 'higher_edu'})

print(X_train.head())
print(X_train.shape)
print(X_test.shape)
