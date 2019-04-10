import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import ElasticNet
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import matplotlib
import pymc3 as pm
import seaborn as sns


def format_dataframe(df,
                     target_col,
                     drop_num_cols=[],
                     drop_cat_cols=[]):
    '''
    do both numerical and categorical, and get the most correlated
    '''
    labels = df[target_col]
    # drop numerical columns for which we don't want to see correlations
    df = df.drop(columns=drop_num_cols)
    # convert entries in categorical columns to entries (e.g. F=0,M=1 for sex)
    df = pd.get_dummies(df)
    # sort columns by highest Correlation coefficient
    most_correlated = df.corr().abs()[target_col].sort_values(ascending=False)
    # get the most correlated
    most_correlated = most_correlated[:8]
    df = df.loc[:, most_correlated.index]
    df = df.drop(columns=drop_cat_cols)
    X_train, X_test, y_train, y_test = train_test_split(df,
                                                        labels,
                                                        test_size=0.25,
                                                        random_state=42)

    return X_train, X_test, y_train, y_test


def get_mae(predictions, responses):
    '''
    Get the Mean Absolute Error (MAE)
    '''
    return np.mean(abs(predictions - responses))


def get_rmse(predictions, responses):
    '''
    Get the Root Mean Squared Error (RMSE)
    '''
    return np.sqrt(((predictions - responses) ** 2).mean())


def get_ols(x_data, y_data, target_col):
    '''
    Get linear regression, given predictor and response lists
    '''
    lr = LinearRegression()
    return lr.fit(x_data.drop(columns=target_col), y_data)


def get_ols_intercept(x_data, y_data, target_col):
    '''
    Get the coefficients for each attribute.
    '''
    lr = get_ols(x_data, y_data, target_col)
    return lr.intercept_


def get_ols_coeffients(x_data, y_data, target_col):
    '''
    Get the coefficients for each attribute.
    '''
    lr = get_ols(x_data, y_data, target_col)
    result = {}
    for column_index, column in enumerate(x_data.columns[1:]):
        result[column] = lr.coef_[column_index]

    return result


def get_ols_formula(intercept, coefficients, target_col):
    '''
    Get multivariate least-squares formula from data.
    '''
    ols_formula = '{} = {:.2f}'.format(target_col, intercept)

    # iterate through python dictionary
    for variable, coefficient in coefficients.items():
        operator = '+' if coefficient >= 0 else '-'
        ols_formula = '{} {} {:.2f} * {}'.format(ols_formula,
                                                 operator,
                                                 abs(coefficient),
                                                 variable)

    return ols_formula


def get_bayesian_lr_formula(x_data, target_col):
    '''
    Get the bayesian linear regression formula.
    '''
    variables = ['%s' % variable for variable in x_data.columns[1:]]
    return 'Grade ~ ' + ' + '.join(variables)


def evaluate_lr_models(X_train, X_test, y_train, y_test, target_col):
    '''
    Evaluate several ml models by training on training set and testing on
    testing set.
    '''
    # Names of models
    model_name_list = [
        'Linear Regression',
        'ElasticNet Regression',
        'Random Forest',
        'Extra Trees',
        'SVM',
        'Gradient Boosted',
        'Baseline'
    ]
    X_train = X_train.drop(columns=target_col)
    X_test = X_test.drop(columns=target_col)

    # Instantiate the models
    models = [
        LinearRegression(),
        ElasticNet(alpha=1.0, l1_ratio=0.5),
        RandomForestRegressor(n_estimators=50),
        ExtraTreesRegressor(n_estimators=50),
        SVR(kernel='rbf', degree=3, C=1.0, gamma='auto'),
        GradientBoostingRegressor(n_estimators=20)
    ]

    # Dataframe for results
    results = pd.DataFrame(columns=['mae', 'rmse'], index=model_name_list)

    # Train and predict with each model
    for i, model in enumerate(models):
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)

        # Metrics
        mae = get_mae(predictions, y_test)
        rmse = get_rmse(predictions, y_test)

        # Insert results into the dataframe
        model_name = model_name_list[i]
        results.loc[model_name, :] = [mae, rmse]

    # Median Value Baseline Metrics
    baseline = np.median(y_train)
    baseline_mae = np.mean(abs(baseline - y_test))
    baseline_rmse = np.sqrt(np.mean((baseline - y_test) ** 2))

    results.loc['Baseline', :] = [baseline_mae, baseline_rmse]

    return results


