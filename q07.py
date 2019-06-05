##
## Agregue una columna  con la suma de _c0 y _c2 a la tabla tbl0.tsv 
## 
import pandas as pd
import numpy as np
x = pd.read_csv('tbl0.tsv', sep = '\t',thousands = None, decimal = '.')
dfx = pd.DataFrame(x)
dfx['suma'] = dfx['_c0']+dfx['_c2']
print(dfx)

