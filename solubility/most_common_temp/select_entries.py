import pandas as pd
import numpy as np

df = pd.read_csv("BigSolDB.csv")
mode = df["T,K"].mode()[0]



df["T,K"] = df["T,K"].apply(lambda x: x if (x == mode) else np.nan)
df.dropna(inplace=True)
df.to_csv("common.csv")
print(df)
print(mode)
