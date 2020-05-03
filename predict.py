from joblib import load
from preprocess import prep_data
from compare import compare
import pandas as pd
from sklearn.metrics import mean_squared_error

def predict_from_csv(path_to_csv):

    df = pd.read_csv(path_to_csv)
    X, y = prep_data(df)

    reg = load("reg.joblib")

    predictions = reg.predict(X)

    compare(y, predictions)

    return predictions

if __name__ == "__main__":
    predictions = predict_from_csv("fish_holdout_demo.csv")
    print(predictions)

    # ho_predictions = predict_from_csv("fish_holdout_demo.csv")
    # ho_truth = pd.read_csv("fish_holdout_demo.csv")["Weight"].values
    # ho_mse = mean_squared_error(ho_truth, ho_predictions)
    # print(ho_mse)