import pandas as pd
import numpy as np

from sklearn.metrics import mean_squared_error

def compare(y, predictions):
	error2 = (abs(y - predictions) ** 2)
	diff = abs(y - predictions)

	df_diff = pd.DataFrame(list(zip(y.round(2), predictions.round(2), diff.round(2))), columns = ["y", "predictions", "diff"])

	print(df_diff)
