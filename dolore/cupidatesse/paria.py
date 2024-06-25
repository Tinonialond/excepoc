from sklearn.impute import SimpleImputer

# Create an instance of the SimpleImputer class with a constant value of 0
imputer = SimpleImputer(strategy='constant', fill_value=0)

# Fit the imputer to the data and transform the dataset
imputed_data = imputer.fit_transform(data)
