import pandas as pd
import numpy as np
from joblib import dump
from preprocess import prep_data
from compare import compare

from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.metrics import mean_squared_error


df = pd.read_csv("fish_participant.csv")

X, y = prep_data(df)

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Train
model = ExtraTreesRegressor(n_estimators=150, criterion="mse")
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# compare(y_test, y_pred)

# Accuracy
acc = model.score(X_test, y_test)
print("acc: %.2f%%" % (acc*100.0))

# mse = mean_squared_error(y_test, y_pred)
# print("mse: %.2f" % mse)

dump(model, "reg.joblib")




