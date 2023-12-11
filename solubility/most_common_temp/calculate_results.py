import pandas as pd
import numpy as np
from sklearn.metrics import r2_score

true = pd.read_csv("Single_T_SolDB_test.csv")["logsol"]
preds = pd.read_csv("chemprop_multigraph/test_preds.csv")["logsol"]
print(r2_score(true, preds))