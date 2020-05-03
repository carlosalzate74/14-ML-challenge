def prep_data(df):
	# Air density
	p = 1

	# Get the max length
	df = df.assign(Lmax=df[["Length1", "Length2", "Length3"]].max(axis=1))
	
	# Calculate the mass = p * height * width * max length
	df = df.assign(Mass=p * df["Height"] * df["Width"] * df["Lmax"])

	# Calculate Matrix and Target
	X = df[["Height", "Width", "Lmax", "Mass"]].values
	y = df["Weight"].values
	
	return X, y