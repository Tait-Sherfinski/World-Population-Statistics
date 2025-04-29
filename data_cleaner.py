import pandas as pd
import numpy as np

data = pd.read_csv("world_population.csv")

np.random.seed(0)
data.head()
missing_values_count = data.isnull().sum()
missing_values_count[0:10]

total_cells = np.product(data.shape)
total_missing = missing_values_count.sum()

percent_missing = (total_missing/total_cells) * 100
print(percent_missing)
missing_values_count[0:10]

data.dropna()
columns_with_na_dropped = data.dropna(axis=1)
columns_with_na_dropped.head()

print("Columns in original dataset: %d \n" % data.shape[1])
print("Columns with na's dropped: %d" % columns_with_na_dropped.shape[1])

subset_data = data.loc[:, 'Rank':'Capital'].head()
subset_data

subset_data.fillna(0)
subset_data.fillna(method='bfill', axis=0).fillna(0)
