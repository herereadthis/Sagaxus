# scikit-learn

What is a <strong>learning problem?</strong> Consider a set of <em>n</em> samples of data and try to predict properties of unknown data. If the sample is multi-dimensional, then it has several attributes or features

* <strong>Supervised learning</strong> - the data hs additional attributes we want to predict
  * <strong>Classification</strong> - samples belong to 2 or more classes, and by using already labelled data, predict the class of unlabeled data. In other words, classification is a discrete form of supervised learning where there are a limited number of categories, and for each of the <em>n</em> samples, try to to label each of them into the correct category. For example, try to to recognized numbers from handwriting.
  * <strong>Regression</strong> - try to predict from one or more continuous variables. For example, try to predict height from a person&rsquo;s age and weight.
* <strong>Unsupervised learning</strong> - the training data has a set of <em>x</em> input vectors and there are no corresponding target values. There are a few goals here:
  * <strong>Clustering</strong> - find groups of similar examples within the data
  * <strong>Density Estimation</strong> - determine the distribution of data
  * <strong>Visualization</strong> - project the data from higher to lower dimensions

To learn about a data set, it is commonly split in two. On the <strong>training set</strong> we try to learn some properties, and then we see if those properties also apply to the <strong>testing set</strong>


### Linear Regression models


`sklearn.linear_model.LinearRegression`
* Ordinary Least Squares (OLS) Linear Regression
`sklearn.linear_model.ElasticNet`
* Elastic Net Regularization
`sklearn.linear_model.RandomForestRegressor`
`sklearn.linear_model.ExtraTreesRegressor`
`sklearn.linear_model.GradientBoostingRegressor`
`sklearn.linear_model.GradientBoostingRegressor`
