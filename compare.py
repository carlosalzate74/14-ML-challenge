import pandas as pd
from sklearn.metrics import mean_squared_error

def compare(y, predictions):
	diff = abs(y - predictions)
	test_df = pd.DataFrame(list(zip(y, predictions, diff.round())), columns = ["y", "predictions", "difference"])

	print(test_df)

	mse = mean_squared_error(y, predictions)

	print(mse)
