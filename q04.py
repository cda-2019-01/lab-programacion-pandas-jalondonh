##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 
import pandas as pd
import numpy as np
x = pd.read_csv('tbl1.tsv', sep = '\t',thousands = None, decimal = '.')
xc4 = pd.Series(x['_c4']).sort_values()
listxc4 = xc4.unique().tolist()
listxc4upper = [x.upper() for x in listxc4]
print(listxc4upper)