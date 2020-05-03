import pandas as pd
from sklearn import linear_model
from sklearn.ensemble import RandomForestRegressor
from joblib import dump
from preprocess import prep_data

df = pd.read_csv("fish_participant.csv")

X, y = prep_data(df)

# model = linear_model.LinearRegression() # 5559 - 0.036
# model = linear_model.Lasso(alpha=0.1) # 5561 - 0.071
# model = linear_model.Ridge(alpha=0.1, fit_intercept=False) # 5457 - 0.047
# model = linear_model.OrthogonalMatchingPursuit(n_nonzero_coefs=4) # 5104 - 0.036

model = RandomForestRegressor(criterion="mse") #580 - 0.003

model.fit(X, y)

dump(model, "reg.joblib")