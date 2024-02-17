import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

# read dataset into dataframe
goalieData = pd.read_csv("data.csv", header = 0)

# seperate into X and y
X = goalieData.loc[:, 'games_played':'sv_pct']
y = goalieData['next_sv_pct']

# split the data for training and validation
X_train, X_valid, y_train, y_valid = train_test_split(X,y,train_size=0.75)

# create model, then train and score
rmodel = RandomForestRegressor(n_estimators = 100,
                               max_depth = 10,
                               min_samples_leaf = 10)
rmodel.fit(X_train, y_train)

print(rmodel.score(X_train, y_train))
print(rmodel.score(X_valid, y_valid))
print()

col_names = pd.Series(list(X.columns))
col_importances = pd.Series(rmodel.feature_importances_)
X_importances = {"names": col_names, 
                 "importance":col_importances}
importance_df = pd.concat(X_importances, axis = 1)

print('feature importances: ')
print(importance_df.sort_values(by = ['importance'], ascending = False))
