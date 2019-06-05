##
## Si la columna _c0 es la clave en las tablas tbl0.tsv
## y tbl2.tsv, compute la suma de tbl2._c5b por cada
## valor en tbl0._c1.
## 
import pandas as pd
import numpy as np
x = pd.read_csv('tbl2.tsv', sep = '\t',thousands = None, decimal = '.')
tbl2 = pd.DataFrame(x)
ordenados = tbl2.sort_values(by=['_c0','_c5a','_c5b'])
grupo_dflista = ordenados.groupby('_c5a')['_c5b'].sum()
print(grupo_dflista)


