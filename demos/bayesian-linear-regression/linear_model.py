import pandas as pd
import matplotlib.pyplot as plt
import util_functions as uf
import pymc3 as pm
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

grade_col = 'Grade'

df = pd.read_csv('temp/student-por.csv')
df = df.rename(columns={'G3': grade_col,
                        'Medu': 'mother_edu',
                        'Fedu': 'father_edu',
                        'Dalc': 'workday_alc'})

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

# show graph of models against baseline
# results = uf.evaluate_lr_models(X_train, X_test, y_train, y_test, grade_col)
# uf.build_models_graph(results)

ols_intercept = uf.get_ols_intercept(X_train, y_train, grade_col)
ols_coefficients = uf.get_ols_coeffients(X_train, y_train, grade_col)
ols_formula = uf.get_ols_formula(ols_intercept, ols_coefficients, grade_col)

print('\nOrdinary Least Squares')
print(ols_formula)

normal_trace = uf.estimate_parameters(X_train, grade_col, draws=500)
'''
# show this as a crazy graph
uf.plot_trace(normal_trace)

# histogram of modifiers for each feature
pm.plot_posterior(normal_trace)

plt.show()
'''

# get summary of model parameters
print(pm.summary(normal_trace))

# show graph of models, and also bayesian modelling, against baseline
results = uf.evaluate_lr_models(X_train, X_test, y_train, y_test, grade_col)
all_model_results = uf.evaluate_trace(normal_trace, X_train, X_test, y_train, 
                                      y_test, results)
print(all_model_results)
# uf.build_models_graph(all_model_results)

# test model against test data
# uf.test_model(normal_trace, X_test.iloc[41])

# observation = pd.Series({'Intercept': 1, 'mother_edu': 2, 'failures': 2, 
#                          'higher_edu': 1, 'studytime': 2, 'father_edu': 3,
#                          'workday_alc': 1})
# uf.query_model(normal_trace, observation)


def model_effect(query_var, trace, X):
    '''
    Given a response with multiple variables, show the effect of changing one
    variable while keeping all others at median.
    Params: variable name, trace, and data
    '''

    # Variables that do not change
    steady_vars = list(X.columns)
    steady_vars.remove(query_var)

    def lm(value, sample):
        '''
        Estimate (as a linear model) the response based on the value of the
        query variable and one sample from the trace.
        '''

        # Prediction is the estimate given a value of the query variable
        prediction = sample['Intercept'] + sample[query_var] * value

        # Each non-query variable is assumed to be at the median value
        for var in steady_vars:
            # Multiply the weight by the median value of the variable
            prediction += sample[var] * X[var].median()

        return prediction

    plt.figure(figsize=(6, 6))

    # Find the minimum and maximum values for the range of the query var
    var_min = X[query_var].min()
    var_max = X[query_var].max()

    # Plot the estimated grade versus the range of query variable
    pm.plot_posterior_predictive_glm(trace, 
                                     eval=np.linspace(var_min, var_max, 100), 
                                     lm=lm, samples=100, color='blue', 
                                     alpha=0.4, lw=2)

    # Plot formatting
    plt.xlabel('%s' % query_var, size=16)
    plt.ylabel('Grade', size=16)
    plt.title("Posterior of Grade vs %s" % query_var, size=18)
    plt.show()

model_effect('mother_edu', normal_trace, X_train.drop(columns='Grade'))

'''
Notes
df_summary have been removed, use summary instead
https://github.com/pymc-devs/pymc3/blob/master/RELEASE-NOTES.md
'''
