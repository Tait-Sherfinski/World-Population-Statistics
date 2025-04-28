import pandas as pd
import numpy as np

data = pd.read_csv("world_population.csv")

np.random.seed(0)
data.head()
missing_values_count = data.isnull().sum()
missing_values_count[0:10]

total_cells = np.product(data.shape)
total_missing = missing_values_count.sum()

# percent of data that is missing
percent_missing = (total_missing/total_cells) * 100
print(percent_missing)