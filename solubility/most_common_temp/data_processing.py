import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


old_df = pd.read_csv("common.csv", index_col=0)
df = pd.DataFrame()
df["smiles"] = old_df["SMILES"]
df["solvent"] = old_df["SMILES_Solvent"]
df["logsol"] = old_df["Solubility"].apply(lambda x:np.log(x))

df_train_val, df_test = train_test_split(df, test_size=0.1, random_state=0)
df_train, df_valid = train_test_split(df_train_val, test_size=1/9, random_state=0)
df_train.to_csv("Single_T_SolDB_train.csv")
df_valid.to_csv("Single_T_SolDB_valid.csv")
df_test.to_csv("Single_T_SolDB_test.v")

