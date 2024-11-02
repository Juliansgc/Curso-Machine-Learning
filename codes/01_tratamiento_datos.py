import pandas as pd
import numpy as np

df = pd.read_csv("dataset_1.csv", index_col=0)

print(df)
print(df.describe())
