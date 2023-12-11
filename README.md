# PharmHGT Experiment

## Introduction
* Augmented model that runs the experiment in "" modified from "Pharmacophoric-constrained Heterogeneous Graph Transformer".

* We design a pharmacophoric-constrained multi-views molecular representation graph, enabling PharmHGT to extract vital chemical information from functional substructures and chemical reactions. With a carefully designed pharmacophoric constrained multi-view molecular representation graph, PharmHGT can learn more chemical information from molecular functional substructures and chemical reaction information. 

![Heterogeneous Molecular Graph](images/Fig.1.png)


## Dataset
All data used in this paper are publicly available on [Molecule-Net](http://moleculenet.org/datasets-1).

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
