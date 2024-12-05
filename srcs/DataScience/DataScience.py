
# %%
import pandas as pd
import numpy as np
import math

# %%
def numerical_columns(df):
	"""
	Summary: Creates a new dataframe and retrieves from df the columns
	with numerical values
	Return: Returns the new numerical dataframe
	"""
	new_df = pd.DataFrame()
	loc = 0
	types = df.dtypes
 
	# inserting numerical columns from df to new_df
	for i in range(0, len(types)):
		if types.iloc[i] == "float64" or types.iloc[i] == "int":
				if df.columns[i].upper() != "INDEX":
					new_df.insert(column=df.columns[i], value=df[df.columns[i]], loc=loc)
					loc += 1
	return new_df

# %%

def count_valid_values(values):
	counter = 0
	for el in values:
		if math.isnan(el) is False:
			counter += 1
	return counter

def count(df):
	"""
	Summary: Defines ans returns into a list the number of valide 
 	feature values of each feature from df.
	"""
	lst_count = [count_valid_values(df[el]) for el in df.columns]
	print(lst_count)
	# return lst_count

def mean(df):
	"""
	Summary: Defines and returns the mean of each feature in df.
	"""
	lst_mean = [np.sum(df[el]) / df[el].size for el in df.columns]
	print(lst_mean)
	return lst_mean

def std(df, lst_mean):
    lst_std = [ ((sum(df[col]) - (mean * df[col].size)) ** (2 ** df[col].size)) / df[col].size  for col, mean in zip(df.columns, mean)]

   