import pandas as pd
import os
import numpy as np
from rdkit.Chem import AllChem as Chem
import sys


#df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

catalan_descriptors = ["SP", "SdP", "SA", "SB"]
mn_descriptors = ["eps","n","alpha","beta","gamma","phi**2","psi**2"]
reichardt_descriptors = ["ET(30) (kcal mol-1)", "ETN"]

catalan_descriptor_df = pd.read_csv("./catalan_solvent_descriptors.csv", index_col=0)
mn_descriptor_df = pd.read_csv("./mn_solvent_descriptors_combined.csv", index_col=0)
reichardt_descriptor_df = pd.read_csv("./reichardt_solvent_descriptors.csv", index_col=0)

test_data_df = pd.read_csv("./sanitized_Single_T_SolDB/2022_fold_0_test.csv", index_col=0)

train_data_df = pd.read_csv("./sanitized_Single_T_SolDB/2022_fold_0_train.csv", index_col=0)

valid_data_df = pd.read_csv("./sanitized_Single_T_SolDB/2022_fold_0_valid.csv", index_col=0)

catalan_mapping = catalan_descriptor_df.to_dict("index")
catalan_descriptor_df_new_mapping = {}
for num in catalan_mapping:
    catalan_descriptor_df_new_mapping[catalan_mapping[num]["smiles"]] = {descriptor: catalan_mapping[num][descriptor] for descriptor in catalan_descriptors}

mn_mapping = mn_descriptor_df.to_dict("index")
mn_descriptor_df_new_mapping = {}
for num in mn_mapping:
    mn_descriptor_df_new_mapping[mn_mapping[num]["smiles"]] = {descriptor: mn_mapping[num][descriptor] for descriptor in mn_descriptors}

reichardt_mapping = reichardt_descriptor_df.to_dict("index")
reichardt_descriptor_df_new_mapping = {}
for num in reichardt_mapping:
    reichardt_descriptor_df_new_mapping[reichardt_mapping[num]["smiles"]] = {descriptor: reichardt_mapping[num][descriptor] for descriptor in reichardt_descriptors}


def sanitize_solvent(smiles):
    try:
        properties = catalan_descriptor_df_new_mapping[smiles]
        properties = mn_descriptor_df_new_mapping[smiles]
        properties = reichardt_descriptor_df_new_mapping[smiles]
    except:
        smiles = np.nan
    return smiles



train_data_df['solvent'] = train_data_df['solvent'].apply(lambda x: sanitize_solvent(x))
train_data_df.dropna(inplace=True)


valid_data_df['solvent'] = valid_data_df['solvent'].apply(lambda x: sanitize_solvent(x))
valid_data_df.dropna(inplace=True)

test_data_df['solvent'] = test_data_df['solvent'].apply(lambda x: sanitize_solvent(x))
test_data_df.dropna(inplace=True)

train_data_df.drop(train_data_df.columns[train_data_df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
valid_data_df.drop(valid_data_df.columns[valid_data_df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
test_data_df.drop(test_data_df.columns[test_data_df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

test_data_df.to_csv("./compatable/2022_fold_0_test.csv")
train_data_df.to_csv("./compatable/2022_fold_0_train.csv")
valid_data_df.to_csv("./compatable/2022_fold_0_valid.csv")


catalan_test_data_df = pd.read_csv("./compatable/2022_fold_0_test.csv", index_col=0)

catalan_train_data_df = pd.read_csv("./compatable/2022_fold_0_train.csv", index_col=0)

catalan_valid_data_df = pd.read_csv("./compatable/2022_fold_0_valid.csv", index_col=0)

for descriptor in catalan_descriptors:
    catalan_test_data_df[descriptor] = catalan_test_data_df["solvent"].map(lambda x: catalan_descriptor_df_new_mapping[x][descriptor])
    catalan_train_data_df[descriptor] = catalan_train_data_df["solvent"].map(lambda x: catalan_descriptor_df_new_mapping[x][descriptor])
    catalan_valid_data_df[descriptor] = catalan_valid_data_df["solvent"].map(lambda x: catalan_descriptor_df_new_mapping[x][descriptor])

catalan_test_data_df.to_csv("./catalan/2022_fold_0_test.csv")
catalan_train_data_df.to_csv("./catalan/2022_fold_0_train.csv")
catalan_valid_data_df.to_csv("./catalan/2022_fold_0_valid.csv")


mn_test_data_df = pd.read_csv("./compatable/2022_fold_0_test.csv", index_col=0)

mn_train_data_df = pd.read_csv("./compatable/2022_fold_0_train.csv", index_col=0)

mn_valid_data_df = pd.read_csv("./compatable/2022_fold_0_valid.csv", index_col=0)


for descriptor in mn_descriptors:
    mn_test_data_df[descriptor] = mn_test_data_df["solvent"].map(lambda x: mn_descriptor_df_new_mapping[x][descriptor])
    mn_train_data_df[descriptor] = mn_train_data_df["solvent"].map(lambda x: mn_descriptor_df_new_mapping[x][descriptor])
    mn_valid_data_df[descriptor] = mn_valid_data_df["solvent"].map(lambda x: mn_descriptor_df_new_mapping[x][descriptor])

mn_test_data_df.to_csv("./mn/2022_fold_0_test.csv")
mn_train_data_df.to_csv("./mn/2022_fold_0_train.csv")
mn_valid_data_df.to_csv("./mn/2022_fold_0_valid.csv")


reichardt_test_data_df = pd.read_csv("./compatable/2022_fold_0_test.csv", index_col=0)

reichardt_train_data_df = pd.read_csv("./compatable/2022_fold_0_train.csv", index_col=0)

reichardt_valid_data_df = pd.read_csv("./compatable/2022_fold_0_valid.csv", index_col=0)

for descriptor in reichardt_descriptors:
    reichardt_test_data_df[descriptor] = reichardt_test_data_df["solvent"].map(lambda x: reichardt_descriptor_df_new_mapping[x][descriptor])
    reichardt_train_data_df[descriptor] = reichardt_train_data_df["solvent"].map(lambda x: reichardt_descriptor_df_new_mapping[x][descriptor])
    reichardt_valid_data_df[descriptor] = reichardt_valid_data_df["solvent"].map(lambda x: reichardt_descriptor_df_new_mapping[x][descriptor])

reichardt_test_data_df.to_csv("./reichardt/2022_fold_0_test.csv")
reichardt_train_data_df.to_csv("./reichardt/2022_fold_0_train.csv")
reichardt_valid_data_df.to_csv("./reichardt/2022_fold_0_valid.csv")