def build_models_graph(results):
    plt.figure(figsize=(9, 6))

    matplotlib.rcParams['font.size'] = 12
    # Root mean squared error
    ax = plt.subplot(1, 2, 1)
    results.sort_values('mae', ascending=True).plot.bar(y='mae', color='b', ax=ax)
    plt.title('Model Mean Absolute Error')
    plt.ylabel('MAE')

    # Median absolute percentage error
    ax = plt.subplot(1, 2, 2)
    results.sort_values('rmse', ascending=True).plot.bar(y='rmse', color='r', ax=ax)
    plt.title('Model Root Mean Squared Error')
    plt.ylabel('RMSE')

    plt.tight_layout()

    # return results
    plt.show()


def evaluate_trace(trace, X_train, X_test, y_train, y_test, model_results):
    '''
    Evalute the MCMC trace and compare to ml models
    compare Bayesian linear model against baseline and other regression models.
    '''
    
    # Dictionary of all sampled values for each parameter
    var_dict = {}
    for variable in trace.varnames:
        var_dict[variable] = trace[variable]
        
    # Results into a dataframe
    var_weights = pd.DataFrame(var_dict)
    
    # Means for all the weights
    var_means = var_weights.mean(axis=0)
    
    # Create an intercept column
    X_test['Intercept'] = 1
    
    # Align names of the test observations and means
    names = X_test.columns[1:]
    X_test = X_test.ix[:, names]
    var_means = var_means[names]
    
    # Calculate estimate for each test observation using the average weights
    results = pd.DataFrame(index=X_test.index, columns=['estimate'])

    for row in X_test.iterrows():
        results.ix[row[0], 'estimate'] = np.dot(np.array(var_means), np.array(row[1]))
        
    # Metrics 
    actual = np.array(y_test)
    errors = results['estimate'] - actual
    mae = np.mean(abs(errors))
    rmse = np.sqrt(np.mean(errors ** 2))
    
    print('Model  MAE: {:.4f}\nModel RMSE: {:.4f}'.format(mae, rmse))
    
    # Add the results to the comparison dataframe
    model_results.ix['Bayesian LR', :] = [mae, rmse]
    
    return model_results


def estimate_parameters(X_train, target_col, draws=2000, chains=2, tune=500):
    '''
    Build a model from regression formlula.
    Data likelihood is a normal distribution.
    Let as Markov Chain Monte Carlo (MCMC) algorithm draw samples from
    posterior to approximate the posterior for each of the model parameters.
    '''
    bayesian_lr_formula = get_bayesian_lr_formula(X_train, target_col)

    with pm.Model() as normal_model:
        
        # The prior for the model parameters will be a normal distribution
        family = pm.glm.families.Normal()
        
        # Creating the model requires a formula and data (and optionally a family)
        pm.GLM.from_formula(formula=bayesian_lr_formula,
                            data=X_train,
                            family=family)
        
        # Perform Markov Chain Monte Carlo sampling
        normal_trace = pm.sample(draws=draws, chains=chains, tune=tune, njobs=-1)

        return normal_trace


# Shows the trace with a vertical line at the mean of the trace
def plot_trace(trace):
    # Traceplot with vertical lines at the mean value
    ax = pm.traceplot(trace, figsize=(14, len(trace.varnames)*1.8),
                      lines={k: v['mean'] for k, v in pm.summary(trace).iterrows()})
    
    matplotlib.rcParams['font.size'] = 12
    
    # Labels with the median value
    for i, mn in enumerate(pm.summary(trace)['mean']):
        annotation = '{:0.2f}'.format(mn)
        ax[i, 0].annotate(annotation, xy=(mn, 0), xycoords='data', size=8,
                          xytext=(-18, 18), textcoords='offset points', 
                          rotation=90, va='bottom', fontsize='large', 
                          color='red')


