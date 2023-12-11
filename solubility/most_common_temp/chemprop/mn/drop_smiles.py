import pandas as pd
import os
import numpy as np
from rdkit.Chem import AllChem as Chem
import sys

test_data_df = pd.read_csv("./2022_fold_0_test.csv", index_col = 0)

train_data_df = pd.read_csv("./2022_fold_0_train.csv", index_col = 0)

valid_data_df = pd.read_csv("./2022_fold_0_valid.csv", index_col = 0)

test_data_df = test_data_df.drop(columns= ["smiles", "solvent", "logsol"], axis=1)
train_data_df = train_data_df.drop(columns= ["smiles", "solvent", "logsol"], axis=1)
valid_data_df = valid_data_df.drop(columns= ["smiles", "solvent", "logsol"], axis=1)

test_data_df.to_csv("./test_mndescriptor.csv")
train_data_df.to_csv("./train_mndescriptor.csv")
valid_data_df.to_csv("./valid_mndescriptor.csv")