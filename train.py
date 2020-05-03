import pandas as pd
from sklearn.linear_model import LinearRegression
from joblib import dump
from preprocess import prep_data

df = pd.read_csv("fish_participant.csv")

X, y = prep_data(df)

model = LinearRegression()
model.fit(X, y)

dump(model, "reg.joblib")