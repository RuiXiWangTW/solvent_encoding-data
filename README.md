# PharmHGT Experiment

## Introduction
* Augmented model that runs the experiment in the solvent-encoding project modified from PharmHGT and chemprop.

## Environment
* base dependencies:
```
  - dgl
  - wandb
  - numpy
  - pandas
  - python>=3.7
  - pytorch>=1.7.1
  - rdkit
  - chemprop
```

## Experiment on mn descriptor on PharmHGT:
```bash
cd PharmHGT_modified
python descriptor_train.py configs/sanitized_Single_T_SolDB_mn_all.json
```
## Experiment on catalan descriptor on PharmHGT:
```bash
cd PharmHGT_modified
python descriptor_train.py configs/sanitized_Single_T_SolDB_catalan_all.json
```
## Experiment on reichardt descriptor on PharmHGT:
```bash
cd PharmHGT_modified
python descriptor_train.py configs/sanitized_Single_T_SolDB_reichardt_all.json
```
## Experiment on graph-augmentation on PharmHGT:
```bash
cd PharmHGT_modified
python solvent_train.py configs/sanitized_Single_T_SolDB_graph_all.json
```

## Experiment on mn descriptor on chemprop:
```bash
cd chemprop
chemprop_train --data_path 2022_fold_0_train.csv --separate_test_path 2022_fold_0_test.csv --separate_val_path 2022_fold_0_valid.csv --save_dir model --save_preds --dataset_type regression --features_path train_mndescriptor.csv --separate_val_features_path valid_mn_descriptor.csv --separate_test_features_path test_mndescriptor.csv --epoch 200 --target_columns logsol --number_of_molecules 1 --smiles_columns smiles
```

## Experiment on catalan descriptor on chemprop:
```bash
cd chemprop
chemprop_train --data_path 2022_fold_0_train.csv --separate_test_path 2022_fold_0_test.csv --separate_val_path 2022_fold_0_valid.csv --save_dir model --save_preds --dataset_type regression --features_path train_catalandescriptor.csv --separate_val_features_path valid_catalandescriptor.csv --separate_test_features_path test_catalandescriptor.csv --epoch 200 --target_columns logsol --number_of_molecules 1 --smiles_columns smiles
```

## Experiment on reichardt descriptor on chemprop:
```bash
cd chemprop
chemprop_train --data_path 2022_fold_0_train.csv --separate_test_path 2022_fold_0_test.csv --separate_val_path 2022_fold_0_valid.csv --save_dir model --save_preds --dataset_type regression --features_path train_catalandescriptor.csv --separate_val_features_path valid_catalandescriptor.csv --separate_test_features_path test_catalandescriptor.csv --epoch 200 --target_columns logsol --number_of_molecules 1 --smiles_columns smiles
```

## Experiment on graph-augmentation on chemprop:
```bash
cd chemprop
chemprop_train --data_path 2022_fold_0_train.csv --separate_test_path 2022_fold_0_test.csv --separate_val_path 2022_fold_0_valid.csv --save_dir model --save_preds --dataset_type regression --epoch 200 --target_columns logsol --number_of_molecules 2 --smiles_columns smiles solvent
```
