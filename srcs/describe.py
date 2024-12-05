
# Modules
# %%
from DataScience import DataScience as dt
import pandas as pd
import params as p

# %%
# Importing and extracting csv into df
df =  pd.read_csv(p.path_dataset_train)

# %%
# outputting content into a file 
with open("describe_dataset_train.txt", "w") as f:
	f.write(df.to_string())
 
# %%
# Retrieving numerical columms from the df
numeric_features = dt.numerical_columns(df)

# Defining count (list of sum of valid feature value)
lstCount = dt.count(numeric_features)

# Defining mean (list of mean of each feature)
lstMean = dt.mean(numeric_features)

# Defines the standard deviation (list of std per feature)
lstStd = dt.std(numeric_features, lstMean)


index = ["Count", "Mean", "Std", "Min", "25%", "50%", "70%", "Max"]
# new_df = pd.DataFrame(index=index, columns=df.columns[df.columns.find("Arithmancy")]:)
# print(new_df)
# dt.count(df)

# %%