# Make a new prediction from the test set and compare to actual value
def test_model(trace, test_observation):
    
    # Print out the test observation data
    print('Test Observation:')
    print(test_observation)
    var_dict = {}
    for variable in trace.varnames:
        var_dict[variable] = trace[variable]

    # Results into a dataframe
    var_weights = pd.DataFrame(var_dict)
    
    # Standard deviation of the likelihood
    sd_value = var_weights['sd'].mean()

    # Actual Value
    actual = test_observation['Grade']
    
    # Add in intercept term
    test_observation['Intercept'] = 1
    test_observation = test_observation.drop('Grade')
    
    # Align weights and test observation
    var_weights = var_weights[test_observation.index]

    # Means for all the weights
    var_means = var_weights.mean(axis=0)

    # Location of mean for observation
    mean_loc = np.dot(var_means, test_observation)
    
    # Estimates of grade
    estimates = np.random.normal(loc=mean_loc, scale=sd_value, size=500)

    # Plot all the estimates
    plt.figure(figsize=(7, 7))
    sns.distplot(estimates, hist=True, kde=True, bins=19,
                 hist_kws={'edgecolor': 'k', 'color': 'darkblue'},
                 kde_kws={'linewidth': 4},
                 label='Estimated Dist.')
    # Plot the actual grade
    plt.vlines(x=actual, ymin=0, ymax=5, linestyles='--', colors='red',
               label='True Grade', linewidth=2.5)
    
    # Plot the mean estimate
    plt.vlines(x=mean_loc, ymin=0, ymax=5, linestyles='-', colors='orange',
               label='Mean Estimate', linewidth=2.5)
    
    plt.legend(loc=1)
    plt.title('Density Plot for Test Observation')
    plt.xlabel('Grade')
    plt.ylabel('Density')
    plt.ylim(0, 0.2)
    
    # Prediction information
    info = np.array([
        actual,
        mean_loc,
        np.percentile(estimates, 5), 
        np.percentile(estimates, 95)
    ])

    info_series = pd.Series(info, index=[
            'True Grade',
            'Average Estimate', 
            '5% Estimate',
            '95% Estimate'
        ])

    print(info_series)
    plt.show()


def query_model(trace, new_observation):
    '''
    Make predictions for a new data point from the model trace
    '''

    # Print information about the new observation
    print('New Observation')
    print(new_observation)
    # Dictionary of all sampled values for each parameter
    var_dict = {}
    for variable in trace.varnames:
        var_dict[variable] = trace[variable]
        
    # Standard deviation
    sd_value = var_dict['sd'].mean()
    
    # Results into a dataframe
    var_weights = pd.DataFrame(var_dict)
    
    # Align weights and new observation
    var_weights = var_weights[new_observation.index]
    
    # Means of variables
    var_means = var_weights.mean(axis=0)
    
    # Mean for observation
    mean_loc = np.dot(var_means, new_observation)
    
    # Distribution of estimates
    estimates = np.random.normal(loc=mean_loc, scale=sd_value,
                                 size=1000)
    
    # Plot the estimate distribution
    plt.figure(figsize=(8, 8))
    sns.distplot(estimates, hist=True, kde=True, bins=19,
                 hist_kws={'edgecolor': 'k', 'color': 'darkblue'},
                 kde_kws={'linewidth': 4}, label='Estimated Dist.')
    # Plot the mean estimate
    plt.vlines(x=mean_loc, ymin=0, ymax=5, linestyles='-',
               colors='orange', linewidth=2.5)
    plt.title('Density Plot for New Observation')
    plt.xlabel('Grade')
    plt.ylabel('Density')
    plt.xlim(0, 20)
    plt.ylim(0, 0.18)
    plt.xticks(np.arange(0, 20, step=2))
    plt.yticks(np.arange(0, 0.18, step=0.02))
    
    # Estimate information
    info = np.array([
        mean_loc,
        np.percentile(estimates, 5), 
        np.percentile(estimates, 95)
    ])

    info_series = pd.Series(info, index=[
            'Average Estimate', 
            '5% Estimate',
            '95% Estimate'
        ])

    print(info_series)
    plt.show()
