import pandas as pd
from sklearn.metrics import mean_squared_error

def compare(y, predictions):
	error2 = abs(y - predictions) ** 2
	diff_df = pd.DataFrame(list(zip(y, predictions, error2.round(3))), columns = ["y", "predictions", "error2"])

	# print(diff_df)

	# diff_df.to_csv("tests/diff_RFR.csv")

	mse = round(mean_squared_error(y, predictions), 3)

	print(mse)
