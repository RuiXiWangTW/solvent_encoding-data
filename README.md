# PharmHGT and chemprop Experiment

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

## Referrence
1. Analyzing Learned Molecular Representations for Property Prediction <https://pubs.acs.org/doi/10.1021/acs.jcim.9b00237> 

2. Pharmacophoric-constrained heterogeneous graph transformer model for molecular property prediction <https://www.nature.com/articles/s42004-023-00857-x>

3. Multi-fidelity prediction of molecular optical peaks with deep learning <https://pubs.rsc.org/en/content/articlelanding/2022/sc/d1sc05677h>

4. Minnesota Solvent Descriptor Database <https://comp.chem.umn.edu/solvation/mnsddb.pdf>

5. Solvatochromic Dyes as Solvent Polarity Indicators <https://pubs.acs.org/doi/10.1021/cr00032a005>

6. Toward a Generalized Treatment of the Solvent Effect Based on Four Empirical Scales: Dipolarity (SdP, a New Scale), Polarizability (SP), Acidity(SA), and Basicity (SB) of the Medium <https://pubs.acs.org/doi/10.1021/jp8095727>
7. BigSolDB: Solubility Dataset of Compounds in Organic Solvents and Water in a Wide Range of Temperatures <https://chemrxiv.org/engage/chemrxiv/article-details/6426c1d8db1a20696e4c947b>
8. Chemprop: A Machine Learning Package for Chemical Property Prediction <https://chemrxiv.org/engage/chemrxiv/article-details/656f3bae5bc9fcb5c918caa2>
