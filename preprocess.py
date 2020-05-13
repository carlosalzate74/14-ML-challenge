import pandas as pd
import numpy as np

from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import QuantileTransformer, MinMaxScaler


# Removes outlies by feature and specie
def remove_outliers(df):
	np.seterr(divide='ignore', invalid='ignore')
	cols = ["Length1", "Length2", "Length3", "Height", "Width"]	
	# Add and id based on the df's index
	df["id"]= df.index
	species = df.Species.unique()

	# Loop through features
	for col in cols:		
		# Column to sum adjusted values from all column_specie
		df[col + "_ro"] = 0

		# Loop through species
		for specie in species:
			X = df.loc[df["Species"] == specie]
			X = X[["id", "Species", col]]
			# Calculate mean by specie
			df_mean = df.groupby(["Species"])[col].mean()
			X = X.merge(df_mean, how="left", on="Species", suffixes=("", "_mean_" + specie))

			# Identify outlier by feature and specie
			X[col + "_outl_" + specie] = IsolationForest(behaviour="new", contamination="auto").fit_predict(X[[col]])

			# Replace outliers with mean by feature and specie 
			X[col + "_ro_" + specie] = np.where(X[col + "_outl_" + specie] == 1, X[col], X[col + "_mean_" + specie])
			X = X[["id", col + "_ro_" + specie]]
			df = df.merge(X, how="left", on="id")

			# Combine adjusted columns by feature
			df[col + "_ro_" + specie] = df[col + "_ro_" + specie].fillna(0)
			df[col + "_ro"] = df[col + "_ro"] + df[col + "_ro_" + specie]
			df = df.drop(col + "_ro_" + specie, axis=1)

	return df

# Add calculated features
def add_features(df):

	# Air density
	p = 1.225

	# Calculate Max length
	df = df.assign(Lmax=df[["Length1_ro", "Length2_ro", "Length3_ro"]].min(axis=1))

	# Calculate Average length
	df = df.assign(Lavg=df[["Length1_ro", "Length2_ro", "Length3_ro"]].mean(axis=1))
	
	# Calculate Mass
	df = df.assign(Mass=p * df["Height_ro"] * df["Width_ro"] * df["Lmax"])

	# # Calculate Volume
	df = df.assign(Volume=df["Height_ro"] * df["Width_ro"] * df["Lmax"])

	# Round all columns
	df = df.round(decimals=3)

	return df

# Normalize and Scale features
def normalize(df, features):
	for col in features:
		X = df.iloc[:, df.columns == col]

		# Normalize feature by quantiles
		X_trans = QuantileTransformer(n_quantiles=20, output_distribution='normal').fit_transform(X)
		df[col + "_QT"] = X_trans

		# Scale normalized feature to its original range
		X_trans = MinMaxScaler(feature_range=(X[col].min(), X[col].max())).fit_transform(X_trans)
		df[col + "_MMS"] = X_trans

		# Clean dataframe
		df = df[df.columns.drop(list(df.filter(regex='_QT')))]
	return df



def prep_data(df):

	df = remove_outliers(df)

	df = add_features(df)

	# Exclude Species
	X = df.iloc[:, df.columns != "Species"]
	y = df.iloc[:,1] #Weight

	# Convert to Dataframe
	X = pd.DataFrame(data= X, columns=X.columns)

	# Calculate correlation for feature selection
	X = X.drop("id", axis=1)
	cor = X.corr()

	cor_target = abs(cor["Weight"])
	criteria = 0.74

	all_features = cor_target[cor_target>0.001]
	# print(all_features.sort_values(ascending=False))
	relevant_features = cor_target[cor_target>criteria]
	# print(relevant_features.index)

	features = relevant_features.index
	
	df = normalize(df, features)

	X = X[['Weight', 'Length1', 'Length2', 'Length3', 'Width', 'Width_ro']]

	return X, y
