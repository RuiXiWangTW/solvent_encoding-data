# PharmHGT Experiment

## Introduction
* Augmented model that runs the experiment in the solvent-encoding project modified from "Pharmacophoric-constrained Heterogeneous Graph Transformer".

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
```

## Experiment on mn descriptor:
```bash
python descriptor_train.py configs/sanitized_Single_T_SolDB_mn_all.json
```
## Experiment on catalan descriptor:
```bash
python descriptor_train.py configs/sanitized_Single_T_SolDB_catalan_all.json
```
## Experiment on reichardt descriptor:
```bash
python descriptor_train.py configs/sanitized_Single_T_SolDB_reichardt_all.json
```
## Experiment on graph-augmentation:
```bash
python solvent_train.py configs/sanitized_Single_T_SolDB_graph_all.json
```
