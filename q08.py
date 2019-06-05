##
## Agregue el año como una columna a la tabla tbl0.tsv 
## 
import pandas as pd
import numpy as np
import datetime
x = pd.read_csv('tbl0.tsv', sep = '\t',thousands = None, decimal = '.')
dfx = pd.DataFrame(x)
dfx['ano'] = pd.Series(dfx['_c3']).str.extract('^([0-9]{4})')
print(dfx)