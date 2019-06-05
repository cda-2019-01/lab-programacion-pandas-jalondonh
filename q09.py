##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv
## 
import pandas as pd
import numpy as np
x = pd.read_csv('tbl0.tsv', sep = '\t',thousands = None, decimal = '.')
tbl0c1c2 = pd.DataFrame(x)[['_c1','_c2']]
sortedletras = tbl0c1c2.sort_values(by=['_c1','_c2'])
letraunica = sortedletras.groupby('_c1')['_c2'].apply(list)
mergeletras = pd.merge(sortedletras[['_c1']],letraunica,on='_c1')
mergeletras = mergeletras.rename(columns={'_c1':'_c0','_c2':'_c1'})
def concatenar(list):
    result= ''
    for index, value in enumerate(list,1):
        if index < len(list):
            result += str(value)+':'
        else:
            result += str(value)
    return result

mergeletras['lista']= mergeletras['_c1'].map(lambda x: concatenar(x))
mergeletrasunica = mergeletras[['_c0','lista']].drop_duplicates()
mergeletrasunica = mergeletrasunica.reset_index(drop=True)
print(mergeletrasunica)